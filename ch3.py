"""Cover Chapter 3 of Pandas Cookbook."""

import numpy as np
import pandas as pd


college = pd.read_csv('data/college.csv')

# print(college.head())
# print(college.shape)
# print(college.info())
# print(college.describe(include=[np.number]).T)
# print(college.describe(include=[np.object, pd.Categorical]).T)

different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']

col2 = college.loc[:, different_cols]
print(col2.head())

print(col2.dtypes)

print(col2.memory_usage(deep=True))

col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)

print(col2.dtypes)

print(col2.memory_usage(deep=True))

col2['STABBR'] = col2['STABBR'].astype('category')

print(col2.dtypes)

print(col2.memory_usage(deep=True))
