import pymysql
import numpy as npy
import pandas as pda

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test", charset = "utf8")
sql = "select * from taob"
data = pda.read_sql(sql, conn)
print(data.describe())
