from django import forms
from .models import State, Place


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'state', 'description']
