from films.models import Users, Movies, Ratings, Links
import sqlite3
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def execute_sql(s):
    con = sqlite3.connect(dir_path + '../../db.sqlite3')
    with con:
        cur = con.cursor()
        cur.execute(s)


def populate_users(ratings_file):

    usr = []

    with open(ratings_file, encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')

            usr.append(int(columns[0]))

    usr = sorted(usr, reverse=True)

    print(Users.objects.count())

    for x in range(1,int(usr[0])+1):
        try:
            Users.objects.get(id=x)
        except Exception as e:
            print("User " + str(x) + " already exists")
            continue
        Users.objects.create()
        print("Users: " + str(Users.objects.count()))

    Users.objects.get(id=1)  # there is no id=0 !! OK

    usr = []


def populate_movies(movies_file):

    with open(movies_file, encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')
            try:
                Movies.objects.update_or_create(movieid=int(columns[0]), title=columns[1])
            except Exception as e:
                print("Movie: " + str(columns[0]) + " - " + str(columns[1]) + " already exists")
                continue

            print("Movies: " + str(Movies.objects.count()))

def populate_ratings(ratings_file):

    with open(ratings_file, encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')
            try:
                Ratings.objects.update_or_create(movie=Movies.objects.get(movieid=int(columns[1])),
                                   user=Users.objects.get(id=int(columns[0])),
                                   rating=columns[2])
            except Exception as e:
                print("Rating: (" + str(columns[0]) + "," + str(columns[1]) + "," + str(columns[2]) + ") already exists")
                continue

            print("Ratings: " + str(Ratings.objects.count()))
        #  ================================
        #  Django testing database result  1m45s
        #  Raw SQL - > over 5m

        # for movie_id in movie_list:
        #     try:
        #
        #         sql = (
        #             '''INSERT INTO films_ratings (user_id, movie_id, rating) VALUES (\'{}\',\'{}\',\'{}\')'''.format(
        #                 int(columns[0]),
        #                 int(columns[1]),
        #                 float(columns[2]),
        #             ))
        #
        #         execute_sql(sql)
        #
        #         print("Insert movie: " + str(columns[0]), str(Ratings.objects.count()))
        #     except Exception as e:
        #         print('Movie Insert Failure: ' + columns[0], e)
        #         continue


def populate_links(links_file):

    with open(links_file, encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')
            try:
                Links.objects.update_or_create(movie=Movies.objects.get(movieid=int(columns[0])),
                                           imdbid=columns[1])
            except Exception as e:
                print("Link : " + str(columns[0]) + " imdb : " + str(columns[1]) + " already exists")
                continue

            print("Links objects: " + str(Links.objects.count()))