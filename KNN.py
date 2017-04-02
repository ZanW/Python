from numpy import *
# from numpy import *: every method under numpy can be used directly without introduce package name numpy
# import numpy: methods under package needs package name introduced ahead of it
import operator

#extend array row: tile(name, number(times original column numbers))
#extend column row: tile(name, (newRowNum, number(times original column numbers)))

def knn(k, testdata, traindata, labels):
    traindatasize = traindata.shape[0] #index [0] represents row number, [1] indicates column number
    s = tile(testdata,(traindatasize, 1)) # the dimentions of testdata and traindata may be different, to calculate, they must accord with each other
    diff = s - traindata
    sqdiff = diff**2
    sumsqdiff = sqdiff.sum(axis = 1) # axis = 1: sum each column values in one row; axis = 0: sum all colume values in all rows   distance = sumsqdiff**0.5
    sortdistance = distance.argsort() #sort values in ascending order, return indices from least value, i.e. the first value in array
    count = {}
    for i in range(0, k):
        vote = labels[sortdistance[i]]
        count[vote] = count.get(vote, 0) + 1 # count.get(index) = count[index], but count.get(index, value), preassign value to index, but final assignment, needs count[index] = to set
        # sort count[vote] by frequency values in increasing order
    sortcount= sorted(count.items(), key = operator.itemgetter(1), reverse = True) # operator.itemgetter(1): sort the dictionary item based on value; # operator.itemgetter(0): sort the dictionary item based on key; reverse = True: in descending order
    return sortcount[0][0]
