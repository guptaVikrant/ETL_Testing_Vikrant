import pandas as pd
from sqlalchemy import create_engine, URL
mysql_url = URL.create(
    "mysql+pymysql",
    username="admin",
    password="Radha_150683",
    host="vikkydb-1.cns6q62e0zoz.ap-south-1.rds.amazonaws.com",
    port=3306,
    database="Sales_databse"
)
rds_conn = create_engine(mysql_url)
#read_data_from_rds():
mysql_query1="""
SELECT *
FROM product
"""
df = pd.read_sql(mysql_query1,rds_conn)
print(df.head())