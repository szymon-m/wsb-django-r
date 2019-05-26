import numpy
from pandas import *
from numpy.linalg import *

ratings_df = pandas.read_csv("../behavetest/test_csv/ratings.csv")

print(ratings_df.count())

print(ratings_df.head())

user_ratings_df = ratings_df.pivot(index='userId', columns='movieId', values='rating')

user_ratings_df = user_ratings_df.fillna(0)

print(user_ratings_df.head())



user_1 = user_ratings_df.iloc[1,:]

print(type(user_1))

np_user_ratings = user_ratings_df.to_numpy()

print(list(np_user_ratings[0,0:4]))

print(type(np_user_ratings))



user_1 = np_user_ratings[1,]
user_2 = np_user_ratings[609,]


euclid = numpy.linalg.norm(user_1-user_2)

print(euclid)


