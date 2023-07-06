from serializers.events import EventSerializer, AttendeeSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Event, Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle



class EventViewSet(viewsets.ModelViewSet):
    allowed_methods = ['GET', 'POST']
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('/auth/api/token/')  
    #     return super().dispatch(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def rsvp(self, request, pk=None):
        event = self.get_object()

        # Retrieve the user making the RSVP
        user = request.user

        # Perform the RSVP logic
        if user in event.attendees.all():
            return Response({'detail': 'You have already RSVPed for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            event.attendees.add(user)
            event.save()
            return Response({'detail': 'RSVP successful.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def comments(self, request, pk=None):
        event = self.get_object()

        # Retrieve the user making the comment
        user = request.user

        # Retrieve the comment text from the request data
        comment_text = request.data.get('comment')

        # Perform the comment creation logic
        if not comment_text:
            return Response({'detail': 'Comment text is required.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Create the comment and associate it with the event
            Comment.objects.create(event=event, user=user, text=comment_text)
            return Response({'detail': 'Comment created successfully.'}, status=status.HTTP_201_CREATED)


class EventAttendeesViewSet(viewsets.ViewSet):
    allowed_methods = ['GET', 'POST']
    throttle_classes = [UserRateThrottle]

    def list(self, request, event_id=None):
        event = Event.objects.get(id=event_id)
        attendees = event.attendees.all()
        
        # Serialize the attendees and return the response
        serializer = AttendeeSerializer(attendees, many=True)
        return Response(serializer.data)
    
class EventSearchViewSet(viewsets.ViewSet):
    allowed_methods = ['GET', 'POST']
    throttle_classes = [UserRateThrottle]

    def list(self, request):
        date = request.GET.get('date')
        location = request.GET.get('venue')
        category = request.GET.get('category')
        
        # Perform the search based on the criteria
        events = Event.objects.filter(date=date, location=location, category=category)
        
        # Serialize the events and return the response
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)