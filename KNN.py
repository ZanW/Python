from numpy import *
# from numpy import *: every method under numpy can be used directly without introduce package name numpy
# import numpy: methods under package needs package name introduced ahead of it
import operator

#extend array row: tile(name, number(times original column numbers))
#extend column row: tile(name, (newRowNum, number(times original column numbers)))

def knn(k, testdata, traindata, label):
    traindatasize = traindata.shape[0] #index [0] represents row number, [1] indicates column number
# the dimentions of testdata and traindata may be different, to calculate, they must accord with each other
