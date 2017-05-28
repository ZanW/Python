import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

web_stats = {"Day":[1,2,3,4,5,6], "Visitors":[23,43,454,56,67,45], "Bounce_Rate":[65,74,65,46,23,56]}

df = pd.DataFrame(web_stats)

print(df)
print(df.head())
print(df.tail())
print(df.tail(2))

print(df.set_index("Day"))

print(df.Visitors)
print(df.Bounce_Rate)
print(df[["Visitors"]])

print(df.Visitors.tolist())

import numpy as np
print(np.array(df[["Day", "Bounce_Rate"]]))
