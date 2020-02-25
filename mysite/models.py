from django.db import models

# Create your models here.
class Event(models.Model):
    pass

class Clients(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date = models.DateField()
    phone_number = models.IntegerField()
    email = models.EmailField()
    event = models.ManyToManyField(Event)

    def __str__(self):
        return self.name