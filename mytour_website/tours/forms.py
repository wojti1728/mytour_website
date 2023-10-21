from django import forms
from django.forms import ModelForm
from .models import Tour, Place, Accommodation, ThingsList, Transport, MyTourUser


class TourForm(forms.ModelForm):
    # Custom form fields for related models

    class Meta:
        model = Tour
        fields = ('title', 'description', 'start_date',
                  'end_date', 'transports', 'price', 'administrator',
                  'attendees', 'places', 'tour_plan', 'accommodation', 'things_list',)

        labels = {
            'title': 'Tour Name',
            'description': '',
            'start_date': 'Start Tour Date',
            'end_date': 'End Tour Date',
            'transports': 'Main Transports',
            'price': 'Summary Price',
            'administrator': 'Tour Menager',
            'attendees': '',
            'places': 'Main Place',
            'tour_plan': 'Main Plan of The Tour',
            'accommodation': 'Place of Accommodation',
            'things_list': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Tour Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Description'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'transports': forms.SelectMultiple(attrs={'class': 'form-control w-25'}),
            'administrator': forms.Select(attrs={'class': 'form-select w-25', 'placeholder': 'Tour Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control w-25'}),
            'price': forms.NumberInput(attrs={'class': 'form-control w-25', 'placeholder': 'Tour Price'}),
            'places': forms.SelectMultiple(attrs={'class': 'form-select w-50'}),
            'things_list': forms.SelectMultiple(attrs={'class': 'form-control w-25'}),
            'tour_plan': forms.Textarea(attrs={'class': 'form-control w-75', 'placeholder': 'Tour Plan With Details'}),
        }

# create a tour form


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'description', 'address', 'web')

        labels = {
            'name': '',
            'description': '',
            'address': '',
            'web': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Place Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control w-50', 'placeholder': 'Description'}),
            'address': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Place Address'}),
            'web': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Web Address'})

        }
