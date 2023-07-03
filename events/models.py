from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    attendees = models.ManyToManyField(User, related_name='events_attending')

