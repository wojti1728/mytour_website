from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Tour, Place
from .forms import PlaceForm
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory, inlineformset_factory

from .forms import TourForm


def search_places(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', False)
        places = Place.objects.filter(name__icontains=searched)

        return render(request, 'tours/search_places.html', {'searched': searched, 'places': places})
    else:
        return render(request, 'tours/search_places.html', {})


def show_place(request, id):
    place = Place.objects.get(pk=id)
    return render(request, 'tours/show_place.html', {'place': place})


def list_places(request):
    place_list = Place.objects.all()
    return render(request, 'tours/place.html', {'place_list': place_list})


def create_tour(request):
    submitted = False
    if request.method == 'POST':
        tour_form = TourForm(request.POST)

        if tour_form.is_valid():
            tour_form.save()
            return HttpResponseRedirect('/create_tour?submitted=True')
    else:
        tour_form = TourForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'tours/create_tour.html', {
        'tour_form': tour_form
    })


def add_place(request):
    submitted = False
    form = PlaceForm
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_place?submitted=True')
        else:
            form = PlaceForm
            if 'submitted' in request.GET:
                submitted = True

    return render(request, 'tours/add_place.html', {'form': form, 'submitted': submitted})


def all_tours(request):
    tour_list = Tour.objects.all()

    return render(request, 'tours/tour_list.html',
                  {'tour_list': tour_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # convert month from name to number
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M %p')
    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )

    return render(request, 'tours/home.html', {
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "now": now,
        "time": time,
    })
