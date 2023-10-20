from django import forms
from django.forms import ModelForm
from .models import Tour, Place, Accommodation, ThingsList, Transport, MyTourUser


class TourForm(forms.ModelForm):
    # Custom form fields for related models
    places = forms.ModelChoiceField(
        queryset=Place.objects.all(), required=False)
    accommodation = forms.ModelChoiceField(
        queryset=Accommodation.objects.all(), required=False)
    transports = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'type': 'checkbox'}),
                                                queryset=Transport.objects.all(), required=False)
    things_list = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                 queryset=ThingsList.objects.all(), required=False)

    attendees = forms.ModelMultipleChoiceField(
        queryset=MyTourUser.objects.all(), required=False)

    class Meta:
        model = Tour
        fields = ('title', 'description', 'start_date',
                  'end_date', 'transports', 'price', 'administrator',
                  'attendees', 'tour_plan', 'places', 'accommodation', 'things_list',)

        # labels = {
        # }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-50', 'placeholder': 'Tour Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control w-50', 'placeholder': 'Description'}),
            'start_date': forms.DateInput(),
            'end_date': forms.DateInput(),
            'price': forms.NumberInput(attrs={'class': 'form-control w-25', 'placeholder': 'Tour Price'}),
            'tour_plan': forms.Textarea(attrs={'class': 'form-control w-75', 'placeholder': 'TOur Plan With Details'}),
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
