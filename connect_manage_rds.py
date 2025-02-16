import mysql.connector
import os
#與 RDS 連線（不指定 DB Name）
connection = mysql.connector.connect(
    host=os.getenv('RDS_HOST'),
    user=os.getenv('RDS_USER'),
    password=os.getenv('RDS_PASSWORD'),
    port=os.getenv('RDS_PORT')
)

cursor = connection.cursor()
# cursor.execute("SHOW DATABASES;")
# for db in cursor:
#     print(db)
#
# cursor.execute("CREATE DATABASE IF NOT EXISTS buysideRDS;")

cursor.execute("USE buysideRDS;")
for response in cursor:
    print(response)

# cursor.execute("DROP TABLE test0212;")
# for response in cursor:
#     print(response)

cursor.execute("SHOW TABLES;")
for table in cursor:
    print(table)

# cursor.execute("SELECT * FROM farm_trade_data WHERE trade_date >= CURDATE() - INTERVAL 1 MONTH;")
# for row in cursor:
#     print(row)

cursor.execute("SELECT * FROM farm_trade_data WHERE trade_date = '2025-02-16';")
for row in cursor:
    print(row)

# cursor.execute("SELECT * FROM users;")
# for d in cursor:
#     print(d)
# 關閉連線
cursor.close()
connection.close()
