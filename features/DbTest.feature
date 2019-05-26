Feature: DB Test - checking behave-django working with test database

  Before migrations - update ## migrations had to be made -- python manage.py makemigrations -> python manage.py migrate

  Scenario Outline: Populating test db and simple test
    Given Having model TestData and example dataset with fields [imie] and [nazwisko]
    When When I save <imie> and <nazwisko>
    Then I should be able to read object containing <imie> and <nazwisko>


    Examples:
      | imie | nazwisko |
      | Jan  | Kowalski |
      | Anna | Dymna    |