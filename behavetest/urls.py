from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_user),
    path('db_test', views.show_records)
]