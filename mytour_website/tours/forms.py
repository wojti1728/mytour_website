from django import forms
from django.forms import ModelForm
from .models import Tour, Place, Day, Accommodation, Sightseeing, ThingsList


# quick test
class TourForm(forms.ModelForm):
    # Custom form fields for related models
    place = forms.ModelChoiceField(
        queryset=Place.objects.all(), required=False)
    accommodation = forms.ModelChoiceField(
        queryset=Accommodation.objects.all(), required=False)
    sightseeing = forms.ModelMultipleChoiceField(
        queryset=Sightseeing.objects.all(), required=False)
    things_list = forms.ModelMultipleChoiceField(
        queryset=ThingsList.objects.all(), required=False)

    class Meta:
        model = Tour
        fields = '__all__'


class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = '__all__'


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
