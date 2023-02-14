import pandas as pd

data = pd.read_csv("weather_data.csv")

# print(data['temp'])
# print(data['day'])
# print(data['condition'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data['temp'].mean())
print(data['temp'].max())

# Get data in columns
print(data['condition'])
print(data.condition)

# Get data in row
print(data[data.day == 'Monday'])


monday = data[data.day == 'Monday']
print(monday.condition)
monday_temp = int(monday.temp)
print(monday_temp)

# Create a dataframe from scratch
new_data_dict = {
    "students": ["amy", "james", "angela"],
    "scores": [1, 2, 3]
}

new_data = pd.DataFrame(new_data_dict)
new_data.to_csv("newdataframe.csv", index=False)