import pandas as pd

df = pd.read_csv('csv/stock_data.csv')
print(df)
print()

df = pd.read_csv('csv/stock_data.csv',skiprows=2)
print(df)
print()

df = pd.read_csv('csv/stock_data.csv',header=1)
print(df)
print()

df = pd.read_csv('csv/stock_data.csv',na_values={
    'eps':["not available","n.a."],
    'people':["not available","n.a."],
    'price':["not available","n.a."],
    'revenue':["-1"]
})
print(df)
df.to_csv('new.csv',index=False,columns=['tickers','eps'],header=False)


#excel file

# df = pd.read_excel("stock_data.xlsx",'Sheet1')
# print(df)
# df.to_excel('new.xlsx')
