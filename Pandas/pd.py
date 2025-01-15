# import pandas as pd
# import numpy as np

# dataFrame = [
#     ['Alice', 25, 'Paris'],
#     ['Bob', 30, 'Lyon'],
#     ['Charlie', 35, 'Marseille']
# ]
# df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

# dataFrame = {
#     'Name':['Alice', 'Charlie', 'Bob'],
#     'Age':[25, 30, 35],
#     'City':['Paris', 'Lyon', 'Marseille']
# }
# df = pd.DataFrame(dataFrame)
# print(df)

# dataSeries = [10, 20, 30, 40]
# ds = pd.Series(dataSeries)
# print(ds)

# names = ['first', 'second', 'third', 'fourth']
# dataSeries = [10, 20, 30, 40]
# ds = pd.Series(dataSeries, index=names)
# print(ds)

# names = ['first', 'second', 'third', 'fourth']
# dataSeries = [[10, 20, 30, 40],[10, 20, 30, 40],[10, 20, 30, 40],[10, 20, 30, 40]]
# ds = pd.Series(dataSeries, index=names)
# print(ds)
# print(ds['first'])

# dsf = pd.Series(dataFrame)
# print(dsf)
# print(dsf['Name'])

# data = pd.read_csv("salary.csv")
# print(data)
# print(data.head(3))
# print(data.info())
# print(data.describe().round())
# print(data.isna()) #isna return true if the data is missing
# print(data.isna().sum())
# print(data.mean()) # calcue average
# print(data.fillna(data.mean())) # fillna() replace the NaN with something
# print(data.dropna()) #dropna remove the row wish have the missing data
# print(data)
# for x in data.index: #check the data if > 50000
#     if (data.loc[x,"Salary"] > 50000):
#         data.loc[x, "Salary"] = 50000
# print(data)

# dataNew = data.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
# print(dataNew)

# data = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6]
# })

# # Apply a lambda function to each column (sum of each column)
# result = data.apply(lambda x: x.sum())
# print(result)

# # DataFrames to concatenate
# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# # Concatenate vertically (along rows)
# result = pd.concat([df1, df2], axis=0)

# print(result)