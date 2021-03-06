import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")


# api_key = open

##df = quandl.get("ZILL/N00548_LPC")
##print(df.head())
##
##fiddy_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
##print(fiddy_states[0])

codeNum = ["12265", "08729", "00548"]
main_df = pd.DataFrame()

for code in codeNum:
    df = quandl.get("ZILL/N" +code+"_LPC")
    
    if main_df.empty == True:
        #df.set_index("Date", inplace = True)
        main_df = df
    else:
        #df.set_index("Date", inplace = True)
        #main_df = pd.merge(main_df, df, on = "Date", how = "outer")
        main_df = pd.concat([main_df, df])

main_df.plot()
plt.show()

main_df["Value"] = (main_df["Value"] - main_df["Value"][0])/main_df["Value"][0]*100


pickle_out = open("C:\\Users\\Asymmetry\\Desktop\\fiddy_states1.pickle", "wb")
pickle.dump(main_df, pickle_out)
pickle_out.close()

pickle_in = open("C:\\Users\\Asymmetry\\Desktop\\fiddy_states1.pickle", "rb")
HPI_data = pickle.load(pickle_in)
print(HPI_data)

HPI_data.to_pickle("C:\\Users\\Asymmetry\\Desktop\\pickle.pickle")

##HPI_data.plot()
##plt.legend().remove()
##plt.show() 
