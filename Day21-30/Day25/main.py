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

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data) # this is nicely formatted
# to get hold of all values in temp column
print(data["temp"])