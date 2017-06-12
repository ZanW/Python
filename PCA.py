#principle component analysis
#http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
from sklearn.decomposition import PCA
import pymysql
import pandas as pda
import numpy as npy

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test", charset = "utf8")
sql = "select hits,comment from myhexun"
data = pda.read_sql(sql, conn)
#print(data.describe())
ch = data[u"comment"]/data[u"hits"]
data[u"comment_hits_rate"] = ch 
#print(data)

pca1 = PCA()
pca1.fit(data)#Fit the model with "data"
tz1 = pca1.components_#Principal axes in feature space, representing the directions of maximum variance in the data. 
print("get principle axes: ")
print(tz1)
#each principle component explains the overall variability
ratio = pca1.explained_variance_ratio_
print("the radio is:")
print(ratio)

# dimensionality reduction
pca2 = PCA(2)
pca2.fit(data)
reduction = pca2.transform(data)#Apply dimensionality reduction to "data"
print("the reduction to 2 dimension is:")
print(reduction)
tran_inverse = pca2.inverse_transform(reduction)
print("do inversion to data: ")
print(tran_inverse)




