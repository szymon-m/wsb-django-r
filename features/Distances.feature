Feature: EUCLIDEAN : calculating Euclidean distances for various data types and sets

  Various helper functions for calculating Euclidean distance.
  Recommender systems is based on calculated distances of user vectors.
  The closest proximity between users (the lowest distance value) mean higher similarity of users
  resulting in higher weights for such user's ratings.

  Scenario Outline: Float example values
    Given I got user#1 rating <user1> and user#2 rating <user2>
    When I want calculate Euclidean distance between them
    Then I should receive result <result>

    Examples:
      | user1         | user2       | result    |
      | 1.6           | 3.4         | 5         |


  Scenario: helpers.calculateManually() -> Manually calculated Euclidean distance
    Given Vector of ratings of user#1 [1.1,2.1,3.22] and user#2 [3.2,4.34,2.1]
    When I calculate sqrt on sum of differences
    Then The calculated distance should be [3.2683329083800503]



  Scenario: helpers.calculateNumpyNorm() -> calculating distance using np.linalg.norm
    Given Having matrix with first row : user#1 vector [1.1,2.1,3.22] and second row user#2 vector [3.2,4.34,2.1]
    When i use calculateNumpyNorm()
    Then I should receive [3.2683329083800503]