import pandas as pd

data_set = {"age": ["6", "13", "7", "9"], "frequency": [3, 7, 8, 3]}

table = pd.DataFrame(data_set)  # creates a table with the values :o

list = [1, 7, 2]

series = pd.Series(list)  # presents the list as a column

labels = pd.Series(list, index=["x", "y", "z"])  # changes the id

key_object = {
    "key1": 1,
    "key2": 2,
    "key3": 3,
}  # basically a dictionary but with a series

dictionary = pd.Series(key_object)

series2 = {
    "series1": [1, 2, 3, 4],
    "series2": [60, 50, 40, 60],
}  # multi dimensional tables (data sets)

DataFrame = pd.DataFrame(series2)

print(DataFrame)
