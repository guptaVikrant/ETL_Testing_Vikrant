import pandas as pd
import oracledb
import pymysql
from sqlalchemy import create_engine, URL

mysql_url = URL.create(
    "mysql+pymysql",
    username="root",
    password="Radha@150683",
    host="localhost",
    port=3306,
    database="vikrantdb"
)

mysql_conn = create_engine(mysql_url)
#mysql_conn=create_engine("mysql+pymysql://root:Radha%40150683@localhost:3306/vikrantdb")
mysql_query1="""
SELECT *
FROM product
"""

oracle_url = URL.create(
    "oracle+oracledb",
    username="system",
    password="Radha@150683",
    host="192.168.1.2",
    port=1521,
    query={"service_name": "XEPDB1"}
)

oracle_conn = create_engine(oracle_url)
#oracle_conn=create_engine("oracle+oracledb://system:Radha@150683@192.168.1.2:1521/XEPDB1")
oracle_query1="""
SELECT *
FROM product
"""
df_source=pd.read_sql(oracle_query1,oracle_conn)
print("Data from source",end="\n")
df_source = df_source.reset_index(drop=True)
print(df_source)
print("Data from target",end="\n")
df_target=pd.read_sql(mysql_query1,mysql_conn)

df_target = df_target.reset_index(drop=True)
print(df_target)
'''
print("Data difference from target",end="\n")
df_difference=df_source.compare(df_target)
print(df_difference)'''
'''
Scenario 1 : Source is CSV file and Target is relational db mySQL database. 
Check if all the values from eno column from source is loaded in target.'''
df_result = df_source['product_id'].isin(df_target['product_id'])
print(df_result)