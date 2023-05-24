import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('csv/weather_by_cities.csv')
g = df.groupby('city')

# for city,city_df in g:
#     print(city)
#     print(city_df)

# print(g.get_group('mumbai'))
# print(g.max())
# print(g.min())
# print(g.mean(['temperature']))

# print(g.describe())

print(df)

x1 =g.get_group('mumbai').temperature.values.reshape(-1,1)
x2 =g.get_group('mumbai').windspeed.values.reshape(-1,1)
y =g.get_group('mumbai').day.values
plt.plot(y,x1,color='red')
plt.plot(y,x2,color='blue')
plt.show()

# print(df.set_index(['city','temperature']))
