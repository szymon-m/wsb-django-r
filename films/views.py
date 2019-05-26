from django.http import HttpResponse
from django.shortcuts import render

import helpers
from films.models import *
from helpers import models


# Create your views here.


def simple_films(request):

    x = 0
    response = '<html><head></head><body>'
    # https://stackoverflow.com/questions/3284827/python-3-chokes-on-cp-1252-ansi-reading  added encoding to utf-8
    with open('films/csv_data/movies.csv', encoding="utf-8") as f:
        for row in f.readlines()[1:]:
            columns = row.split(',')

            if x < 5:

                response += columns[0] + ' : ' + columns[1] + '<br>'
                m = Movie(movieid=columns[0], title=columns[1])
                m.save()
                x += 1

            response += '\n</body></html>'

        if Movie.objects.all().count() == 5:
            return HttpResponse(response)
        else:
            return HttpResponse("Fail")


def show_main(request):

    ratings_file = 'films/csv_data/ratings.csv'
    movies_file = 'films/csv_data/movies.csv'
    links_file = 'films/csv_data/links.csv'

    helpers.models.populate_users(ratings_file)
    helpers.models.populate_movies(movies_file)
    helpers.models.populate_links(links_file)
    helpers.models.populate_ratings(ratings_file)


    context = {'helloworld': 'Wybierz ID użytkownika do rekomendacji: '}
    return render(request, 'films/main.html', context)

