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
print(dat2)
print("******************************************************")
#(2)Z-score Normalizaiton
dat3 = (dat1 - dat1.mean())/dat1.std()
print(dat3)
#(3)decimal 
k = npy.ceil(npy.log10(dat1.abs().max()))
dat4 = dat1/10**k
print(dat4)


# scatter with same width
dat5 = dat1[u"price"].copy()
dat6 = dat5.T
dat7 = dat6.values
k = 3
c = pda.cut(dat7, k, labels=["cheap","decent","expensive"])
print(c)

#attribute generation
dat8 = dat1
dat8["price_rate"] = dat8["price"]/dat8["rate"]
print(dat8)
dat8.to_excel("C:/Users/Administrator/Desktop/jd_attri_gen.xls")

# PCA analysis
from sklearn.decomposition import PCA
da = pda.read_excel("C:/Users/Administrator/Desktop/jd_attri_gen.xls")
pca1 = PCA()
pca1.fit(da)
eigenvector = pca1.components_
print(eigenvector)
print("---------------------eigenvector ratio--------------------")
ratio = pca1.explained_variance_ratio_
print(ratio)
print("-----------------------dimentsion reduction-------------")
pca2 = PCA(2)
pca2.fit(da)
print(pca2.transform(da))
print("-----------------------dimension inversion-----------------")
dimension_reduction = pca2.transform(da)
print(pca2.inverse_transform(dimension_reduction))
