from .models import Client, Event
from django import forms
import datetime

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'birth_date', 'phone_number', 'email', 'event']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name:', 'class': 'form-control', 'name': 'todo', 'id': 'id_todo', 'required': 'required'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_date', 'event_time', 'place', 'price']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter event name:', 'class': 'form-control', 'required': 'required'}
            ),
            'event_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'min': datetime.date.today() + datetime.timedelta(days=1), 'max': datetime.date.today() + datetime.timedelta(days=365)}
            ),
            'event_time': forms.TimeInput(
                attrs={'type': 'text', 'class': 'form-control'}
            ),
            'place': forms.TextInput(
                attrs={'placeholder': 'Enter event location:', 'class': 'form-control', 'required': 'required'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Enter event price:', 'class': 'form-control'}
            ),
        }