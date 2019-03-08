"""Work through Chapter 11 on visualizations."""

import datetime
from matplotlib.cm import Greys
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

# x = [-3, 5, 7]
# y = [10, 2, 5]

# fig, ax = plt.subplots(figsize=(15, 3))
# ax.plot(x, y)
# ax.set_xlim(0, 10)
# ax.set_ylim(-3, 8)
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_title('Line Plot')
# fig.suptitle('Figure Title', size=20, y=1.03)

# fig, ax = plt.subplots(nrows=1, ncols=1)
# fig.set_size_inches(14., 4.)
# fig.set_facecolor('.9')
# ax.set_facecolor('.7')

# spines = ax.spines
# spine_left = spines['left']
# spine_left.set_position(('outward', -100))
# spine_left.set_linewidth(5)

# spine_bottom = spines['bottom']
# spine_bottom.set_visible(False)

# ax.xaxis.grid(True, which='major', linewidth=2, color='black', linestyle='--')
# ax.xaxis.set_ticks([.2, .4, .55, .93])
# ax.xaxis.set_label_text('X Axis', family='Verdana', fontsize=15)

# ax.set_ylabel('Y axis', family='Calibri', fontsize=20)
# ax.set_yticks([.1, .9])
# ax.set_yticklabels(['point 1', 'point 9'], rotation=45)

# movie = pd.read_csv('data/movie.csv')
# med_budget = movie.groupby('title_year')['budget'].median() / 1e6
# med_budget_roll = med_budget.rolling(5, min_periods=1).mean()
# print(med_budget_roll.tail())

# years = med_budget_roll.index.values
# print(years[-5:])
# budget = med_budget_roll.values
# print(budget[-5:])

# fig, ax = plt.subplots(figsize=(14, 4), linewidth=5, edgecolor='.5')
# ax.plot(years, budget, linestyle='--', linewidth=3, color='.2',
#         label='All Movies')
# text_kwargs = dict(fontsize=20, family='cursive')
# ax.set_title('Median Movie Budget', **text_kwargs)
# ax.set_ylabel('Millions of Dollars', **text_kwargs)

# movie_count = movie.groupby('title_year')['budget'].count()
# print(movie_count.tail())

# ct = movie_count.values
# ct_norm = ct / ct.max() * budget.max()

# fifth_year = (years % 5 == 0) & (years >= 1970)
# years_5 = years[fifth_year]
# ct_5 = ct[fifth_year]
# ct_norm_5 = ct_norm[fifth_year]
# ax.bar(years_5, ct_norm_5, 3, facecolor='.5', alpha=.3, label='Movies per Year')
# ax.set_xlim(1968, 2017)
# for x, y, v in zip(years_5, ct_norm_5, ct_5):
#     ax.text(x, y + .5, str(v), ha='center')
# ax.legend()

# top10 = movie.sort_values(
#     'budget', ascending=False).groupby('title_year')['budget'].apply(
#     lambda x: x.iloc[:10].median() / 1e6)
# top10_roll = top10.rolling(5, min_periods=1).mean()
# print(top10_roll.tail())

# plt.show(fig)

# fig2, ax_array = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
# ax1 = ax_array[0]
# ax2 = ax_array[1]

# ax1.plot(years, budget, linestyle='--', linewidth=3, color='.2',
#          label='All Movies')
# ax1.bar(years_5, ct_norm_5, 3, facecolor='.5', alpha=.3,
#         label='Movies per Year')
# ax1.legend(loc='upper left')
# ax1.set_xlim(1968, 2017)
# plt.setp(ax1.get_xticklines(), visible=False)

# for x, y, v in zip(years_5, ct_norm_5, ct_5):
#     ax1.text(x, y + .5, str(v), ha='center')

# ax2.plot(years, top10_roll.values, color='.2', label='Top 10 Movies')
# ax2.legend(loc='upper left')

# fig2.tight_layout()
# fig2.suptitle('Median Movie Budget', y=1.02, **text_kwargs)
# fig2.text(0, .6, 'Millions of Dollars', rotation='vertical',
#           ha='center', **text_kwargs)

