"""Complete Chapter 7 walkthrough in Pandas Cookbook."""

from collections import OrderedDict
import numpy as np
import pandas as pd


def max_deviation(s):
    """Calculate the max std."""
    std_score = (s - s.mean()) / s.std()
    return std_score.abs().max()


def pct_between_1_3k(s):
    """Determine if a school's pop is between 1 and 3k."""
    return s.between(1000, 3000).mean()


def pct_between(s, low, high):
    """Allow the user to set the low and high bounds."""
    return s.between(low, high).mean()


def check_minority(df, threshold):
    """Determine if a state pop is higher than the minority pct threshold."""
    minority_pct = 1 - df['UGDS_WHITE']
    total_minority = (df['UGDS'] * minority_pct).sum()
    total_ugds = df['UGDS'].sum()
    total_minority_pct = total_minority / total_ugds
    return total_minority_pct > threshold


def find_perc_loss(s):
    """Calculate the percent weight loss since beginning of month."""
    return (s - s.iloc[0]) / s.iloc[0]


def weighted_math_average(df):
    """Calculate weighted average of SAT scores."""
    weighted_math = df['UGDS'] * df['SATMTMID']
    return int(weighted_math.sum() / df['UGDS'].sum())


def weighted_average(df):
    data = OrderedDict()
    weight_m = df['UGDS'] * df['SATMTMID']
    weight_v = df['UGDS'] * df['SATVRMID']
    wm_avg = weight_m.sum() / df['UGDS'].sum()
    wv_avg = weight_v.sum() / df['UGDS'].sum()

    data['weighted_math_avg'] = wm_avg
    data['weighted_verbal_avg'] = wv_avg
    data['math_avg'] = df['SATMTMID'].mean()
    data['verbal_avg'] = df['SATVRMID'].mean()
    data['count'] = len(df)
    return pd.Series(data, dtype='int')


def max_streak(s):
    """Find the longest streak of 1s in a series."""
    s1 = s.cumsum()
    return s.mul(s1).diff().where(lambda x: x < 0).ffill().add(
        s1, fill_value=0).max()


def max_delay_streak(df):
    df = df.reset_index(drop=True)
    s = 1 - df['ON_TIME']
    s1 = s.cumsum()
    streak = s.mul(s1).diff().where(lambda x: x < 0) \
        .ffill().add(s1, fill_value=0)
    last_idx = streak.idxmax()
    first_idx = last_idx - streak.max() + 1
    labels = [first_idx, last_idx]
    df_return = df.loc[labels, ['MONTH', 'DAY']]
    df_return['streak'] = streak.max()
    df_return.index = ['first', 'last']
    df_return.index.name = 'streak_row'
    return df_return


s = pd.Series([0, 1, 1, 0, 1, 1, 1, 0])

s1 = s.cumsum()
s2 = s.mul(s1).diff().where(lambda x: x < 0).ffill().add(s1, fill_value=0)
# print(s2)

flights = pd.read_csv('data/flights.csv')
flights['ON_TIME'] = flights['ARR_DELAY'].lt(15).astype(int)
# print(flights[['AIRLINE', 'ORG_AIR', 'ON_TIME']].head(10))
streaks = (flights.sort_values(['MONTH', 'DAY', 'SCHED_DEP'])
           .groupby(['AIRLINE', 'ORG_AIR'])['ON_TIME']
           .agg(['mean', 'size', max_streak])
           .round(2))

print(streaks.head(10))

lotsodelays = flights.sort_values(['MONTH', 'DAY', 'SCHED_DEP']) \
                     .groupby(['AIRLINE', 'ORG_AIR']) \
                     .apply(max_delay_streak) \
                     .sort_values('streak', ascending=False)

print(lotsodelays.head(20))

# print(flights.head())

# avg_arrdelay = flights.groupby('AIRLINE').agg({'ARR_DELAY': 'mean'})
# avg_arrdelay = flights.groupby('AIRLINE')['ARR_DELAY'].agg('mean')
# avg_arrdelay = flights.groupby('AIRLINE')['ARR_DELAY'].agg(np.mean)
# avg_arrdelay = flights.groupby('AIRLINE')['ARR_DELAY'].mean()
# print(avg_arrdelay.head())

# cancels = flights.groupby(['AIRLINE', 'WEEKDAY']).agg({'CANCELLED': 'sum'})
# print(cancels.head(7))

# candiv = flights.groupby(['AIRLINE', 'WEEKDAY']).agg(
#     {'CANCELLED': ['sum', 'mean'], 'DIVERTED': ['sum', 'mean']})

# print(candiv.head(7))

