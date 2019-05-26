import numpy
import pandas
from behave import *
from hamcrest import assert_that, equal_to

from helpers.inmemory import create_main_ratings
import hamcrest

import helpers

use_step_matcher("re")


@given("Having ratings\.csv file with cross data users/films/ratings")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.ratings_file = 'films/csv_data/ratings.csv'


@when("I call helpers\.create_main_ratings\(rating_file\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.main_ratings = helpers.inmemory.create_main_ratings(context.ratings_file)


@then("I should obtain main_ratings in-memory table")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # 610 users x 9724 = 5.931.640
    assert_that(context.main_ratings.size, equal_to(int(5931640)))


@given("From movies\.csv file and links\.csv")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.movies_file = 'films/csv_data/movies.csv'
    context.links_file = 'films/csv_data/links.csv'


@when("I call helpers\.create_movies_table\(movies_file, links_file\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.movie_table = helpers.inmemory.create_movies_table(context.movies_file, context.links_file)


@then("I should receive table with rows containing movie_id, title, genre and IMDB link id")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expected = pandas.DataFrame(numpy.array([
        [1, 'Toy Story (1995)', 'Adventure|Animation|Children|Comedy|Fantasy', '0114709'],
        [2, 'Jumanji (1995)', 'Adventure|Children|Fantasy', '0113497'],
    ]), columns=['movieId', 'title', 'genres', 'imdbId'])

    #//TODO: Watch zeros in imdb!! 114709 - pandas gets without zeros as nums while imdb is 0114709 !!

    expected = expected.iloc[0, 0:4].to_list()

    actual = context.movie_table.iloc[0, 0:4].to_list()
    #actual = [str(record) for record in context_actual]

    assert_that(actual, equal_to(expected))