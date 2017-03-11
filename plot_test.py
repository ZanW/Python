import matplotlib.pylab as pyl
import numpy as npy
x = [1,2,3,4,8]
y = [5,7,2,1,5]
#pyl.plot(x, y)
#pyl.show()
#pyl.plot(x, y, "o")
#pyl.show()
'''
pyl.plot(x, y)
pyl.title("show")
pyl.xlabel("ages")
pyl.ylabel("temp")
pyl.xlim(0,10)
pyl.ylim(0,8)
pyl.show()
'''
'''
import numpy as npy
data = npy.random.random_integers(1, 20, 10)
print(data)
data2 = npy.random.normal(5, 2, 10)
print(data2)
'''
'''
data3 = npy.random.normal(10, 1, 10000)
data4 = npy.random.random_integers(1, 25, 1000)
sty = npy.arange(1, 30, 2)
pyl.hist(data4, sty)
pyl.show()
'''

pyl.subplot(2,2,1)
x1 = [1,2,3,4,5]
y1 = [5,2,5,6,7]
pyl.plot(x1,y1)

pyl.subplot(2,2,2)
x2 = [3,3,4,6,7]
y2 = [2,4,6,2,5]
pyl.plot(x2,y2)

pyl.subplot(2,1,2)
x3 = [3,4,6,8,5,7]
y3 = [3,5,2,7,7,4]
pyl.plot(x3,y3)

pyl.show()
