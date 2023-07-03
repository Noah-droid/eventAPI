from rest_framework import serializers
from events.models import Event, Venue

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer()

    class Meta:
        model = Event
        fields = '__all__'