from django.db import models

# Create your models here.
class Event(models.Model):
    pass

class Clients(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=255)
    event = models.ManyToManyField(Event)

    def __str__(self):
        return self.name