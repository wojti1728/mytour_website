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
    path('list_places/', views.list_places, name='list-places'),
    path('show_place/<id>', views.show_place, name='show-place'),
    path('search_places/', views.search_places, name="search-places"),
    path('update_place/<id>', views.update_place, name='update-place'),
    path('update_tour/<id>', views.update_tour, name='update-tour'),
    path('list_tours/', views.list_tours, name="list-tours2"),
]
