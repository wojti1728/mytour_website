from . import views
from django.urls import path, include


urlpatterns = [
    # Path converters
    # int: numbers
    # str: strings
    # path: whole urls
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
]
