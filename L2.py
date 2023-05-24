import pandas as pd
df = pd.read_csv('csv/weather_data.csv')
print(df)
rows, columns = df.shape
print("rows :", rows);
print("columns :", columns)
# print(df.head()) # print few first row
# print(df.head(2)) # print first 2 row
# print(df.tail()) # print few last row
# print(df.tail(2)) # print last 2 row
# print(df[2:5]) # print df from 2 index to 5

print(df.columns)
# print(df.day)
# print(df['temperature'])
# print(df[['day','temperature']])
# print(df['temperature'].min())
# print(df['temperature'].std()) # standard deviation

df.set_index('day',inplace=True)
print(df)
print()
print("information of 1 January 2017")
print(df.loc['1/1/2017'])

df.reset_index(inplace=True)
print(df)