Feature: IMPORTS from .csv files to db and from db to in-memory tables for calculations

  Testing import features loading data into db and fetching data from db to lists in purpose to calculate recommendations

  Scenario: Loading sample data from ratings.csv to example model and retrival
    Given Having ratings.csv file with (userId, movieId, rating, timestamp)
    When While I load them to database model
    Then I should get objects in db
