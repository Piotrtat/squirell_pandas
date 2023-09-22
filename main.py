import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

count_gray = len(data[data["Primary Fur Color"] == "Gray"])
count_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_black = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "squirrel_colors": ["Gray", "Cinnamon", "Black"],
    "squirrel_number": [count_gray, count_cinnamon, count_black]
}

df = pandas.DataFrame(squirrel_dict)
print(df)
df.to_csv("squirrel_count")