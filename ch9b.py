"""Exercise the final section of Chapter 9."""

import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data/chinook.db')

tracks = pd.read_sql_table('tracks', engine)
genres = pd.read_sql_table('genres', engine)
# print(tracks.head())

genre_track = genres.merge(tracks[['GenreId', 'Milliseconds']],
                           on='GenreId', how='left')
genre_track = genre_track.drop('GenreId', axis='columns')
genre_time = genre_track.groupby('Name')['Milliseconds'].mean()
genre_time = pd.to_timedelta(genre_time, unit='ms').dt.floor('s').sort_values()

# print(genre_time)

cust = pd.read_sql_table('customers', engine,
                         columns=['CustomerId', 'FirstName', 'LastName'])
invoice = pd.read_sql_table('invoices', engine,
                            columns=['InvoiceId', 'CustomerId'])
ii = pd.read_sql_table('invoice_items', engine,
                       columns=['InvoiceId', 'UnitPrice', 'Quantity'])
cust_inv = cust.merge(invoice, on='CustomerId').merge(ii, on='InvoiceId')
# print(cust_inv.head(15))

total = cust_inv['Quantity'] * cust_inv['UnitPrice']
cols = ['CustomerId', 'FirstName', 'LastName']
cust_inv = cust_inv.assign(Total=total).groupby(
    cols)['Total'].sum().sort_values(ascending=False)
print(cust_inv)
