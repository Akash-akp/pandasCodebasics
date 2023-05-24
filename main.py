import pandas as pd
df = pd.read_csv("Contest-6710.csv")
# df.fillna(0,inplace=True)
print(df['name'][df['coding problem score']==df['coding problem score'].max()])
print(df['coding problem score'].mean())