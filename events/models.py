from django.db import models
from django.contrib.auth.models import User
from auth_app.models import User
import uuid
from django.utils import timezone
from django.contrib.auth import get_user_model

class Venue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(User, related_name='events_attending')

    def __str__(self):
        return self.title

    def is_past_event(self):
        return self.date < timezone.now().date()

    def get_attendees_count(self):
        return self.attendees.count()


User = get_user_model()

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
