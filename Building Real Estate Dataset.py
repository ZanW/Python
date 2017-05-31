import quandl
import pandas as pd

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

print(main_df.head())
type(main_df)
