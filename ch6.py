"""Work through the Chapter 6 examples."""

import numpy as np
import pandas as pd

college = pd.read_csv('data/college.csv', index_col='INSTNM')
# print(college.dtypes)

cols = ['MD_EARN_WNE_P10', 'GRAD_DEBT_MDN_SUPP']
for col in cols:
    college[col] = pd.to_numeric(college[col], errors='coerce')

# print(college.dtypes.loc[cols])

college_n = college.select_dtypes(include=[np.number])
# print(college_n.head())
criteria = college_n.nunique() == 2
binary_cols = college_n.columns[criteria].tolist()
# print(binary_cols)

college_n2 = college_n.drop(labels=binary_cols, axis='columns')
# print(college_n2.head())
max_cols = college_n2.idxmax()
# print(max_cols)
unique_max_cols = max_cols.unique()

college_n2.loc[unique_max_cols].style.highlight_max()
print(college_n2.loc[unique_max_cols].style.highlight_max())

# columns = college.columns
# print(columns)

# print(columns.values)

# baseball_14 = pd.read_csv('data/baseball14.csv', index_col='playerID')
# baseball_15 = pd.read_csv('data/baseball15.csv', index_col='playerID')
# baseball_16 = pd.read_csv('data/baseball16.csv', index_col='playerID')

# print(baseball_14.head())

# print(baseball_14.index.difference(baseball_15.index))
# print(baseball_14.index.difference(baseball_16.index))

# hits_14 = baseball_14['H']
# hits_15 = baseball_15['H']
# hits_16 = baseball_16['H']

# hits_total = hits_14.add(hits_15, fill_value=0).add(hits_16, fill_value=0)

# print(hits_total.head())

# employee = pd.read_csv('data/employee.csv')
# dept_sal = employee[['DEPARTMENT', 'BASE_SALARY']]

# dept_sal = dept_sal.sort_values(['DEPARTMENT', 'BASE_SALARY'],
#                                 ascending=[True, False])

# max_dept_sal = dept_sal.drop_duplicates(subset='DEPARTMENT')
# print(max_dept_sal.head())

# max_dept_sal = max_dept_sal.set_index('DEPARTMENT')
# employee = employee.set_index('DEPARTMENT')

# employee['MAX_DEPT_SALARY'] = max_dept_sal['BASE_SALARY']
# print(employee.head())
# print(employee.query('BASE_SALARY > MAX_DEPT_SALARY'))
