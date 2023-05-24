import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
print(india_weather)

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
print(us_weather)

df = pd.concat([india_weather,us_weather],ignore_index=True,keys=['india','us'])
print(df)
df = pd.concat([india_weather,us_weather],keys=['india','us'])
print(df)
print(df.loc['us'])

temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])

windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])

print(temperature_df)
print(windspeed_df)

df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)

s = pd.Series(["Humid","Dry","Rain"],name="event")
df = pd.concat([df,s],axis=1)
print(df)
