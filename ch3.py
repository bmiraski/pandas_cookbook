"""Cover Chapter 3 of Pandas Cookbook."""

import numpy as np
import pandas as pd
import pandas_datareader as pdr


def set_trailing_loss(symbol, purchase_date, perc):
    close = pdr.DataReader(symbol, 'yahoo', start=purchase_date)['Close']
    return close.cummax() * perc

# college = pd.read_csv('data/college.csv')

# print(college.head())
# print(college.shape)
# print(college.info())
# print(college.describe(include=[np.number]).T)
# print(college.describe(include=[np.object, pd.Categorical]).T)

# different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']

# col2 = college.loc[:, different_cols]
# print(col2.head())

# print(col2.dtypes)

# print(col2.memory_usage(deep=True))

# col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)

# print(col2.dtypes)

# print(col2.memory_usage(deep=True))

# col2['STABBR'] = col2['STABBR'].astype('category')

# print(col2.dtypes)

# print(col2.memory_usage(deep=True))

# movie = pd.read_csv('data/movie.csv')
# movie2 = movie[['movie_title', 'imdb_score', 'budget']]
# movie2 = movie[['movie_title', 'title_year', 'imdb_score']]

# print(movie2.head())

# print(movie2.sort_values('imdb_score', ascending=False).head(100).sort_values('budget').head())

# movie_smallest_largest = movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')

# print(movie_smallest_largest)

# sort_movie2 = movie2.sort_values(['title_year', 'imdb_score'], ascending=False)

# movie3 = sort_movie2.drop_duplicates(subset='title_year')

# print(movie3)

# print(movie2.nlargest(100, 'imdb_score').head())

# print(movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget').head())

# tsla = pdr.DataReader('tsla', data_source='yahoo', start='2017-1-1')

# print(tsla.head(8))

# tsla_close = tsla['Close']

# tsla_cummax = tsla_close.cummax()
# print(tsla_cummax.head(8))

# tsla_trailing_stop = tsla_cummax * .9
# print(tsla_trailing_stop.head(8))

msft_trailing_stop = set_trailing_loss('msft', '2017-6-1', .85)

print(msft_trailing_stop.head(8))
