class Bayes:
    def __init__(self):
        self.length = -1 # -1 indicates data has not trained yet
        self.label = dict()
        self.vector = dict()
    def fit(self, dataSet:list, labels:list):
        if(len(dataSet) != len(labels)):
            raise ValueError("test dataset and labels have different length")
        self.length = len(dataSet[0]) # the length of feature data in test dataset
        labelsum = len(labels) # total number of labels
        noReLabels = 
