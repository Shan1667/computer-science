import pandas as pd
#when we wish to use pandas we will type pd instead of pandas
df = pd.read_csv("unclean_data 1.csv",encoding="ANSI")
#this will give an erorr message
#pandas expects to get a utf-8 encoded file by default
#overwrite the default encoding of utf-8
#df = pd.read_csv("unclean_data.csv",encoding="ANSI")
#print(df.columns)
#print(df.isnull())
pd.set_option("display.max_columns", None)
#print(df.isnull())
#print(df.isnull().any())
#print(df.isnull().sum())
#print(df.isnull().sum().sum())
#print(df.head(5))
#df = df.fillna(0)
#print(df.head(5))
#print(df.head(5))
new_values = {"duration": 100, "FACENUMBER_IN_POSTER": -999}
df=df.fillna(value=new_values)
print(df.head(5))
#df.dropna(inplace=True)
#df = df.dropna()
#new_values = {"TIME
#meanoftime = df["TIME"].mean()
#df["TIME"] = df.TIME.fillna(meanoftime)