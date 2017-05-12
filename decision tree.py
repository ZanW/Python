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
xf = pda.DataFrame(x)
yf = pda.DataFrame(y)
x2 = xf.as_matrix().astype(int)
y2 = yf.as_matrix().astype(int)

#build decision tree
from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC(criterion = "entropy")
dtc.fit(x2, y2)

#predict sales volume
import numpy as npy
x3 = npy.array([[1, -1, -1, 1], [1, 1, 1, 1], [-1, 1, -1, 1]])
result = dtc.predict(x3)
print(result)

# visualize decision tree
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open("C:/Users/Administrator/Desktop/dtc.dot", "w") as file:
    export_graphviz(dtc, feature_names = ["Practice", "Course Num", "Sales Promotion", "datum"], out_file = file)
