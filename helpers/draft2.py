import numpy
from pandas import *
from numpy.linalg import *

ratings_df = pandas.read_csv("../films/csv_data/ratings.csv")

user_id = ratings_df['userId']
print(user_id.size)

print(ratings_df.count().get('userId'))
print(ratings_df.ndim)
print(ratings_df.head())

user_ratings_df = ratings_df.pivot(index='userId', columns='movieId', values='rating')

user_ratings_df = user_ratings_df.fillna(0)

print(user_ratings_df.head())

expected = pandas.DataFrame(numpy.array([
    [1,'Toy Story (1995)','Adventure|Animation|Children|Comedy|Fantasy','0114709'],
    [2,'Jumanji (1995)','Adventure|Children|Fantasy','0113497'],
    ]), columns=['movieId', 'title', 'genres', 'imdbId'])
print(expected.iloc[0,0:4])

test_df = pandas.DataFrame(numpy.array([[1,'Toy Story (1995)','Adventure|Animation|Children|Comedy|Fantasy','0114709']]),
                                columns=['movieId', 'title', 'genres', 'imdbId'])

part = expected.iloc[0,0:4].to_list()
print(part)
print(expected)

user_1 = user_ratings_df.iloc[1:2,1:4]

print(user_1)

np_user_ratings = user_ratings_df.to_numpy()

print(list(np_user_ratings[0,0:4]))



print(type(np_user_ratings))



user_1 = np_user_ratings[1,]
user_2 = np_user_ratings[609,]


euclid = numpy.linalg.norm(user_1-user_2)

print(euclid)


