import matplotlib.pylab as mpyl
import numpy as npy
import pandas as pda
import pymysql

# load data from mysql database, then summary the data
conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test", charset = "utf8")
sql = "select * from myhexun"
data = pda.read_sql(sql, conn)
print(data.describe())
recordsNumOfData = len(data)
print("Total Record Numbers including 0: "+str(recordsNumOfData))
print()

#show scattergraph with x axis as hits and y axis as comment
da = data.T.values # transpose data frame, then value it as array
x_hits = da[3]
y_comment = da[4]
mpyl.plot(x_hits, y_comment, "o")
mpyl.show()

# from the scatter diagram, there is no need to handle abnormal numbles valued 0
# set 772 to all abnormal hits number valued more than 33000
# set 5 to all abnormal comment number valued more than 250

rowNum = len(da)# first dimension of da, i.e. total number of rows
columnNum = len(da[0])
for i in range(0, columnNum):
    if da[3][i] > 33000:
        da[3][i] = 772
    if da[4][i] > 250:
        da[4][i] = 5
        
# disply revied scatter diagram
mpyl.plot(x_hits, y_comment, "o")
mpyl.show()

# disply histogram of hits
hits_max = da[3].max()
hits_min = da[3].min()
hits_gap = hits_max - hits_min
interspace = hits_gap/10
sty = npy.arange(hits_min, hits_max, interspace)
mpyl.hist(da[3], sty)
mpyl.show()

# disply histogram of comment
comment_max = da[4].max()
comment_min = da[4].min()
comment_gap = comment_max - comment_min
interspace = comment_gap/10
sty = npy.arange(comment_min, comment_max, interspace)
mpyl.hist(da[4], sty)
mpyl.show()
