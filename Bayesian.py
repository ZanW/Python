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
            labelRatio[thislabel] = labels.count(thislabel)/labelsum # the ratio of current label to total of all labels
            for vector, label in zip(dataSet, labels): #This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
                if(label not in vectorRatio): #The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False otherwise
                    self.vectorRatio[label] = []
                self.vectorRatio[label].append(vector)
            print("training ends")
            return self
        def btest(self, TestData, labelsSet):
            if(self.length == -1):
                raise ValueError("training is not done, please do training first")
            # calculate the raito that testdata under each label respectively
