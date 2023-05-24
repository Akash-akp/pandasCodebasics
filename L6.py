import pandas as pd
import numpy as np

df = pd.read_csv('csv/weather_data2.csv')
print(df)
df1=df.replace([-99999,'0'],np.nan);
print(df1)
df2=df.replace({
    'temperature':-99999,
    'windspeed':-99999,
    'event':'0'
},np.nan);
print(df2)
df3 = df.replace({
    -99999:np.nan,
    '0':'Snowy'
})
print(df3)

d = pd.DataFrame({
    'temperature': ['35F',34,28,39,'40C'],
    'windspeed' : ['5mph',7,'8mph',5,9],
    'event' : ['Snowy','Rainy','Sunny','Normal','Rainy']
})
print(d)
d1 = d.replace({
    'temperature': '[A-Za-z]',
    'windspeed' : '[A-Za-z]'
},"",regex=True)
print(d1)


d2 = pd.DataFrame({
    'Score' : ['Outstanding','Excellent','Poor','Good','Outstanding'],
    'Student' : ['a','b','c','d','e']
})
print(d2)

d3 = d2.replace(['Outstanding','Excellent','Good','Poor'],[4,3,2,1])
print(d3)
