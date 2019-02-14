"""Conduct sample exercises from Chapter 8."""

import numpy as np
import pandas as pd


def change_col_name(col_name):
    """Change column names to have numbers at the end."""
    col_name = col_name.replace('_name', '')
    if 'facebook' in col_name:
        fb_idx = col_name.find('facebook')
        col_name = col_name[:5] + col_name[fb_idx - 1:] + col_name[5:fb_idx-1]
    return col_name


state_fruit = pd.read_csv('data/state_fruit.csv', index_col=0)
state_fruit_tidy = state_fruit.stack().rename_axis(['state', 'fruit'])
# print(state_fruit_tidy)
state_fruit_tidy = state_fruit_tidy.reset_index(name='weight')
# print(state_fruit_tidy)

state_fruit2 = pd.read_csv('data/state_fruit2.csv')
# print(state_fruit2)

state_fruit2 = state_fruit2.melt(id_vars=['State'],
                                 value_vars=['Apple', 'Orange', 'Banana'],
                                 var_name='Fruit',
                                 value_name='Weight')
# print(state_fruit2)

movie = pd.read_csv('data/movie.csv')
actor = movie[['movie_title', 'actor_1_name', 'actor_2_name', 'actor_3_name',
               'actor_1_facebook_likes', 'actor_2_facebook_likes',
               'actor_3_facebook_likes']]
actor2 = actor.rename(columns=change_col_name)

stubs = ['actor', 'actor_facebook_likes']
actor2_tidy = pd.wide_to_long(actor2,
                              stubnames=stubs,
                              i='movie_title',
                              j='actor_num',
                              sep='_')

# print(actor2_tidy.head())

usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
college = pd.read_csv('data/college.csv',
                      index_col='INSTNM',
                      usecols=usecol_func)
college_stacked = college.stack()
# print(college_stacked.head(18))
# print(college_stacked.unstack().head(18))

college2 = pd.read_csv('data/college.csv', usecols=usecol_func)
# print(college2.head())
college_melted = college2.melt(id_vars='INSTNM', var_name='Race',
                               value_name='Percentage')
# print(college_melted.head())
melted_inv = college_melted.pivot(index='INSTNM', columns='Race',
                                  values='Percentage')
# print(melted_inv.head())
college2_replication = melted_inv.loc[
    college2['INSTNM'], college2.columns[1:]].reset_index()
# print(college2_replication.head())

college3 = pd.read_csv('data/college.csv')
cg = college3.groupby(['STABBR', 'RELAFFIL'])['UGDS', 'SATMTMID'].agg(
    ['size', 'min', 'max'])
cg = cg.rename_axis(['AGG_COLS', 'AGG_FUNCS'], axis='columns')
cg = cg.stack('AGG_FUNCS').swaplevel('AGG_FUNCS', 'STABBR', axis='index')
cg = cg.sort_index(level='RELAFFIL', axis='index')
cg = cg.sort_index(level='AGG_COLS', axis='columns')
# print(cg.head(6))


employee = pd.read_csv('data/employee.csv')
emp_grouped = employee.groupby([
    'RACE', 'GENDER'])['BASE_SALARY'].mean().astype(int)

# print(emp_grouped)
emp_adj = emp_grouped.unstack('GENDER').sort_values('Female', ascending=False)
# print(emp_adj)
emp_adj_race = emp_grouped.unstack('RACE')
# print(emp_adj_race)

emp_grouped2 = employee.groupby(['RACE', 'GENDER'])['BASE_SALARY'].agg(
    ['mean', 'max', 'min']).astype(int)

# print(emp_grouped2)
emp_adj2 = emp_grouped2.unstack('GENDER')
# print(emp_adj2)

flights = pd.read_csv('data/flights.csv')
fp = flights.pivot_table(index='AIRLINE', columns='ORG_AIR',
                         values='CANCELLED', aggfunc='sum',
                         fill_value=0).round(2)
# print(fp)

fg = flights.groupby(['AIRLINE', 'ORG_AIR'])['CANCELLED'].sum()
fg2 = fg.unstack('ORG_AIR', fill_value=0).round(2)
# print(fg2.head())

