from re import I
import django
from django.db.models.expressions import F
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/hotels', views.hotels_api),
]

