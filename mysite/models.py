from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255, null=False)
    event_date = models.DateTimeField(null=False)
    place = models.CharField(max_length=255, null=False)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    event = models.ManyToManyField(Event, related_name='events')

    def __str__(self):
        return self.name