from pyexpat.errors import messages
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Tour, Place
from .forms import PlaceForm
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import modelformset_factory, inlineformset_factory
from .forms import TourForm, TourFormAdmin
from django.contrib import messages
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.core.paginator import Paginator
from django.contrib.auth.models import User


def my_tours(request):
    if request.user.is_authenticated:
        me = request.user.id
        tours = Tour.objects.filter(attendees=me)
        return render(request, 'tours/my_tours.html', {'tours': tours})
    else:
        messages.success(
            request, ("You are not authorized to see this page!"))
        return redirect('home')


def tour_pdf(request):
    buf = io.BytesIO()

    # create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    # create a text obj
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont('Helvetica', 14)

    tours = Tour.objects.all()
    lines = []

    for tour in tours:
        lines.append(
            f'Tour Name: {tour.title}{tour.description}{tour.start_date}{tour.end_date}{tour.price}Transport:')
        for transport in tour.transports.all():
            lines.append(f'{transport.type} - {transport.description}')
        lines.append(f'Manager: {tour.administrator}')
        for attendee in tour.attendees.all():
            lines.append(f'{attendee.first_name} {attendee.last_name}')
        lines.append(f'Tour Plan:{tour.tour_plan}')
        lines.append('=================================================')
        # do poprawy zawijanie tekstu
        # www.reportlab.com/docs/reportlab-userquide.pdf

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='tour.pdf')


def tour_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=tour_place.txt'

    tours = Tour.objects.all()
    lines = []

    for tour in tours:
        lines.append(
            f'Tour Name: {tour.title}\n{tour.description}\n{tour.start_date}\n{tour.end_date}\n{tour.price}\n\nTransport:\n')
        for transport in tour.transports.all():
            lines.append(f'{transport.type} - {transport.description}')
        lines.append(f'Manager: {tour.administrator}\n')
        for attendee in tour.attendees.all():
            lines.append(f'{attendee.first_name}  {attendee.last_name}\n')
        lines.append(f'\nTour Plan:\n{tour.tour_plan}\n\n\n')
        # dokonczczyc tutaj reszte ...

    response.writelines(lines)
    return response


def delete_place(request, id):
    place = Place.objects.get(pk=id)
    place.delete()
    return redirect('list-places')


def delete_tour(request, id):
    tour = Tour.objects.get(pk=id)
    if request.user == tour.administrator:
        tour.delete()
        messages.success(
            request, ("Your Tour Was Deleted!"))
        return redirect('list-tours2')
    else:
        messages.success(
            request, ("Your Are Not Authorized To Delete This Tour"))
        return redirect('list-tours2')


def show_tour(request, id):
    tour = Tour.objects.get(pk=id)
    return render(request, 'tours/show_tour.html', {'tour': tour})


def update_tour(request, id):
    tour = Tour.objects.get(pk=id)
    form = TourForm(request.POST or None, instance=tour)
    if form.is_valid():
        form.save()
        return redirect('list-tours2')
    return render(request, 'tours/update_tour.html', {'tour': tour, 'form': form})


def list_tours(request):
    tour_list = Tour.objects.all().order_by('title')
    p = Paginator(Tour.objects.all().order_by('title'), 2)
    page = request.GET.get('page')
    tours = p.get_page(page)
    nums = tours.paginator.num_pages * "*"
    return render(request, 'tours/tour.html', {'tours': tours, 'nums': nums})


def update_place(request, id):
    place = Place.objects.get(pk=id)
    form = PlaceForm(request.POST or None, instance=place)
    if form.is_valid():
        form.save()
        return redirect('list-places')
    return render(request, 'tours/update_place.html', {'place': place, 'form': form})


def search_places(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', False)
        places = Place.objects.filter(name__icontains=searched)

        return render(request, 'tours/search_places.html', {'searched': searched, 'places': places})
    else:
        return render(request, 'tours/search_places.html', {})


def show_place(request, id):
    place = Place.objects.get(pk=id)
    place_owner = User.objects.get(pk=place.owner)
    return render(request, 'tours/show_place.html', {'place': place, 'place_owner': place_owner})


def list_places(request):
    # pagination
    p = Paginator(Place.objects.all(), 2)
    page = request.GET.get('page')
    places = p.get_page(page)
    nums = places.paginator.num_pages * "*"

    return render(request, 'tours/place.html', {'places': places, 'nums': nums})


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


# def create_tour(request):
#     submitted = False
#     if request.method == 'POST':
#         if request.user.is_superuser:
#             tour_form = TourFormAdmin(request.POST)
#             if tour_form.is_valid():
#                 tour_form.save()
#                 return HttpResponseRedirect('/create_tour?submitted=True')
#         else:
#             tour_form = TourForm(request.POST)
#             if tour_form.is_valid():
#                 # tour = tour_form.save(commit=False)
#                 tour.administrator = request.user
#                 tour.save()
#                 return HttpResponseRedirect('/create_tour?submitted=True')
#     else:
#         if request.user.is_superuser:
#             tour_form = TourFormAdmin
#         else:
#             tour_form = TourForm

#         if 'submitted' in request.GET:
#             submitted = True

#     return render(request, 'tours/create_tour.html', {
#         'tour_form': tour_form
#     })


def add_place(request):
    submitted = False
    form = PlaceForm
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.owner = request.user.id
            place.save()
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
