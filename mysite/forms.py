from .models import Client, Event, Message, Document
from django import forms
import datetime


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'birth_date', 'phone_number', 'email']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter name:', 'class': 'form-control', 'required': 'required'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter last name:', 'class': 'form-control', 'required': 'required'}),
            'birth_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'Enter birth date:', 'class': 'form-control', 'required': 'required'}),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Enter phone number:', 'class': 'form-control', 'required': 'required'}),
            'email': forms.EmailInput(
                attrs={'type': 'email', 'placeholder': 'Enter email:', 'class': 'form-control', 'required': 'required'}),
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
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Enter time: hour:min'}
            ),
            'place': forms.TextInput(
                attrs={'placeholder': 'Enter event location:', 'class': 'form-control', 'required': 'required'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Enter event price:', 'class': 'form-control'}
            ),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'subject': forms.TextInput(
                attrs={'maxlength': '255', 'placeholder': 'Enter subject:', 'class': 'form-control', 'required': 'required'}
            ),
            'message': forms.TextInput(
                attrs={'placeholder': 'Enter message:', 'class': 'form-control', 'required': 'required'}
            ),
        }




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

        