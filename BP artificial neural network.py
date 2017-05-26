#BP artificial neural network
#1. load data
#2. keras.models Sequential / keras.layers.core Dense or Activation
#3. Sequential (build model)
#4. Dense (build layers)
#5. Activation (activate functions)
#6. compile
#7. fit (training data)
#8. verification

#1
import pandas as pda
fname = "C:/Users/Administrator/Desktop/data1/lesson2.csv"
dataf = pda.read_csv(fname)
x = dataf.iloc[:, 1:5].as_matrix()
y = dataf.iloc[:, 5].as_matrix()
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

from keras.models import Sequential
from keras.layers.core import Dense, Activation
model = Sequential()
#build input layer
model.add(Dense(10, input_dim = len(x2[0]))) # 10 is input points, dim is number of feature 
model.add(Activation("relu")) #activating function: relu
#bulid output layer
model.add(Dense(1, input_dim = 1))
model.add(Activation("sigmoid"))#sigmoid is specially for binary 
#compile
model.compile(loss = "binary_crossentropy", optimizer = "adam", class_model = "binary")
#training
model.fit(x2, y2, nb_epoch =20, batch_size = 100)#nb_epoch: num of training
#predict classification
rst = model.predict_classes(x).reshape(len(x))
for i in range(0, len(x2)):
    z = 0
    if(rst[i] != y[i]):
        z+=1
print(1 - z/len(x2))
