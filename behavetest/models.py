from django.db import models
import json


class Ratings(models.Model):
    userid = models.IntegerField(primary_key=True)
    rating = models.CharField(max_length=20000)
    # def __str__(self):
    #     return self.movieid + '|' + self.userid

    @staticmethod
    def get_name():
        return 'userid'

    # def set_rating(self, x):
    #     self.rating = json.dumps(x)
    #
    # def get_rating(self):
    #     return json.loads(self.rating)