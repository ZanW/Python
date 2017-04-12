from numpy import *

# from numpy import *: every method under numpy can be used directly without introduce package name numpy
# import numpy: methods under package needs package name introduced ahead of it
import operator

#extend array column: tile(name, number(times original column numbers))
#extend array row: tile(name, (newRowNum, newColNumber(times original column numbers))) (note that newRowNum >1, increases array's dimension)

def knn(k, testdata, traindata, labels):
    traindatasize = traindata.shape[0] #index [0] represents row number, [1] indicates column number
    s = tile(testdata,(traindatasize, 1)) # the dimentions of testdata and traindata may be different, to calculate, they must accord with each other
    diff = s - traindata
    sqdiff = diff**2
    sumsqdiff = sqdiff.sum(axis = 1) # axis = 1: sum each column values in one row; axis = 0: sum all colume values in all rows   distance = sumsqdiff**0.5
    distance = sumsqdiff**0.5
    sortdistance = distance.argsort() #sort values in ascending order, return indices from least value, i.e. the first value in array
    count = {}
    for i in range(0, k):
        vote = labels[sortdistance[i]]
        count[vote] = count.get(vote, 0) + 1 # count.get(index) = count[index], however, count.get(index, value), preassign value to index, but final assignment, needs count[index] = to set
        # sort count[vote] by frequency values in increasing order
    sortcount= sorted(count.items(), key = operator.itemgetter(1), reverse = True) # operator.itemgetter(1): sort the dictionary item based on value;
                                                                                                                       # operator.itemgetter(0): sort the dictionary item based on key; reverse = True: in descending order
    return sortcount[0][0]

# pillow : deal with image, abbreviate as PIL when use
# first convert all image into size 32*32, then make txt file
from PIL import Image
im = Image.open("C:/Users/Administrator/Desktop/testimage.jpg")
fh = open("C:/Users/Administrator/Desktop/testimage.txt","a")
# im.save("C:/Users/Administrator/Desktop/502691801970044230.bmp")
height = im.size[0]
width = im.size[1]
#k = im.getpixel((1,9))
#print(k)
for i in range(height):
    for j in range(width):
        cl = im.getpixel((i, j))
        claAll = cl[0] + cl[1] +cl[2]
        if(claAll == 0): #color black
            fh.write("1")
        else:
            fh.write("0")
    fh.write("\n")
fh.close()

#load data
def datatoarray(fname):
    arr = []
    fh = open(fname)
    for i in range(0, 32):
        thisline = fh.readline()
        for j in range(0, 32):
            arr.append(int(thisline[j]))
    return arr
arr1 = datatoarray("C:/Users/Administrator/Desktop/0_30.txt")
#build a method to get the prefix of the file name of training data
def seplabel(fname):
    filestr = fname.split(".")[0]
    label = int(filestr.split("_")[0])
    return label
#build training data
#listdir: list all files under one folder
from os import listdir
def traindata():
    labels = []
    trainfile = listdir("C:/Users/Administrator/Desktop/data1/traindata")
    num = len(trainfile)
    #one list store all train data, each row store one file of train data, so the list should have 1024(32*32 values in one file of training data) columns
    #use zeros() creates a list with 0 values(belongs to numpy package)
    trainarr = zeros((num, 1024))
    for i in range(0, num):
        thisFileName = trainfile[i]
        thislabel = seplabel(thisFileName)
        labels.append(thislabel)
        trainarr[i,:] = datatoarray("C:/Users/Administrator/Desktop/data1/traindata/" + thisFileName)
    return trainarr, labels
#identify test data via KNN
def datatest():
    trainarr, labels = traindata()
    testlist = listdir("C:/Users/Administrator/Desktop/data1/testdata")
    tnum = len(testlist)
    print(tnum)
    for i in range(0,tnum):
        thisTestFile = testlist[i]
        testarr = datatoarray("C:/Users/Administrator/Desktop/data1/testdata/"+thisTestFile)
        #print(testarr)
        rknn = knn(3, testarr, trainarr, labels)
        print(rknn)

datatest()
