
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
#x indicates student serial No., y represent student class
s = npy.arange(0, len(y))
