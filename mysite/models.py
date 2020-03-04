from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



class Event(models.Model):
    name = models.CharField(max_length=255, null=False)
    event_date = models.DateField(null=False)
    place = models.CharField(max_length=255, null=False)
    price = models.FloatField(blank=True, null=True)
    event_time = models.TimeField(null=False)
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Client(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    event = models.ForeignKey(Event, related_name='clients', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)