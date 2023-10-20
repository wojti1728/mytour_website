from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Tour
from .forms import PlaceForm
from django.http import HttpResponseRedirect
from .models import Tour, Day
from .forms import TourForm, DayForm
from django.forms import modelformset_factory, inlineformset_factory


def create_tour(request):
    TourDayFormSet = modelformset_factory(
        Day, form=DayForm, extra=1, can_delete=True)

    if request.method == 'POST':
        tour_form = TourForm(request.POST, prefix='tour')
        day_formset = TourDayFormSet(request.POST, prefix='day')

        if tour_form.is_valid() and day_formset.is_valid():
            tour = tour_form.save()
            days = day_formset.save(commit=False)
            for day in days:
                day.tour = tour
                day.save()

            return redirect('success-url')  # Redirect to a success page
    else:
        tour_form = TourForm(prefix='tour')
        day_formset = TourDayFormSet(prefix='day')

    return render(request, 'tours/create_tour.html', {
        'tour_form': tour_form,
        'day_formset': day_formset,
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
