from behave import *
from django.db.models import QuerySet
from hamcrest import *
from behavetest.models import TestData

use_step_matcher("re")


@given("Having model TestData and example dataset with fields \[imie\] and \[nazwisko\]")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_data = TestData.objects.all()


@when("When I save (?P<imie>.+) and (?P<nazwisko>.+)")
def step_impl(context, imie, nazwisko):
    """
    :type context: behave.runner.Context
    :type imie: str
    :type nazwisko: str
    """
    TestData.objects.create(imie=imie, nazwisko=nazwisko)


@then("I should be able to read object containing (?P<imie>.+) and (?P<nazwisko>.+)")
def step_impl(context, imie, nazwisko):
    """
    :type context: behave.runner.Context
    :type imie: str
    :type nazwisko: str
    """

    expected = TestData(imie=imie, nazwisko=nazwisko)

    assert_that(TestData.objects.get(imie__exact=imie, nazwisko__exact=nazwisko), equal_to(expected))
