import pymysql
import numpy as npy
import pandas as pda
import matplotlib.pylab as mpyl

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test", charset = "utf8")
sql = "select * from taob"
data = pda.read_sql(sql, conn)
print(data.describe())

#data["price"][(data["price"]==0)] = None

# set 36 to all price equaling zero
x=0
for j in range(len(data)):
    if (data["price"][j] ==0):
        data["price"][j] = "36"
        x+=1
print(x)

#x axis is price, y axis is comment
data2 = data.T
price = data2.values[2]
comment = data2.values[3]
mpyl.plot(price, comment, "o")
mpyl.show()

#abnormal comments>200000, abnormal price > 2300
line = len(data.values)
col = len(data.values[0])
da = data.values
for i in range(0, line):
    #for j in range(0, col):
        if da[i][2] > 2300:
            print(da[i])
            da[i][2] = 36
        if da[i][3] > 200000:
            print(da[j])
            da[i][3] = 58
print()

print("the second figure is making")           
da2 = da.T
price = da2[2]
comment = da2[3]
mpyl.plot(price, comment, "o")
mpyl.show()
