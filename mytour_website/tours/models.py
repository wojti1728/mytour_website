from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('PLace Name', max_length=100)
    description = models.TextField(max_length=300)
    address = models.CharField(max_length=200)
    web = models.URLField('Web Address')
    owner = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return f"{self.name}"


class Transport(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.type}"


class Accommodation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Accomadation Names', max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


# class Sightseeing(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(max_length=300)
#     address = models.ForeignKey(Place, on_delete=models.CASCADE)
#     price = models.IntegerField()

#     def __str__(self):
#         return f"Sightseeing: {self.name}"


# class Day(models.Model):
#     date = models.DateField()
#     places = models.ManyToManyField(Place, related_name='days')
#     accomadation = models.ForeignKey(
#         Accommodation, on_delete=models.CASCADE, related_name='days', blank=True)
#     sightseeing = models.ManyToManyField(Sightseeing, related_name='days')

#     def __str__(self):
#         return f"Day: {self.date}"


class ThingsList(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField('Title', max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.title}"


class MyTourUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tour(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    transports = models.ManyToManyField(
        Transport, blank=True, default=None)
    price = models.IntegerField()
    administrator = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(
        MyTourUser, blank=True)
    tour_plan = models.TextField(max_length=1000, default=None)
    accommodation = models.ForeignKey(
        Accommodation, blank=True, null=True, on_delete=models.CASCADE)
    places = models.ManyToManyField(
        Place, blank=True)
    things_list = models.ManyToManyField(
        ThingsList, blank=True, default=None)

    def __str__(self):
        return f"{self.title}"
