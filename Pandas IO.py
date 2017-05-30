import pandas as pd

df = pd.read_csv("C:\\Users\\Administrator\\Desktop\\ZILL-Z77006_3B.csv")
print(df.head())

df.set_index("Date", inplace = True)
df.to_csv("C:\\Users\\Administrator\\Desktop\\newcsv2.csv")

df = pd.read_csv("C:\\Users\\Administrator\\Desktop\\newcsv2.csv", index_col = 0)
print(df.head())

df.columns = ["Austin_HPI"]
print(df.head())

df.to_csv("C:\\Users\\Administrator\\Desktop\\newcsv3.csv")
df.to_csv("C:\\Users\\Administrator\\Desktop\\newcsv4.csv", header = False)

df = pd.read_csv("C:\\Users\\Administrator\\Desktop\\newcsv4.csv", names = ["Date", "Austin_HPI"], index_col = 0)
print(df.head())

df.to_html("C:\\Users\\Administrator\\Desktop\\example.html")

df = pd.read_csv("C:\\Users\\Administrator\\Desktop\\newcsv4.csv", names = ["Date","Austin_HPI"])
print(df.head())

df.rename(columns = {"Austin_HPI" : "323wer"}, inplace = True)
print(df.head())

