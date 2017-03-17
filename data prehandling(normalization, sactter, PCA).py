# Principle Component Analysis for Jindong
import pandas as pda
import pymysql
import numpy as npy

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test", charset = "utf8")
sql = "select * from taob"
data = pda.read_sql(sql, conn)
'''
data1 = data
for i in range(len(data1["price"])):
    if data1["price"][i].isdigit():
        print()
    else:
        int(data1["price"][i])

print(data.describe())
'''           
               
               


#print(data)
#print(data - data.min())
# Normalize Data
#(1)min-max normalization
#data2 =(data - data.min())/(data.max()-data.min())
#print(data2)
