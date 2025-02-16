import requests
import pandas as pd
from sqlalchemy import create_engine, text
import os
import json
import socket
from datetime import datetime


# ---------------------------- 測試外網連線 ----------------------------
def test_internet_connectivity():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Lambda 連接外部網路成功")
        return True
    except OSError:
        print("Lambda 無法連接外部網路")
        return False


def test_url_connectivity(url):
    try:
        print(f"測試連線: {url}")
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print("API 連線成功")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"無法連接 API: {e}")
        return None


# ---------------------------- Lambda 入口函數 ----------------------------
def lambda_handler(event, context):
    try:
        # 讀取環境變數
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("BUYSIDE_DBPORT")
        db_name = os.getenv("BUYSIDE_DBNAME")
        db_user = os.getenv("BUYSIDE_DBUSER")
        db_password = os.getenv("BUYSIDE_DBPASSWORD")
        env_url = os.getenv("ENV_URL")

        if not all([db_host, db_port, db_name, db_user, db_password, env_url]):
            raise ValueError("某些必要的變數未設置")

        # 測試是否能連上外網
        if not test_internet_connectivity():
            raise RuntimeError("無法連接外部網路")

        # 測試 API 是否可用
        data = test_url_connectivity(env_url)
        if data is None:
            raise RuntimeError("API無法連線")

        # ------------------------------ JSON 轉 DataFrame ------------------------------
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("API取得的資料無效或為空")

        df = pd.DataFrame(data)

        # ---------------------------- 數據清理與轉換 ----------------------------
        def convert_date(date_str):
            try:
                year, month, day = date_str.split('.')
                year = int(year) + 1911
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            except:
                return None

        df['交易日期'] = df['交易日期'].apply(convert_date)
        df['交易日期'] = pd.to_datetime(df['交易日期'], errors="coerce")

        numeric_columns = ['上價', '中價', '下價', '平均價', '交易量']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        column_mapping = {
            '交易日期': 'trade_date',
            '種類代碼': 'category_code',
            '作物代號': 'crop_code',
            '作物名稱': 'crop_name',
            '市場代號': 'market_code',
            '市場名稱': 'market_name',
            '上價': 'high_price_per_kg',
            '中價': 'medium_price_per_kg',
            '下價': 'low_price_per_kg',
            '平均價': 'average_price_per_kg',
            '交易量': 'trade_volume_kg'
        }
        existing_columns = {k: v for k, v in column_mapping.items() if k in df.columns}
        df.rename(columns=existing_columns, inplace=True)

        # ------------------------------ 連接 MySQL ------------------------------
        engine = create_engine(
            f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
            pool_recycle=3600
        )

        # ----------------------------- 建立分表 -----------------------------
        def create_partitioned_table(engine):
            drop_table_sql = text("DROP TABLE IF EXISTS farm_trade_data;")
            create_table_sql = text("""
            CREATE TABLE farm_trade_data (
                trade_date DATE,
                category_code VARCHAR(10),
                crop_code VARCHAR(10),
                crop_name VARCHAR(50),
                market_code VARCHAR(10),
                market_name VARCHAR(50),
                high_price_per_kg FLOAT,
                medium_price_per_kg FLOAT,
                low_price_per_kg FLOAT,
                average_price_per_kg FLOAT,
                trade_volume_kg FLOAT,
                PRIMARY KEY (trade_date, crop_code, market_code)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            PARTITION BY RANGE ( YEAR(trade_date) * 100 + MONTH(trade_date)) (
                PARTITION p_202401 VALUES LESS THAN (202402),
                PARTITION p_202402 VALUES LESS THAN (202403),
                PARTITION p_202403 VALUES LESS THAN (202404),
                PARTITION p_202404 VALUES LESS THAN (202405),
                PARTITION p_202405 VALUES LESS THAN (202406),
                PARTITION p_202406 VALUES LESS THAN (202407),
                PARTITION p_202407 VALUES LESS THAN (202408),
                PARTITION p_202408 VALUES LESS THAN (202409),
                PARTITION p_202409 VALUES LESS THAN (202410),
                PARTITION p_202410 VALUES LESS THAN (202411),
                PARTITION p_202411 VALUES LESS THAN (202412),
                PARTITION p_202412 VALUES LESS THAN (202501),
                PARTITION p_future VALUES LESS THAN MAXVALUE
            );
            """)

            with engine.connect() as conn:
                conn.execute(drop_table_sql)
                conn.execute(create_table_sql)
                conn.commit()
                print("Partitioned table created successfully")

        # ----------------------------- 插入數據 -----------------------------
        try:
            create_partitioned_table(engine)
            df.to_sql(
                'farm_trade_data',
                con=engine,
                if_exists='append',
                index=False,
                method='multi',
                chunksize=1000
            )
            print("Data inserted successfully")
        except Exception as e:
            raise RuntimeError(f"插入資料時發生錯誤: {str(e)}")

    except Exception as e:
        print(f"Lambda 執行錯誤: {e}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

    finally:
        engine.dispose()

    return {"status": "success"}
