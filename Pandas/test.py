import pandas as pd
import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8]
# s = pd.Series(data)
s = pd.Series(data, index = ["a", "b", "c", "d", "e", "f", "g", "h"])

# print(s)
# print(type(s))

# # Every pandas series has flexible indexing
# # Arithmetic opretaions can be performed on the data series

print(s.iloc[0])

# np.nan is used to simulate missing values
# s1 = pd.Series([1, 2, 3], index = ["a", "b", "c"])
# s2 = pd.Series([4, 5, 6], index = ["a", "b", "c"])
# print(s1 + s2)

# data = [1, 3, 5, np.nan, 6, 8]
# s = pd.Series(data)
# print(s.fillna(0))
# print(s.dropna())

data = {"Name": ["Favour", "Anonymous", "Anybody"],
        "Age": [25, 23, 29],
        "City": ["Port Harcourt", "Somewhere", "Aba"]
        }
df = pd.DataFrame(data)
print(df)