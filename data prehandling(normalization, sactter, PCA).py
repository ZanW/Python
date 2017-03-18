# Principle Component Analysis for Jindong
import pandas as pda
import pymysql
import numpy as npy
import matplotlib.pylab as mpl

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test", charset = "utf8")
sql = "select * from jd"
data = pda.read_sql(sql, conn)
#convert string to number
#file = "C:/Users/Administrator/Desktop/jd.xls"
#data.to_excel(file, index = False)

data1 = pda.read_excel("C:/Users/Administrator/Desktop/jd.xls")
print(data1.describe())

for i in range(len(data1["price"])):
    if data1["price"][i] == 0:
        data1["price"][i] = 767

#convert dataframe to arry
data2 = data1.T
price = data2.values[3]
rate = data2.values[4]
mpl.plot(price, rate, "o")
mpl.show()

# if price greater than 3900, comments greater than 95, considered as abnormal values
for j in range(len(price)):
    if price[j] > 3900:
        price[j] = 3900
    if rate[j] > 95:
        rate[j] = 95

# plot need array not dataframe
mpl.plot(price, rate, "o")
mpl.show()

# step analysis
price_range = (price.max()- price.min())/12
rate_range = (rate.max()-rate.min())/12

pricesty = npy.arange(price.min(),price.max(),price_range)
mpl.hist(price, pricesty)
mpl.show()

ratesty = npy.arange(rate.min(),rate.max(), rate_range)
mpl.hist(rate, ratesty)
mpl.show()

# Normalize Data
# choose price and rate, exclude title, link typed string
sql = "select price,rate from jd"
dat = pda.read_sql(sql, conn)

file = "C:/Users/Administrator/Desktop/jd(price&rate).xls"
dat.to_excel(file, index = False)
dat1 = pda.read_excel(file)

#(1)min-max normalization(use dataframework directly)
dat2 = (dat1-dat1.min())/(dat1.max()-dat1.min())
