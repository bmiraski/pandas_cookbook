"""Solve Chapter 5 exercises."""

from bokeh.io import output_file
from bokeh.models import ColumnDataSource
from bokeh.models import Span
from bokeh.palettes import viridis
from bokeh.plotting import figure
from bokeh.plotting import show
from bokeh.transform import factor_cmap
import numpy as np
import pandas as pd

output_file('Chapter5.html')
movie = pd.read_csv('data/movie.csv', index_col='movie_title')

c1 = movie['title_year'] >= 2010
c2 = movie['title_year'].isnull()

criteria = c1 | c2

movie_masked = movie.mask(criteria).dropna(how='all')

print(movie_masked.head())

# print(movie.head())

# fb_likes = movie['actor_1_facebook_likes'].dropna()
# print(fb_likes.head())

# print(fb_likes.describe(percentiles=[.1, .25, .5, .75, .9]).astype(int))

# criteria_high = fb_likes < 20000
# print(criteria_high.mean().round(2))

# print(fb_likes.where(criteria_high, other=20000).head())

# criteria_low = fb_likes > 300
# fb_likes_cap = fb_likes.where(criteria_high, other=20000).where(
#     criteria_low, 300)

# print(fb_likes_cap.head())

# fb_bins = pd.cut(fb_likes_cap, bins=10)
# print(fb_bins.value_counts().sort_index())


# movie_2_hours = movie['duration'] > 120
# print(movie_2_hours.head(10))
# print(movie_2_hours.sum())
# print(movie_2_hours.describe())

# criteria1 = movie.imdb_score > 8
# criteria2 = movie.content_rating == 'PG-13'
# criteria3 = ((movie.title_year < 2000) | (movie.title_year > 2009))

# print(criteria2.head())
# criteria_final = criteria1 & criteria2 & criteria3

# print(criteria_final.head())

# crit_b1 = movie.imdb_score < 5
# crit_b2 = movie.content_rating == 'R'
# crit_b3 = ((movie.title_year >= 2000) | (movie.title_year) <= 2010)

# final_crit_b = crit_b1 & crit_b2 & crit_b3

# final_crit_all = criteria_final | final_crit_b

# print(final_crit_all.head())

# print(movie[final_crit_all].head())

# college = pd.read_csv('data/college.csv')
# college2 = college.set_index('STABBR')
# print(college2.index.is_monotonic)

# college3 = college2.sort_index()
# print(college3.index.is_monotonic)
# print(college3.head())

# college_unique = college.set_index('INSTNM')
# print(college_unique.index.is_unique)

# print(college_unique.loc['Stanford University'])

slb = pd.read_csv('data/slb_stock.csv', index_col='Date', parse_dates=['Date'])

slb_close = slb['Close']
slb_summary = slb_close.describe(percentiles=[.1, .9])

upper_10 = slb_summary.loc['90%']
lower_10 = slb_summary.loc['10%']
criteria = (slb_close > upper_10) | (slb_close < lower_10)
slb_top_bottom_10 = slb_close[criteria]

slb_x = slb_top_bottom_10.index.tolist()
slb_y = slb_top_bottom_10.tolist()

slb_fig = figure(plot_height=800,
                 plot_width=1000,
                 h_symmetry=True,
                 x_axis_label='Date',
                 x_axis_type='datetime',
                 x_axis_location='below',
                 y_axis_label='Closing Price',
                 y_axis_type='linear',
                 y_axis_location='left',
                 y_range=(45, 125),
                 title='SLB',
                 title_location='above',
                 toolbar_location=None)

slb_close_cds = ColumnDataSource(slb)

slb_fig.line('Date', 'Close', color='black', source=slb_close_cds)
slb_fig.circle(slb_x, slb_y, color='red', size=3)

bottom_10 = Span(location=lower_10, dimension='width', line_color='black',
                 line_dash='dashed', line_width=2)
top_10 = Span(location=upper_10, dimension='width', line_color='black',
              line_dash='dashed', line_width=2)

slb_fig.add_layout(bottom_10)
slb_fig.add_layout(top_10)

# show(slb_fig)

# employee = pd.read_csv('data/employee.csv')
# print(employee.DEPARTMENT.value_counts().head())
# print(employee.GENDER.value_counts())
# print(employee.BASE_SALARY.describe().astype(int))

# depts = ['Houston Police Department-HPD', 'Houston Fire Department (HFD)']
# criteria_dept = employee.DEPARTMENT.isin(depts)
# criteria_gender = employee.GENDER == 'Female'
# criteria_sal = employee.BASE_SALARY.between(80000, 120000)

# criteria_final = criteria_dept & criteria_gender & criteria_sal

# select_columns = ['UNIQUE_ID', 'DEPARTMENT', 'GENDER', 'BASE_SALARY']

# qs = """DEPARTMENT in @depts and GENDER == 'Female' and 80000 <= BASE_SALARY <= 120000"""

# emp_filtered = employee.query(qs)
# print(emp_filtered[select_columns].head())

# filt_employee = employee.loc[criteria_final, select_columns]
# print(filt_employee.head())

# amzn = pd.read_csv('data/amzn_stock.csv', index_col='Date',
#                    parse_dates=['Date'])

# amzn_daily_return = amzn.Close.pct_change()
# print(amzn_daily_return.head())

# amzn_daily_return = amzn_daily_return.dropna()

# amzn_bins = pd.cut(amzn_daily_return, 20)
# amzn_bins = amzn_bins.sort_index()
# print(amzn_bins.value_counts())

# mean = amzn_daily_return.mean()
# std = amzn_daily_return.std()

# abs_z_score = amzn_daily_return.sub(mean).abs().div(std)
# pcts = [abs_z_score.lt(i).mean() for i in range(1, 4)]

# print('{:.3f} fall within 1 standard deviation. '
#       '{:.3f} within 2 and {:.3f} within 3'.format(*pcts))
