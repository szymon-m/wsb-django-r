from films.models import Users, Movies, Ratings


def populate_users(ratings_file):

    usr = []

    with open(ratings_file, encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')

            usr.append(int(columns[0]))

    usr = sorted(usr, reverse=True)

    print(Users.objects.count())

    for x in range(1,int(usr[0])+1):
        Users.objects.create()
        print(Users.objects.count())

    Users.objects.get(id=1)  # there is no id=0 !! OK

    usr = []

def populate_movies(movies_file):

    #movies = []

    #Movies.objects.create(title="hello")

    with open(movies_file, encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')
            Movies.objects.create(movieid=int(columns[0]), title=columns[1])



    # for movie in movies:
    #     Movies.objects.create(title=movie)


def populate_ratings(ratings_file):

    with open(ratings_file, encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')
            Ratings.objects.create(movie=Movies.objects.get(movieid=int(columns[1])),
                                   user=Users.objects.get(id=int(columns[0])),
                                   rating=columns[2])