# path = os.path.expanduser('~/Desktop/movie_budget.png')
# fig2.savefig(path, bbox_inches='tight')

# plt.show(fig2)

# df = pd.DataFrame(index=['Atiya', 'Abbas', 'Cornelia', 'Stephanie', 'Monte'],
#                   data={'Apples': [20, 10, 40, 20, 50],
#                         'Oranges': [35, 40, 25, 19, 33]})
# print(df)

# color = ['.2', '.7']
# df_plot = df.plot(kind='bar', color=color, figsize=(16, 4))

# plt.show(df_plot)

# df_kde = df.plot(kind='kde', color=color, figsize=(16, 4))
# plt.show(df_kde)

# fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 4))
# fig.suptitle('Two Variable Plots', size=20, y=1.02)
# df.plot(kind='line', color=color, ax=ax1, title='Line Plot')
# df.plot(x='Apples', y='Oranges', kind='scatter', color='.2', ax=ax2,
#         title='Scatterplot')
# df.plot(kind='bar', color=color, ax=ax3, title='Bar plot')

# fig.suptitle('One Variable Plots', size=20, y=1.02)
# df.plot(kind='kde', color=color, ax=ax1, title='KDE plot')
# df.plot(kind='box', ax=ax2, title='Boxplot')
# df.plot(kind='hist', color=color, ax=ax3, title='Histogram')

# flights = pd.read_csv('data/flights.csv')
# flights['DELAYED'] = flights['ARR_DELAY'].ge(15).astype('int')
# cols = ['DIVERTED', 'CANCELLED', 'DELAYED']
# flights['ON_TIME'] = 1 - flights[cols].any(axis=1)
# cols.append('ON_TIME')
# status = flights[cols].sum()

# print(status)

# fig, ax_array = plt.subplots(2, 3, figsize=(18, 8))
# (ax1, ax2, ax3), (ax4, ax5, ax6) = ax_array
# fig.suptitle('2015 US Flights - Univariate Summary', size=20)

# ac = flights['AIRLINE'].value_counts()
# ac.plot(kind='barh', ax=ax1, title='Airline')

# oc = flights['ORG_AIR'].value_counts()
# oc.plot(kind='bar', ax=ax2, rot=0, title='Origin City')

# dc = flights['DEST_AIR'].value_counts().head(10)
# dc.plot(kind='bar', ax=ax3, rot=45, title='Destination City')

# status.plot(kind='bar', ax=ax4, rot=0, log=True, title='Flight Status')
# flights['DIST'].plot(kind='kde', ax=ax5, xlim=(0, 3000), title='Distance KDE')
# flights['ARR_DELAY'].plot(kind='hist', ax=ax6, title='Arrival Delay',
#                           range=(0, 200))

# plt.show(fig)

# hour = flights['SCHED_DEP'] // 100
# minute = flights['SCHED_DEP'] % 100
# df_date = flights[['MONTH', 'DAY']].assign(YEAR=2015, HOUR=hour, MINUTE=minute)

# print(df_date.head())

# flight_dep = pd.to_datetime(df_date)
# print(flight_dep.head())

# flights.index = flight_dep
# fc = flights.resample('W').size()
# fc_plot = fc.plot(figsize=(12, 3), title='Flights per Week', grid=True)

# fc_miss = fc.where(fc > 1000)
# fc_intp = fc_miss.interpolate(limit_direction='both')
# ax = fc_intp.plot(color='black', figsize=(16, 4))
# fc_intp[fc < 500].plot(linewidth=10, grid=True, color='.8', ax=ax)

# ax.annotate(xy=(.8, .55), xytext=(.8, .77), xycoords='axes fraction',
#             s='missing data', ha='center', size=20, arrowprops=dict())
# ax.set_title('Flights per Week (Interpolated Missing Data)')

