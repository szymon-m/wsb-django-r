from django.http import HttpResponse
from films.models import Movie

# Create your views here.


def show_films(request):

    x = 0
    response = '<html><head></head><body>'
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
