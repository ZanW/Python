# read data from hexun.com and make visual analysis

import numpy as npy
import matplotlib.pylab as mpyl
import pandas as pda

data = pda.read_csv("D:/Personal\Study/IT Study/data science/hellobi/Python数据分析与挖掘实战\第5周/hexun.csv")
data2 = data.T
y1 = data2.values[3]
x1 = data2.values[4]
'''
mpyl.plot(x1, y1)
mpyl.show()
'''
x2=data2.values[0]
y2=data2.values[4]
mpyl.plot(x2,y2)
mpyl.show()
