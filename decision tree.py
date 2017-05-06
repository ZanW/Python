import pandas as pda
fname = "C:/Users/Administrator/Desktop/data/lesson2.csv"
dataf = pda.read_csv(fname)
dataf[dataf == "高"]= 1
