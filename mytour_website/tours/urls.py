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
    path('show_tour/<id>', views.show_tour, name='show-tour'),
    path('search_places/', views.search_places, name="search-places"),
    path('update_place/<id>', views.update_place, name='update-place'),
    path('delete_place/<id>', views.delete_place, name='delete-place'),
    path('update_tour/<id>', views.update_tour, name='update-tour'),
    path('delete_tour/<id>', views.delete_tour, name='delete-tour'),
    path('list_tours/', views.list_tours, name="list-tours2"),
    path('tour_text', views.tour_text, name='tour_text'),
    path('tour_pdf', views.tour_pdf, name='tour_pdf'),
    path('my_tours', views.my_tours, name='my_tours'),
    path('search_tours', views.search_tours, name='search_tours'),
    path('add_accommodation', views.add_accommodation, name='add-accommodation'),
]
