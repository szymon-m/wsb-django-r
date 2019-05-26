from pandas import *
import itertools

from pandas._libs.parsers import basestring


def create_main_ratings(ratings_file):
    ratings_df = pandas.read_csv(ratings_file)
    user_ratings_df = ratings_df.pivot(index='userId', columns='movieId', values='rating')
    user_ratings_df = user_ratings_df.fillna(0)
    return user_ratings_df


def create_movies_table(movies_file, links_file):
    movies = pandas.read_csv(movies_file)
    links = pandas.read_csv(links_file, dtype={'imdbId': str})

    movies_file_ids = movies['movieId']
    links_file_ids = links['movieId']

    if movies_file_ids.size == links_file_ids.size:
        for x in range(1, movies_file_ids.size):
            if movies_file_ids[x] == links_file_ids[x]:
                continue
            else:
                print("Movie id's not matching!")
                return pandas.DataFrame()

    movies.insert(3, 'imdbId', links['imdbId'])

    return movies