fbig = flights.pivot_table(index=['AIRLINE', 'MONTH'],
                           columns=['ORG_AIR', 'CANCELLED'],
                           values=['DEP_DELAY', 'DIST'],
                           aggfunc=[np.sum, np.mean],
                           fill_value=0)
# print(fbig.head())

fgbig = flights.groupby(['AIRLINE', 'MONTH', 'ORG_AIR',
                         'CANCELLED'])['DEP_DELAY', 'DIST'].agg(
    ['sum', 'mean']).unstack(['ORG_AIR', 'CANCELLED'],
                             fill_value=0).swaplevel(0, 1,
                                                     axis='columns').fillna(0)
# print(fgbig.head())

weightlifting = pd.read_csv('data/weightlifting_men.csv')
# print(weightlifting)

wl_melt = weightlifting.melt(id_vars='Weight Category', var_name='sex_age',
                             value_name='Qual Total')
# print(wl_melt.head())
sex_age = wl_melt['sex_age'].str.split(expand=True)
sex_age.columns = ['Sex', 'Age Group']
sex_age['Sex'] = sex_age['Sex'].str[0]
# print(sex_age.head())

wl_cat_total = wl_melt[['Weight Category', 'Qual Total']]
wl_tidy = pd.concat([sex_age, wl_cat_total], axis='columns')
# print(wl_tidy.head())

inspections = pd.read_csv('data/restaurant_inspections.csv',
                          parse_dates=['Date'])
inspections = inspections.set_index(['Name', 'Date', 'Info'])
inspections = inspections.unstack('Info')
inspections = inspections.reset_index(col_level=-1)
inspections.columns = inspections.columns.droplevel(0).rename(None)
# print(inspections.head(10))

cities = pd.read_csv('data/texas_cities.csv')
geolocations = cities.Geolocation.str.split(pat='. ', expand=True)
geolocations.columns = ['latitude', 'latitude direction', 'longitude',
                        'longitude direction']
geolocations = geolocations.astype({'latitude': 'float',
                                    'longitude': 'float'})
cities_tidy = pd.concat([cities['City'], geolocations], axis=1)
# print(cities_tidy)

sensors = pd.read_csv('data/sensors.csv')
sensors = sensors.melt(id_vars=['Group', 'Property'], var_name='Year')
sensors = sensors.pivot_table(index=['Group', 'Year'], columns='Property',
                              values='value')
sensors = sensors.reset_index()
sensors = sensors.rename_axis(None, axis='columns')
# print(sensors.head(12))

movie = pd.read_csv('data/movie_altered.csv')
movie.insert(0, 'id', np.arange(len(movie)))
stubnames = ['director', 'director_fb_likes', 'actor', 'actor_fb_likes']
movie_long = pd.wide_to_long(movie, stubnames=stubnames,
                             i='id', j='num',
                             sep='_')
movie_long = movie_long.reset_index()
movie_long['num'] = movie_long['num'].astype(int)
# print(movie_long.head(9))
movie_table = movie_long[['id', 'title', 'year', 'duration', 'rating']]
director_table = movie_long[['id', 'num', 'director', 'director_fb_likes']]
actor_table = movie_long[['id', 'num', 'actor', 'actor_fb_likes']]

movie_table = movie_table.drop_duplicates().reset_index(drop=True)
director_table = director_table.dropna().reset_index(drop=True)
actor_table = actor_table.dropna().reset_index(drop=True)

director_cat = pd.Categorical(director_table['director'])
director_table.insert(1, 'director_id', director_cat.codes)
actor_cat = pd.Categorical(actor_table['actor'])
actor_table.insert(1, 'actor_id', actor_cat.codes)

director_associative = director_table[['id', 'director_id', 'num']]
dcols = ['director_id', 'director', 'director_fb_likes']
director_unique = director_table[dcols].drop_duplicates().reset_index(
    drop=True)

actor_associative = actor_table[['id', 'actor_id', 'num']]
acols = ['actor_id', 'actor', 'actor_fb_likes']
actor_unique = actor_table[acols].drop_duplicates().reset_index(drop=True)

print(movie_table.head(9))
# print(director_table.head(9))
print(director_associative.head(9))
print(director_unique.head(9))
# print(actor_table.head(9))
print(actor_associative.head(9))
print(actor_unique.head(9))
