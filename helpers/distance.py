import math
import numpy

'''
#  helper methods for calculating distances (esp. Euclidean distances on users vectors)
#
#
'''

def calculateManually(x, y):

    result = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

    print(result)

    return result


def calculateNumpyNorm(user1_np_array, user2_np_array):

    # numpy.linalg.norm(a-b)
    return numpy.linalg.norm(user1_np_array-user2_np_array)