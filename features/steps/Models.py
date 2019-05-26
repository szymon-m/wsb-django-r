from behave import *
from hamcrest import assert_that, equal_to

import helpers.models
from films.models import *

use_step_matcher("re")


@given("Having ratings\.csv with users")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.ratings_file = 'films/csv_data/ratings.csv'


@when("i call helpers\.models\.populate_users\(ratings_file\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    helpers.models.populate_users(context.ratings_file)


@then("I should have my Users table populated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(Users.objects.count(), equal_to(int(610)))


@given("Having movies\.csv with film titles and genres")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.movies_file = 'films/csv_data/movies.csv'


@when("i call helpers\.models\.populate_movies\(movies_file\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    helpers.models.populate_movies(context.movies_file)


@then("I should have my Movies table populated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(Movies.objects.count(), equal_to(int(9742)))


@given("Having ratings\.csv file with ratings joined with users/movies id's")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.ratings_file = 'films/csv_data/ratings.csv'
    context.movies_file = 'films/csv_data/movies.csv'


@step("populated databases with proper number of users and movies")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    helpers.models.populate_users(context.ratings_file)
    helpers.models.populate_movies(context.movies_file)

    #Users.objects.get(id=1)
    assert_that(Users.objects.count(), equal_to(int(610)))
    assert_that(Movies.objects.count(), equal_to(int(9742)))



@when("calling helpers\.models\.populate_ratings\(rating_file\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    helpers.models.populate_ratings(context.ratings_file)


@then("I should have my Ratings table populated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(Ratings.objects.count(), equal_to((int(100836))))
