from behave import *
from hamcrest  import *
from helpers import distance
import numpy as np

use_step_matcher("parse")
counter = 0

@given('I got user#1 rating {user1:f} and user#2 rating {user2:f}')
def step_impl(context, user1, user2):

    global counter
    counter = user1 + user2
    """
    :type context: behave.runner.Context
    :type user1: str
    :type user2: str
    """

@when("I want calculate Euclidean distance between them")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


@then("I should receive result {result}")
def step_impl(context, result):
    """
    :type context: behave.runner.Context
    :type result: str
    """
    assert (counter == 5)

'''
#
#   helper.caluclateManually(x,y)
#
#
'''

@given("Vector of ratings of user#1 [1.1,2.1,3.22] and user#2 [3.2,4.34,2.1]")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user1_vector = [1.1, 2.1, 3.22]
    context.user2_vector = [3.2, 4.34, 2.1]


@when("I calculate sqrt on sum of differences")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.manual_result = distance.calculateManually(context.user1_vector, context.user2_vector)

@then("The calculated distance should be [3.2683329083800503]")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.manual_result,equal_to(3.2683329083800503))
    # assert(context.manual_result == 3.2683329083800503)

'''
    Calculating using numpy.linalg.norm from numpy Python library
'''

@given("Having user#1 vector [1.1,2.1,3.22] and user#2 vector  [3.2,4.34,2.1]")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user1_vector = [1.1, 2.1, 3.22]
    context.user2_vector = [3.2, 4.34, 2.1]


@given("Having matrix with first row : user#1 vector [1.1,2.1,3.22] and second row user#2 vector [3.2,4.34,2.1]")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.user1_np_array = np.array([1.1, 2.1, 3.22])
    context.user2_np_array = np.array([3.2, 4.34, 2.1])



@when("i use calculateNumpyNorm()")
def step_impl(context):

    """
    :type context: behave.runner.Context
    """
    context.numpy_norm_result = distance.calculateNumpyNorm(context.user1_np_array,context.user2_np_array)

@then("I should receive [3.2683329083800503]")
def step_impl(context):
    """
       :type context: behave.runner.Context
    """

    assert_that(context.numpy_norm_result,equal_to(3.2683329083800503))