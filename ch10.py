"""Slog through Chapter 10 with some exercises."""

import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set()

# date = datetime.date(year=2013, month=6, day=7)
# time = datetime.time(hour=12, minute=30, second=19, microsecond=463198)
# dt = datetime.datetime(year=2013, month=6, day=7, hour=12, minute=30,
#                        second=19, microsecond=463198)

# print("date is", date)
# print("time is", time)
# print("datetime is", dt)

# td = datetime.timedelta(weeks=2, days=5, hours=10, minutes=20, seconds=6.73,
#                         milliseconds=99, microseconds=8)
# print(td)

# print("new date is", date + td)
# print("new datetime is", dt + td)

crime_sort = pd.read_hdf('data/crime.h5', 'crime').set_index(
    'REPORTED_DATE').sort_index()

# crime = pd.read_hdf('data/crime.h5', 'crime')
# print(crime.dtypes)

# print(crime_sort.index.weekday_name.value_counts())

# crime_gb = crime_sort.groupby(lambda x: x.weekday_name)['IS_CRIME',
#                                                         'IS_TRAFFIC'].sum()
# print(crime_gb)

# crime = crime.set_index('REPORTED_DATE')
# print(crime.head())

# print(crime.loc['2016-05-12 16:45:00'])

# print(crime.loc['2016-05-12'])

# print(type(crime.index))

# early = crime.between_time('2:00', '5:00', include_end=False)
# print(early.head(12))

# specific = crime.at_time('5:47')
# print(specific.head())

# crime_sort = crime.sort_index()
# crime_six = crime_sort.first(pd.offsets.MonthBegin(6, normalize=True))
# crime_six = crime_sort.first(pd.offsets.MonthEnd(6))

# print(crime_six.head())
# print(crime_six.tail())
# print(len(crime_six))
# print(len(crime))

# weekly_crimes = crime.resample('W').size()
# print(weekly_crimes.head())

# weekly_crimes_gby = crime.groupby(pd.Grouper(freq='W')).size()
# print(weekly_crimes_gby.head())

# crime_quarterly = crime.resample('QS')['IS_CRIME', 'IS_TRAFFIC'].sum()
# print(crime_quarterly.head())

# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
#         'Sunday']
# wd_counts = crime['REPORTED_DATE'].dt.weekday_name.value_counts()
# print(wd_counts)

# weekday = crime['REPORTED_DATE'].dt.weekday_name
# year = crime['REPORTED_DATE'].dt.year

# crime_wd_y = crime.groupby([year, weekday]).size()
# print(crime_wd_y.head(10))

# crime_table = crime_wd_y.rename_axis(['Year', 'Weekday']).unstack('Weekday')
# print(crime_table)

# criteria = crime['REPORTED_DATE'].dt.year == 2017
# print(crime.loc[criteria, 'REPORTED_DATE'].dt.dayofyear.max())

# crime_table.loc[2017] = crime_table.loc[2017].div(.748).astype('int')
# crime_table = crime_table.reindex(columns=days)
# print(crime_table)

# denver_pop = pd.read_csv('data/denver_pop.csv', index_col='Year')
# print(denver_pop)

# den100k = denver_pop.div(100000).squeeze()
# crime_table2 = crime_table.div(den100k, axis='index').astype('int')
# print(crime_table2)

# sns_plot = sns.heatmap(crime_table2)
# fig = sns_plot.get_figure()
# fig.savefig('output.png')

employee = pd.read_csv('data/employee.csv',
                       parse_dates=['JOB_DATE', 'HIRE_DATE'],
                       index_col='HIRE_DATE')

# print(employee.head())

emp_gb = employee.groupby('GENDER')['BASE_SALARY'].mean().round(-2)
# print(emp_gb)

sal_hire = employee.resample('10AS')['BASE_SALARY'].mean().round(-2)
# print(sal_hire)

gen_hire = employee.groupby('GENDER').resample('5AS')[
    'BASE_SALARY'].mean().round(-2)
# print(gen_hire)

sal_avg = gen_hire.unstack('GENDER')
# print(sal_avg)

sal_avg2 = employee.groupby(
    ['GENDER', pd.Grouper(freq='10AS')])['BASE_SALARY'].mean().round(-2)
# print(sal_avg2)

sal_avg2_u = sal_avg2.unstack('GENDER')
# print(sal_avg2_u)

last_date = crime_sort.index.max()
print(last_date)

crime_sort = crime_sort[:'2017-8']
print(crime_sort.index.max())

all_data = crime_sort.groupby(
    [pd.Grouper(freq='M'), 'OFFENSE_CATEGORY_ID']).size()
print(all_data.head())

all_data = all_data.sort_values().reset_index(name='Total')
print(all_data.head())

goal = all_data[all_data['REPORTED_DATE'] == '2017-8-31'].reset_index(drop=True)
goal['Total_Goal'] = goal['Total'].mul(.8).astype('int')
print(goal.head())

last_time = pd.merge_asof(goal, all_data, left_on='Total_Goal',
                          right_on='Total', by='OFFENSE_CATEGORY_ID',
                          suffixes=('_Current', '_Last'))
print(last_time)
