import pymysql
import pandas as pda
import numpy as npy

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test", charset = "utf8")
sql = "select price, comment from taob"
data = pda.read_sql(sql, conn)

print(data.describe())

#Min-Max Normalization
data2 =(data-data.min())/(data.max()-data.min())
print(data2)

#Z-score Normalization
data3 = (data - data.mean())/data.std()
print(data3)

#normalization by decimal scaling
#use log in numpy library
k = npy.ceil(npy.log10(data.abs()).max()) #take the integer ceil of k
data4 = data/10**k
print(data4)

#Data Discretization
#(1)
data5 = data[u"price"].copy() #"u" fix data without changing, copy()is a deep copy
data6 = data5.T
data7 = data6.values # covert to array
k = 3
c1 = pda.cut(data7, k, labels = ["cheap","middle","expensive"])
print(c1)
c2 = pda.cut(data7, [0,50,100,300,500,2000,data7.max()], labels = ["very cheap","cheap","middle","a little expensive","expensive", "very expensive"])
print(c2)


# add new item in column
#conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test", charset = "utf8")
sql1 = "select * from myhexun"
data8 = pda.read_sql(sql1, conn)
#print(data8)
comment_hits_rate = data8[u"comment"]/data8[u"hits"]
data8[u"CH_rate"] = comment_hits_rate
print(data8)
file = "C:/Users/Administrator/Desktop/hexun(ch_rate added).xls"
data8.to_excel(file, index = False)