# group_cols = ['ORG_AIR', 'DEST_AIR']
# agg_dict = {'CANCELLED': ['sum', 'mean', 'size'],
#             'AIR_TIME': ['mean', 'var']}
# route_sum = flights.groupby(group_cols).agg(agg_dict)
# print(route_sum.head(10))

# groups = ['AIRLINE', 'WEEKDAY']
# another_dict = {'DIST': ['sum', 'mean'],
#                 'ARR_DELAY': ['min', 'max']}
# airline_info = flights.groupby(groups).agg(another_dict).astype(int)

# level0 = airline_info.columns.get_level_values(0)
# level1 = airline_info.columns.get_level_values(1)

# airline_info.columns = level0 + '_' + level1
# airline_info = airline_info.reset_index()
# print(airline_info.head(7))

# avg_dist = flights.groupby('AIRLINE',
#                            as_index=False)['DIST'].agg('mean').round(0)
# print(avg_dist)

# bins = [-np.inf, 200, 500, 1000, 2000, np.inf]
# cuts = pd.cut(flights['DIST'], bins=bins)
# print(cuts.head())
# print(cuts.value_counts())

# airline_cuts = flights.groupby(cuts)['AIRLINE'].value_counts(
#    normalize=True).round(3)

# print(airline_cuts.head(15))

# flights_ct = flights.groupby(['ORG_AIR', 'DEST_AIR']).size()
# print(flights_ct.head(20))
# print(flights_ct.loc[[('ATL', 'IAH'), ('IAH', 'ATL')]])
# data_sorted = np.sort(flights[['ORG_AIR', 'DEST_AIR']])

# flights_sort = flights[['ORG_AIR', 'DEST_AIR']].apply(
#    sorted, axis=1, result_type='broadcast')
# print(flights_sort.head())
# flights_sort2 = pd.DataFrame(data_sorted, columns=['AIR1', 'AIR2'])


# rename_dict = {'ORG_AIR': 'AIR1', 'DEST_AIR': 'AIR2'}
# flights_sort = flights_sort.rename(columns=rename_dict)
# flights_ct2 = flights_sort2.groupby(['AIR1', 'AIR2']).size()
# print(flights_ct2.head())
# print(flights_ct2.loc[('ATL', 'IAH')])

# college = pd.read_csv('data/college.csv')

# subset = ['UGDS', 'SATMTMID', 'SATVRMID']
# college2 = college.dropna(subset=subset)
# print(college.shape, college2.shape)

# sat_weight = college2.groupby('STABBR').apply(weighted_math_average)
# print(sat_weight.head())

# weights = college2.groupby('STABBR').apply(weighted_average)
# print(weights)

# grouped = college.groupby('STABBR')
# print(grouped.ngroups)
# print(college['STABBR'].nunique())

# college_filtered = grouped.filter(check_minority, threshold=.5)
# print(college_filtered.head())
# print(college_filtered['STABBR'].nunique())

# state_pop = college.groupby('STABBR')['UGDS'].agg(max_deviation).round(0)
# print(state_pop.head())

# pop_group = college.groupby(['STABBR', 'RELAFFIL'])['UGDS'].agg(
#    pct_between_1_3k)

# pop_group = college.groupby(['STABBR', 'RELAFFIL'])['UGDS'].agg(
#     pct_between, 1000, 10000)

# print(pop_group.head(9))

# grouped = college.groupby(['STABBR', 'RELAFFIL'])
# print(type(grouped))
# print([attr for attr in dir(grouped) if not attr.startswith('_')])
# print(grouped.get_group(('FL', 1)).head())
# for name, group in grouped:
#    print(name)
#    print(group.head(3))

# weight_loss = pd.read_csv('data/weight_loss.csv')
# bob_jan = weight_loss.query('Month=="Jan" and Name=="Bob"')
# bob_jan_pct = find_perc_loss(bob_jan['Weight'])

# print(bob_jan_pct)

# pcnt_loss = weight_loss.groupby(['Name', 'Month'])['Weight'].transform(
#     find_perc_loss)
# weight_loss['Perc Weight Loss'] = pcnt_loss.round(3)

# print(weight_loss.query('Name=="Bob" and Month in ["Jan", "Feb"]'))

# week4 = weight_loss.query('Week == "Week 4"')
# week4a = week4.copy()
# month_chron = week4a['Month'].unique()
# week4a['Month'] = pd.Categorical(week4a['Month'], categories=month_chron,
#                                  ordered=True)

# print(week4)

# winner = week4.pivot(index='Month', columns='Name',
#                      values='Perc Weight Loss')
# winner['Winner'] = np.where(winner['Amy'] < winner['Bob'], 'Amy', 'Bob')
# print(winner)
# print(winner.Winner.value_counts())

# winnera = week4a.pivot(index='Month', columns='Name',
#                        values='Perc Weight Loss')
# print(winnera)
