from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Place(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('PLace Name', max_length=100)
    description = models.TextField(max_length=300)
    address = models.CharField(max_length=200)
    web = models.URLField('Web Address')
    owner = models.IntegerField(blank=False, default=1)
    place_image = models.ImageField(null=True, blank=True, upload_to="images/")

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


class ThingsList(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField('Title', max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.title}"


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
        User, blank=True, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(
        User, related_name='attendees', blank=True)
    tour_plan = models.TextField(max_length=1000, default=None)
    accommodation = models.ForeignKey(
        Accommodation, blank=True, null=True, on_delete=models.CASCADE)
    places = models.ManyToManyField(
        Place, blank=True)
    things_list = models.ManyToManyField(
        ThingsList, blank=True, default=None)

    def __str__(self):
        return f"{self.title}"

    @property
    def Days_till(self):
        today = date.today()
        days_till = self.start_date - today
        days_till_stripped = str(days_till).split(",", 1)[0]

        return days_till_stripped
