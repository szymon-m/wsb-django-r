import math

'''
#  helper methods for calculating distances (esp. Euclidean distances on users vectors)
#
#
'''

def calculateManually(x, y):

    result = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

    print(result)

    return result