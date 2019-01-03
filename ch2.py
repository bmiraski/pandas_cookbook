"""Follow Chapter 2 of Pandas Cookbook."""

import pandas as pd

# movie = pd.read_csv('data/movie.csv')

# movie_actor_director = movie[['actor_1_name', 'actor_2_name',
#                               'actor_3_name', 'director_name']]

# print(movie_actor_director.head())

# print(movie[['director_name']].head())

# print(movie.get_dtype_counts())

# movie = movie.select_dtypes(include=['number'])
# movie = movie.filter(like='facebook')
# movie = movie.filter(regex='\d')

# print(movie.head())

# disc_core = ['movie_title', 'title_year', 'content_rating', 'genres']
# disc_people = ['director_name', 'actor_1_name', 'actor_2_name',
#                'actor_3_name']
# disc_other = ['color', 'country', 'language', 'plot_keywords',
#               'movie_imdb_link']

# cont_fb = ['director_facebook_likes', 'actor_1_facebook_likes',
#            'actor_2_facebook_likes', 'actor_3_facebook_likes',
#            'cast_total_facebook_likes', 'movie_facebook_likes']

# cont_finance = ['budget', 'gross']
# cont_num_reviews = ['num_voted_users', 'num_user_for_reviews',
#                     'num_critic_for_reviews']
# cont_other = ['imdb_score', 'duration', 'aspect_ratio',
#               'facenumber_in_poster']

# new_col_order = (disc_core + disc_people + disc_other + cont_fb +
#                  cont_finance + cont_num_reviews + cont_other)

# movie2 = movie[new_col_order]
# print(movie2.head())

# print(movie.shape, movie.size, movie.ndim, len(movie))

# print(movie.count())

# print(movie.describe())

college = pd.read_csv('data/college.csv', index_col='INSTNM')

# college = college + 5

college = college.filter(like='UGDS_')
# college = (college + 0.00001).round(2)

# print((college == .0019).head())

# print(college.head())

# diversity = pd.read_csv('data/college_diversity.csv', index_col='School')

# print(diversity.head(10))

college = college.dropna(how='all')
print(college.isnull().sum())

collfifteen = college.ge(.15)

div_metric = collfifteen.sum(axis=1)

# print(div_metric.head())
# print(div_metric.sort_values(ascending=False).head())

# print(college.loc[['Regency Beauty Institute-Austin', 'Central Texas Beauty College-Temple']])

us_news_top = ['Rutgers University-Newark',
                   'Andrews University',
                   'Stanford University',
                   'University of Houston',
                   'University of Nevada-Las Vegas']

print(div_metric.loc[us_news_top])