# flightadd = flights.groupby('DEST_AIR')['DIST'].agg(['mean', 'count']) \
#                    .query('count > 100').sort_values('mean').tail(10) \
#                    .plot(kind='bar', y='mean', rot=0, legend=False,
#                          title='Average Distance per Destination')

# fs = flights.reset_index(drop=True)[['DIST', 'AIR_TIME']] \
#             .query('DIST <= 2000').dropna()
# fs.plot(x='DIST', y='AIR_TIME', kind='scatter', s=1, figsize=(16, 4))
# fs['DIST_GROUP'] = pd.cut(fs['DIST'], bins=range(0, 2001, 250))
# print(fs['DIST_GROUP'].value_counts().sort_index())

# normalize = lambda x: (x - x.mean()) / x.std()
# fs['TIME_SCORE'] = fs.groupby('DIST_GROUP')['AIR_TIME'].transform(normalize)

# print(fs.head())

# ax = fs.boxplot(by='DIST_GROUP', column='TIME_SCORE', figsize=(16, 4))
# ax.set_title('Z-Scores for Distance Groups')
# ax.figure.suptitle('')

# outliers = flights.iloc[fs[abs(fs['TIME_SCORE']) > 6].index]
# outliers = outliers[['AIRLINE', 'ORG_AIR', 'DEST_AIR', 'AIR_TIME', 'DIST',
#                      'ARR_DELAY', 'DIVERTED']]
# outliers['PLOT_NUM'] = range(1, len(outliers) + 1)
# print(outliers)

# ax = fs.plot(x='DIST', y='AIR_TIME', kind='scatter', s=1, figsize=(16, 4),
#              table=outliers)
# outliers.plot(x='DIST', y='AIR_TIME', kind='scatter', s=25, ax=ax, grid=True)
# outs = outliers[['AIR_TIME', 'DIST', 'PLOT_NUM']]
# for t, d, n in outs.itertuples(index=False):
#     ax.text(d + 5, t + 5, str(n))
# plt.setp(ax.get_xticklabels(), y=.1)
# plt.setp(ax.get_xticklines(), visible=False)
# ax.set_xlabel('')
# ax.set_title('Flight Time vs. Distance with Outliers')

# meetup = pd.read_csv('data/meetup_groups.csv', parse_dates=['join_date'],
#                      index_col='join_date')
# print(meetup.head())

# group_count = meetup.groupby([pd.Grouper(freq='W'), 'group']).size()
# print(group_count.head())

# gc2 = group_count.unstack('group', fill_value=0)
# print(gc2.tail())

# group_total = gc2.cumsum()
# print(group_total.tail())

# row_total = group_total.sum(axis='columns')
# group_cum_pct = group_total.div(row_total, axis='index')
# print(group_cum_pct.tail())

# ax = group_cum_pct.plot(kind='area', figsize=(18, 4), cmap='Greys',
#                         xlim=('2013-6', None), ylim=(0, 1), legend=False)
# ax.figure.suptitle('Houston Meetup Groups', size=25)
# ax.set_label('')
# ax.yaxis.tick_right()

# plot_kwargs = dict(xycoords='axes fraction', size=15)
# ax.annotate(xy=(.1, .7), s='R Users', color='w', **plot_kwargs)
# ax.annotate(xy=(.25, .16), s='Data Visualizations', color='k', **plot_kwargs)
# ax.annotate(xy=(.5, .55), s='Energy Data Science', color='k', **plot_kwargs)
# ax.annotate(xy=(.83, .07), s='Data Science', color='k', **plot_kwargs)
# ax.annotate(xy=(.86, .78), s='Machine Learning', color='w', **plot_kwargs)

# employee = pd.read_csv('data/employee.csv',
#                        parse_dates=['HIRE_DATE', 'JOB_DATE'])

# sns.countplot(y='DEPARTMENT', data=employee)
# employee['DEPARTMENT'].value_counts().plot('barh')

# ax = sns.barplot(x='RACE', y='BASE_SALARY', data=employee)
# ax.figure.set_size_inches(16, 4)

