import pandas as pd

df = pd.read_csv('csv/weather_data1.csv',parse_dates=['day'])
df.set_index('day',inplace=True)
d=df.fillna(0)
newd = df.fillna({
    'temperature':0,
    'windspeed':0,
    'event':'no event'
})
newd2 = df.fillna(method="ffill",limit=1)
print(newd2)
newd3 = df.fillna(method="bfill")
# newd3 = df.fillna(method="bfill",axis="column")
print(newd3)
