import pandas as pda
fname = "C:/Users/Administrator/Desktop/data/lesson2.csv"
dataf = pda.read_csv(fname)
x = dataf.iloc[:, 1:5].as_matrix()
y = dataf.iloc[:, 5:6].as_matrix()
for i in range(0, len(x)):
    for j in range(0, len(x[i])):
        thisdata = x[i][j]
        if(thisdata == "是" or thisdata == "多" or thisdata == "高"):
            x[i][j] = int(1)
        else:
            x[i][j] = -1
for i in range(0, len(y)):
    thisdata = y[i]
    if(thisdata == "高"):
        y[i] = 1
    else:
        y[i] = -1
# fallible point: train x and y directly here
# right way: convert data type of x and y from object to datframe, then to array designated with type

#build decision tree
from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC(criterion = "entropy")