# avg_sal = employee.groupby('RACE', sort=False)['BASE_SALARY'].mean()
# ax = avg_sal.plot(kind='bar', rot=0, figsize=(16, 4), width=.8)
# ax.set_xlim(-.5, 5.5)
# ax.set_ylabel('Mean Salary')

# ax = sns.barplot(x='RACE', y='BASE_SALARY', hue='GENDER', data=employee,
#                  palette='Greys')
# ax.figure.set_size_inches(16, 4)

# employee.groupby(['RACE', 'GENDER'], sort=False)['BASE_SALARY'].mean() \
#         .unstack('GENDER').plot(kind='bar', figsize=(16, 4), rot=0,
#                                 width=.8, cmap='Blues')

# ax = sns.boxplot(x='GENDER', y='BASE_SALARY', data=employee, hue='RACE',
#                  palette='Blues')
# ax.figure.set_size_inches(14, 4)

# fig, ax_array = plt.subplots(1, 2, figsize=(14, 4), sharey=True)
# for g, ax in zip(['Female', 'Male'], ax_array):
#     employee.query('GENDER== @g') \
#             .boxplot(by='RACE', column='BASE_SALARY', ax=ax, rot=20)
#     ax.set_title(g + ' Salary')
#     ax.set_xlabel('')
# fig.suptitle('')

# days_hired = pd.to_datetime('12-1-2016') - employee['HIRE_DATE']
# one_year = pd.Timedelta(1, unit='Y')
# employee['YEARS_EXPERIENCE'] = days_hired / one_year
# print(employee[['HIRE_DATE', 'YEARS_EXPERIENCE']].head())

# ax = sns.regplot(x='YEARS_EXPERIENCE', y='BASE_SALARY', data=employee)
# ax.figure.set_size_inches(14, 4)

# g = sns.lmplot('YEARS_EXPERIENCE', 'BASE_SALARY', hue='GENDER', palette='Reds',
#                scatter_kws={'s': 10}, data=employee)
# g.fig.set_size_inches(14, 4)

# grid = sns.lmplot(x='YEARS_EXPERIENCE', y='BASE_SALARY', hue='GENDER',
#                   col='RACE', col_wrap=3, palette='Reds', sharex=False,
#                   line_kws={'linewidth': 5}, data=employee)
# grid.set(ylim=(20000, 120000))

diamonds = pd.read_csv('data/diamonds.csv')
print(diamonds.head())

cut_cats = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_cats = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
clarity_cats = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
diamonds['cut'] = pd.Categorical(diamonds['cut'], categories=cut_cats,
                                 ordered=True)
diamonds['color'] = pd.Categorical(diamonds['color'], categories=color_cats,
                                   ordered=True)
diamonds['clarity'] = pd.Categorical(diamonds['clarity'],
                                     categories=clarity_cats,
                                     ordered=True)

# fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 4))
# sns.barplot(x='color', y='price', ax=ax1, data=diamonds)
# sns.barplot(x='cut', y='price', ax=ax2, data=diamonds)
# sns.barplot(x='clarity', y='price', ax=ax3, data=diamonds)
# fig.suptitle('Price Decreasing with Increasing Quality')

# sns.catplot(x='color', y='price', col='clarity', col_wrap=4, data=diamonds,
#             kind='bar')

# fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 4))
# sns.barplot(x='color', y='carat', ax=ax1, data=diamonds)
# sns.barplot(x='cut', y='carat', ax=ax2, data=diamonds)
# sns.barplot(x='clarity', y='carat', ax=ax3, data=diamonds)
# fig.suptitle('Diamond Weight Decreases With Quality')

diamonds['carat_category'] = pd.qcut(diamonds.carat, 5)
greys = Greys(np.arange(50, 250, 40))
g = sns.catplot(x='clarity', y='price', data=diamonds, hue='carat_category',
                col='color', col_wrap=4, kind='point', palette=greys)
g.fig.suptitle('Diamond price by size, color and clarity', y=1.02, size=20)

plt.show()
