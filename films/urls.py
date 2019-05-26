from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.show_main, name='main'),
    path('simple_films', views.simple_films, name='simple_films'),
]