import pandas

data = pandas.read_csv("squirrel_data.csv")
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel)
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

data_frame = pandas.DataFrame(data_dictionary)
data_frame.to_csv("squirrel_count.csv")
