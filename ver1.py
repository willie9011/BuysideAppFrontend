import requests
import pandas as pd
from sqlalchemy import create_engine, text
import os
import json
import socket
from datetime import datetime, timedelta
import calendar


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


# ---------------------------- 分區管理功能 ----------------------------
def manage_partitions(engine, months_ahead=24):
    """
    動態管理分區：確保至少有未來24個月的分區
    """
    print("開始管理分區...")

    # 獲取當前日期
    current_date = datetime.now()

    # 建立基礎表（如果不存在）
    create_base_table_sql = text("""
    CREATE TABLE IF NOT EXISTS farm_trade_data (
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
    PARTITION BY RANGE ( YEAR(trade_date) * 100 + MONTH(trade_date))
    (PARTITION p_future VALUES LESS THAN MAXVALUE);
    """)

    # 獲取現有分區
    get_partitions_sql = text("""
    SELECT PARTITION_NAME, PARTITION_DESCRIPTION 
    FROM INFORMATION_SCHEMA.PARTITIONS 
    WHERE TABLE_NAME = 'farm_trade_data';
    """)

    try:
        with engine.connect() as conn:
            # 建立表（如果不存在）
            conn.execute(create_base_table_sql)
            conn.commit()
            print("基礎表檢查/創建完成")

            # 獲取現有分區
            existing_partitions = conn.execute(get_partitions_sql).fetchall()
            existing_partition_values = {p[0]: int(p[1]) for p in existing_partitions if p[0] != 'p_future'}
            print(f"現有分區數量: {len(existing_partition_values)}")

            # 計算需要的分區
            needed_partitions = {}
            date = current_date
            for _ in range(months_ahead):
                partition_value = date.year * 100 + date.month
                next_month = date.month % 12 + 1
                next_year = date.year + (date.month == 12)
                partition_name = f'p_{date.year}{str(date.month).zfill(2)}'
                needed_partitions[partition_name] = (partition_value, next_year * 100 + next_month)

                # 移到下一個月
                if date.month == 12:
                    date = date.replace(year=date.year + 1, month=1)
                else:
                    date = date.replace(month=date.month + 1)

            # 創建缺少的分區
            for partition_name, (_, upper_bound) in needed_partitions.items():
                if partition_name not in existing_partition_values:
                    try:
                        # 先刪除 MAXVALUE 分區
                        drop_maxvalue_sql = text("""
                        ALTER TABLE farm_trade_data DROP PARTITION p_future;
                        """)

                        # 添加新分區
                        add_partition_sql = text(f"""
                        ALTER TABLE farm_trade_data ADD PARTITION (
                            PARTITION {partition_name} VALUES LESS THAN ({upper_bound})
                        );
                        """)

                        # 重新添加 MAXVALUE 分區
                        add_maxvalue_sql = text("""
                        ALTER TABLE farm_trade_data ADD PARTITION (
                            PARTITION p_future VALUES LESS THAN MAXVALUE
                        );
                        """)

                        print(f"添加分區: {partition_name}")
                        conn.execute(drop_maxvalue_sql)
                        conn.execute(add_partition_sql)
                        conn.execute(add_maxvalue_sql)
                        conn.commit()
                    except Exception as e:
                        print(f"創建分區 {partition_name} 時出錯: {str(e)}")
                        raise

            print("分區管理完成")

    except Exception as e:
        print(f"分區管理過程中發生錯誤: {str(e)}")
        raise


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
            raise ValueError("某些必要的環境變數未設置")

        # 測試是否能連上外網
        if not test_internet_connectivity():
            raise RuntimeError("Lambda 無法連接外部網路，請檢查 VPC、NAT Gateway 設定")

        # 測試 API 是否可用
        data = test_url_connectivity(env_url)
        if data is None:
            raise RuntimeError("API 無法連線，請確認 NAT 設定或 API 是否可用")

        # ------------------------------ JSON 轉 DataFrame ------------------------------
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("從 API 取得的資料無效或為空")

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

        try:
            # 管理分區
            manage_partitions(engine, months_ahead=24)

            # 檢查今天的數據是否已存在
            current_date = datetime.now().date()
            check_sql = text("""
                SELECT COUNT(*) 
                FROM farm_trade_data 
                WHERE trade_date = :current_date
            """)

            with engine.connect() as conn:
                result = conn.execute(check_sql, {"current_date": current_date}).scalar()
                if result > 0:
                    print(f"今天 ({current_date}) 的數據已存在，跳過插入")
                else:
                    # 插入新數據
                    df.to_sql(
                        'farm_trade_data',
                        con=engine,
                        if_exists='append',
                        index=False,
                        method='multi',
                        chunksize=1000
                    )
                    print(f"成功插入 {len(df)} 筆新數據")

        except Exception as e:
            raise RuntimeError(f"處理資料時發生錯誤: {str(e)}")

    except Exception as e:
        print(f"Lambda 執行錯誤: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            })
        }

    finally:
        if 'engine' in locals():
            engine.dispose()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "success",
            "message": "數據處理完成",
            "timestamp": datetime.now().isoformat()
        })
    }