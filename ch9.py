"""Follow along with Chapter 9 exercises."""

import numpy as np
import pandas as pd

names = pd.read_csv('data/names.csv')

# new_data_list = ['Aria', 1]
# names.loc[4] = new_data_list
# names.loc['five'] = ['Zach', 3]
# names.loc[len(names)] = {'Name': 'Zayd', 'Age': 2}
# names.loc[len(names)] = pd.Series({'Age': 32, 'Name': 'Dean'})


names.index = ['Canada', 'Canada', 'USA', 'USA']
# names = names.append({'Name': 'Aria', 'Age': 1}, ignore_index=True)

# s = pd.Series({'Name': 'Zach', 'Age': 3}, name=len(names))

# names = names.append(s)
s1 = pd.Series({'Name': 'Zach', 'Age': 3}, name=len(names))
s2 = pd.Series({'Name': 'Zayd', 'Age': 2}, name='USA')
names = names.append([s1, s2])

# print(names)

bball_16 = pd.read_csv('data/baseball16.csv')
# print(bball_16.head())

data_dict = bball_16.iloc[0].to_dict()
# print(data_dict)

new_data_dict = {k: '' if isinstance(v, str) else
                 np.nan for k, v in data_dict.items()}

# print(new_data_dict)

stocks_2016 = pd.read_csv('data/stocks_2016.csv', index_col='Symbol')
stocks_2017 = pd.read_csv('data/stocks_2017.csv', index_col='Symbol')

stock_list = [stocks_2016, stocks_2017]
stocks = pd.concat(stock_list, join='inner', keys=['2016', '2017'],
                   names=['Year', None],
                   axis='columns')
# print(stocks)
years = [2016, 2017, 2018]
stock_tables = [pd.read_csv('data/stocks_{}.csv'.format(year),
                            index_col='Symbol') for year in years]
stocks_2016, stocks_2017, stocks_2018 = stock_tables
# print(stocks_2016, stocks_2017, stocks_2018)

# stocks = pd.concat(stock_tables, keys=years)
stocks = pd.concat(dict(zip(years, stock_tables)), axis=1, sort=True)
# print(stocks)

other = [stocks_2017.add_suffix('_2017'),
         stocks_2018.add_suffix('_2018')]

stocks_join = stocks_2016.add_suffix('_2016').join(other, how='outer')

# print(stocks_join)

step1 = stocks_2016.merge(stocks_2017, left_index=True, right_index=True,
                          how='outer', suffixes=('_2016', '_2017'))

stocks_merge = step1.merge(stocks_2018.add_suffix('_2018'), left_index=True,
                           right_index=True, how='outer')
# print(stocks_merge)

names = ['prices', 'transactions']
food_tables = [pd.read_csv('data/food_{}.csv'.format(name))
               for name in names]
food_prices, food_transactions = food_tables
# print(food_prices, food_transactions)

tx_amts = food_transactions.merge(food_prices.query('Date == 2017'),
                                  how='left')
# print(tx_amts)

food_prices_join = food_prices.query('Date == 2017').set_index(
    ['item', 'store'])
# print(food_prices_join)

tx_join = food_transactions.join(food_prices_join, on=['item', 'store'])
# print(tx_join)
