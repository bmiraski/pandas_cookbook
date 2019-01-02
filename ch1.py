import pandas as pd

movie = pd.read_csv('data/movie.csv')

# movie = movie.reset_index()

# movie2 = movie.set_index('movie_title')
# print(movie2.head())

# movie2 = movie2.reset_index()
# print(movie2.head())

# index = movie.index
# columns = movie.columns
# data = movie.values

# print(movie.head())
# print(index)
# print(type(index))
# print(columns)
# print(type(columns))
# print(data)
# print(type(data))

# print(movie.dtypes)
# print(movie.get_dtype_counts())

# print(movie['director_name'])

# director = movie['director_name']
# actor_1_fb_likes = movie['actor_1_facebook_likes']

# print(director.head())
# print(actor_1_fb_likes.head())

# print(director.value_counts())

# print(actor_1_fb_likes.describe())
# print(director.describe())

# imdb_score = movie['imdb_score']
# print(imdb_score)

# print(director.value_counts().head(3))
# print(actor_1_fb_likes.isnull().sum())
# print(actor_1_fb_likes.isnull().mean())

# print(actor_1_fb_likes.fillna(0).astype(int).head())

# idx_rename = {'Avatar': 'Ratava', 'Spectre': 'Ertceps'}
# col_rename = {'director_name': 'Director Name',
#              'num_critic_for_reviews': 'Critical
# Reviews'}

# movie_renamed = movie.rename(index=idx_rename, columns=col_rename)

# print(movie_renamed.head())

# index_list = index.tolist()
# column_list = columns.tolist()

# index_list[0] = 'Ratava'
# index_list[2] = 'Ertceps'
# column_list[1] = 'Director Name'
# column_list[2] = 'Critical Reviews'

# print(index_list)
# print(column_list)

# movie.index = index_list
# movie.columns = column_list

# movie['has_seen'] = 0
# movie['actor_director_facebook_likes'] = (
#     movie['actor_1_facebook_likes'] +
#     movie['actor_2_facebook_likes'] +
#     movie['actor_3_facebook_likes'] +
#     movie['director_facebook_likes']
# )

# print(movie['actor_director_facebook_likes'].isnull().sum())

# movie['actor_director_facebook_likes'] = (
#    movie['actor_director_facebook_likes'].fillna(0).astype(int))

# movie['is_cast_likes_more'] = (
#     movie['cast_total_facebook_likes'] >= (
#         movie['actor_director_facebook_likes'])
# )

# print(movie['is_cast_likes_more'].all())

# movie = movie.drop('actor_director_facebook_likes', axis='columns')

movie['actor_total_facebook_likes'] = (
    movie['actor_1_facebook_likes'] +
    movie['actor_2_facebook_likes'] +
    movie['actor_3_facebook_likes']
    )

movie['actor_total_facebook_likes'] = (
    movie['actor_total_facebook_likes'].fillna(0).astype(int))

movie['is_cast_likes_more'] = (
    movie['cast_total_facebook_likes'] >= (
        movie['actor_total_facebook_likes'])
)

print(movie['is_cast_likes_more'].all())

movie['pct_actor_cast_like'] = (
    movie['actor_total_facebook_likes'] / (
        movie['cast_total_facebook_likes']))

print((movie['pct_actor_cast_like'].min(),
      movie['pct_actor_cast_like'].max())
      )

# print(movie.head())

print(movie.set_index('movie_title')['pct_actor_cast_like'].head())

proft_index = movie.columns.get_loc('gross') + 1
print(proft_index)

movie.insert(loc=proft_index,
             column='profit',
             value=movie['gross'] - movie['budget'])

print(movie.set_index('movie_title')['profit'].head())
