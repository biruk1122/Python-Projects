import pandas
data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

# Get Data In Columns
print(data["Condition"])
print(data.Condition)

# Get Data In Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create A Dataframe Scratch
data_dict = {
    "Names": ["Biruk", "Yared", "Jhon"],
    "Scores": [89, 90, 78]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("pandas_file")
