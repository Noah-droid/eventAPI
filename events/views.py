# from rest_framework import generics, permissions
# from .models import Event
# from serializers.events import EventSerializer

# class EventListCreateView(generics.ListCreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.request.user.is_authenticated:
#             # Filter events based on the authenticated user
#             queryset = queryset.filter(user=self.request.user)
#         return queryset
