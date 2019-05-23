from django.db import models


class TestData(models.Model):
    imie = models.CharField(max_length=20, primary_key=True)
    nazwisko = models.CharField(max_length=30)

    def __str__(self):
        return self.imie + '|' + self.nazwisko

    @staticmethod
    def get_name():
        return 'imie'