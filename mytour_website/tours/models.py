from django.db import models


class Place(models.Model):
    name = models.CharField('PLace Name', max_length=100)
    description = models.TextField(max_length=300)
    address = models.CharField(max_length=200)
    web = models.URLField('Web Address')

    def __str__(self):
        return f"This is a {self.name}"


class Transport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    type = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"Transport: {self.name}"


class Accommodation(models.Model):
    name = models.CharField('Accomadation Name', max_length=100)
    description = models.TextField(max_length=300)
    address = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return f"Accommodation: {self.name}"


class Sightseeing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    address = models.ForeignKey(Place, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"Sightseeing: {self.name}"


class Day(models.Model):
    date = models.DateField()
    locations = models.ManyToManyField(Location, related_name='days')
    transports = models.ManyToManyField(Transport, related_name='days')
    accomadation = models.ForeignKey(
        Accommodation, on_delete=models.CASCADE, related_name='days')
    food_plans = models.ManyToManyField(FoodPlan, related_name='days')
    sightseeing = models.ManyToManyField(Sightseeing, related_name='days')

    def __str__(self):
        return f"Day: {self.date}"


class ThingsList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"ThingsList: {self.title}"


class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ManyToManyField(
        Day, related_name='tours')
    things_list = models.ManyToManyField(
        ThingsList, related_name='tours', default=None)

    def __str__(self):
        return f"Tour: {self.title}"

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('tour-detail', args=[str(self.id)])
