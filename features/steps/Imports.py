from behave import *
from django.db.models import QuerySet

from behavetest.models import Ratings
from hamcrest import *
from django.test import TransactionTestCase

use_step_matcher("re")


@given("Having ratings\.csv file with \(userId, movieId, rating, timestamp\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    with open('behavetest/test_csv/ratings.csv', encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')

            r = Ratings(userid=columns[0], movieid=columns[1], rating=columns[2])
            r.save()


@when("While I load them to database model")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@then("I should get objects in db")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(Ratings.objects.all().count(), equal_to(50))
    assert_that(Ratings.objects.get(userid=1, movieid=216, rating=5.0), equal_to(Ratings(userid=1, movieid=216, rating=5.0)))

    #TransactionTestCase.assertQuerysetEqual(Ratings.objects.all(), list(Ratings(userid=1, movieid=216, rating=5.0)))