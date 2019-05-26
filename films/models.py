from django.db import models


class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=30)


    def __str__(self):
        return self.movieid + '|' + self.title

    @staticmethod
    def get_name():
        return 'movie'


class Users(models.Model):

    distances_str = models.CharField(max_length=30000)
    ratings_str = models.CharField(max_length=20000)

    def __str__(self):
        return 'User #' + str(self.id)

    @staticmethod
    def get_name():
        return 'userid'

class Movies(models.Model):

    movieid = models.IntegerField(primary_key=True, default=0)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    @staticmethod
    def get_name():
        return 'movieid'


class Ratings(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, to_field='movieid', on_delete=models.CASCADE, default=0)
    rating = models.FloatField()

    def __str__(self):
        return '(' + str(self.user) + ',' + str(self.movie) + ',' + str(self.rating) + ')'

    @staticmethod
    def get_name():
        return 'rating'

class Links(models.Model):

    movie = models.ForeignKey(Movies, to_field='movieid', on_delete=models.CASCADE, default=0)
    imdbid = models.CharField(max_length=20)

    def __str__(self):
        return '(' + str(self.movie) + ',' + str(self.imdbid) + ')'

    @staticmethod
    def get_name():
        return 'imdbid'