from serializers.events import EventSerializer, AttendeeSerializer
from rest_framework import viewsets
from .models import Event
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import redirect
from rest_framework.response import Response

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('/auth/api/token/')  
    #     return super().dispatch(request, *args, **kwargs)


class EventAttendeesViewSet(viewsets.ViewSet):
    def list(self, request, event_id=None):
        event = Event.objects.get(id=event_id)
        attendees = event.attendees.all()
        
        # Serialize the attendees and return the response
        serializer = AttendeeSerializer(attendees, many=True)
        return Response(serializer.data)
    
class EventSearchViewSet(viewsets.ViewSet):
    def list(self, request):
        date = request.GET.get('date')
        location = request.GET.get('venue')
        category = request.GET.get('category')
        
        # Perform the search based on the criteria
        events = Event.objects.filter(date=date, location=location, category=category)
        
        # Serialize the events and return the response
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)