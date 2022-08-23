# with open("weather_data.csv") as f:
#     data = f.readlines()
#     print(data)
# Reading each line of tabular data in this way is cumbersome and requires a lot of clean up

# Using inbuilt csv module
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     # above creates a csv reader object
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Still to much effort to just read a column
# This is where pandas is super helpful

#import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data) # this is nicely formatted
# to get hold of all values in temp column
# print(data["temp"])

# check type of data
# print(type(data)) # this is a dataframe object

# check data type of a single column
# print(type(data["temp"])) # this is a series (equivalent to a list)

# converting data frame to dictionary
# data_dict = data.to_dict()
# print(data_dict)
# each column name is the key and values are again indexed based on numbers

# can convert each individual series into list
# temp_list = data["temp"].to_list()
# print(temp_list)
# print average temp
# print(sum(temp_list)/len(temp_list))

# can do the same average by calling methods on the series
# print(data["temp"].mean())

# get max temp value using series methods
# print(data["temp"].max())

# Another way to access column data
# print(data.condition) # same as data["condition"]

# Getting data in rows
# Get data for the row where day is Monday
# print(data[data["day"] == "Monday"])

# print row of data where temp is max
# print(data[data["temp"] == data["temp"].max()])

# Convert Monday's temp from c to f
# get the whole Moday row
# monday_data = data[data["day"] == "Monday"]
# # getting specific row value within 1 row is same a overall dict
# monday_temp = monday_data["temp"]
# monday_temp_f = int(monday_temp) * 1.8 + 32
# print(monday_temp_f)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Souvik", "Sayali", "Ajinkya"],
#     "scores": [56, 76, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

################################################
# SQUIRREL DATA ANALYSIS
################################################

# building dict for saving format
import pandas

squirrel_count = {
    "Fur Color": [],
    "Count": []
}

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
squirrel_count["Fur Color"].append("grey")
squirrel_count["Count"].append(grey_count)

black_count = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
squirrel_count["Fur Color"].append("black")
squirrel_count["Count"].append(black_count)

red_count = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
squirrel_count["Fur Color"].append("red")
squirrel_count["Count"].append(red_count)

new_data = pandas.DataFrame(squirrel_count)
new_data.to_csv("squirrel_data.csv")
