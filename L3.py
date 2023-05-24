import pandas as pd

# creating data frame from dictionary
weather_data = {
    'day': [1,2,3,4],
    'temperature':[32,33,37,50]
}
df = pd.DataFrame(weather_data)
print(df)

# creating data frame from xlsx file
# df = pd.read_excel("weather_data.xlsx")
# print(df)

# creating data frame from csv
df = pd.read_csv('csv/weather_data.csv')
print(df)

# creating data frame from tuple
weather_tuple = [
    (1,32),
    (2,33),
    (3,37),
    (4,50)
]
df = pd.DataFrame(weather_tuple,columns=["day","temperature"])
print(df)