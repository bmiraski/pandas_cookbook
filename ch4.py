"""Work through Ch. 4 in Pandas Cookbook."""

import numpy as np
import pandas as pd

college = pd.read_csv('data/college.csv', index_col='INSTNM')
# city = college['CITY']

# np.random.seed(1)

# labels = list(np.random.choice(city.index, 4))

# print(labels)
# print(city.head())

# print(city.iloc[[10, 20, 30]])
# print(city.iloc[4:50:10])

# print(city.loc[labels])

print(college.head())
# print(college.iloc[[60, 99, 3]])

# print(college.iloc[:3, :4])

col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1

print(col_start, col_end)

print(college.iloc[:5, col_start:col_end])
