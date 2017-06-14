import pandas as pda
fname = "C:/Users/Administrator/Desktop/data/luqu.xls"
dataf = pda.read_excel(fname)
#DataFrame.as_matrix: Convert the frame to its Numpy-array representation
#DataFrame.iloc: Purely integer-location based indexing for selection by position
x = dataf.iloc[:, 1:4].as_matrix()
y = dataf.iloc[:, 0:1].as_matrix()

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
r1 = RLR()
r1.fit(x, y)
eff = r1.get_support()#find the effective features, remove noneffective ones
#print(dataf.columns[eff])
t = dataf[dataf.columns[r1.get_support()]].as_matrix()
r2 = LR()
r2.fit(t, y)
print("training ends")
print("accuracy: " + str(r2.score(x,y))) #score():Returns the mean accuracy on the given test data and labels
