Feature: IN Memory tables

  Due to slow loading of large dataset into db, in-memory tables for presentation purpose

  Scenario: 1.'Main_ratings' in memory table
    Given Having ratings.csv file with cross data users/films/ratings
    When I call helpers.create_main_ratings(rating_file)
    Then I should obtain main_ratings in-memory table

  Scenario: 2. 'Movies' in-memory table
    Given From movies.csv file and links.csv
    When I call helpers.create_movies_table(movies_file, links_file)
    Then I should receive table with rows containing movie_id, title, genre and IMDB link id
