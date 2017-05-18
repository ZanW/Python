#application of Bayes

class Bayes:
    def __init__(self):
        self.length = -1 # -1 indicates data has not trained yet
        self.labelRatio = dict()
        self.vectorRatio = dict()
    def fit(self, dataSet:list, labels:list): #list is type
        if(len(dataSet) != len(labels)):
            raise ValueError("test dataset and labels have different length") #the raise statement allows the programmer to force a specified exception to occur
        self.length = len(dataSet[0]) # the length of feature data in test dataset
        labelsum = len(labels) # total number of labels
        norlabels = set(labels) # unduplicated labels
        for item in norlabels:
            thislabel = item
            self.labelRatio[thislabel] = labels.count(thislabel)/labelsum # the ratio of current label to total of all labels
            for vector, label in zip(dataSet, labels): #This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
                if(label not in self.vectorRatio): #The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False otherwise
                    self.vectorRatio[label] = []
                self.vectorRatio[label].append(vector)
            print("training ends")
            return self
        def btest(self, TestData, labelsSet):
            if(self.length == -1):
                raise ValueError("training is not done, please do training first")
            # calculate the raito that testdata under each label respectively


from numpy import *

import operator

#load data
def datatoarray(fname):
    arr = []
    fh = open(fname)
    for i in range(0, 32):
        thisline = fh.readline()
        for j in range(0, 32):
            arr.append(int(thisline[j]))
    return arr
#arr1 = datatoarray("C:/Users/Administrator/Desktop/8.txt")
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

bys = Bayes()
#train data
train_data, labels = traindata()
bys.fit(train_data, labels)
#test
