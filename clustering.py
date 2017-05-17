
# how to cluster the students admitted
import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
fname = "C:\\Users\\Administrator\\Desktop\\data\\luqu.xls"
dataf = pda.read_excel(fname)
x = dataf.iloc[:, 1:4].as_matrix()
#import sklearn.cluster import Brich
from sklearn.cluster import KMeans
kms = KMeans(n_clusters = 4) #n_jobs means number of threads, max_inter indicates of number for iteration
y = kms.fit_predict(x)
print(y)
#x indicates student serial No., y represents student classification
s = npy.arange(0, len(y))
pyl.plot(s, y, "o")
pyl.show()

#clusterting for goods
import pymysql
conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test")
sql = "select price, comment from taob limit 30"
dataf = pda. read_sql(sql, conn)
x = dataf.iloc[:, :].as_matrix()
kms = KMeans(n_clusters = 3) 
y = kms.fit_predict(x)
print(y)

for i in range(0, len(y)):
    if(y[i] == 0):
        pyl.plot(dataf.iloc[i:i+1, 0:1].as_matrix(), dataf.iloc[i:i+1, 1:2].as_matrix(), "*r")
    if(y[i] == 1):
        pyl.plot(dataf.iloc[i:i+1, 0:1].as_matrix(), dataf.iloc[i:i+1, 1:2].as_matrix(), "sy")
    if(y[i] == 2):
        pyl.plot(dataf.iloc[i:i+1, 0:1].as_matrix(), dataf.iloc[i:i+1, 1:2].as_matrix(), "pk")
pyl.show()

