from . import views
from django.urls import path, include


urlpatterns = [
    # Path converters
    # int: numbers
    # str: strings
    # path: whole urls
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('tours', views.all_tours, name="list-tours"),
    path('add_place', views.add_place, name='add-place'),
    path('create_tour/', views.create_tour, name='create-tour'),
]
