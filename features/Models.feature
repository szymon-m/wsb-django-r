Feature: DB Models : creating db models for MovieLens 100k dataset

  Creating Db models for MovieLense 100k dataset

  Scenario: Populating Users table
    Given Having ratings.csv with users
    When i call helpers.models.populate_users(ratings_file)
    Then I should have my Users table populated

  Scenario: Populating Movies table
    Given Having movies.csv with film titles and genres
    When i call helpers.models.populate_movies(movies_file)
    Then I should have my Movies table populated

  Scenario: Populating Ratings table
    Given Having ratings.csv file with ratings joined with users/movies id's
    And populated databases with proper number of users and movies
    When calling helpers.models.populate_ratings(rating_file)
    Then I should have my Ratings table populated

  Scenario: Populating Links table
    Given Having links.csv file with movieId and IMDBid
    When calling helpers.models.populate_links(links_file)
    Then I should have my Links table populated


