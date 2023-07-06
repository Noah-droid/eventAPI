from django.urls import path, include, register_converter
from .converters import UUIDConverter
from events.viewsets import EventViewSet, EventAttendeesViewSet, EventSearchViewSet
from rest_framework.routers import DefaultRouter
from events.viewsets import EventViewSet


register_converter(UUIDConverter, 'uuid')
router = DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = [
    # path('api/events/', views.EventListCreateView.as_view(), name='event-list'),
    # path('api/events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('api/', include(router.urls)),
    path('api/events/<event_id>/attendees/', EventAttendeesViewSet.as_view({'get': 'list'}), name='event-attendees'),
    path('api/events/search/', EventSearchViewSet.as_view({'get': 'list'}), name='event-search'),
    path('api/events/<uuid:event_id>/rsvp/', EventViewSet.as_view({'post': 'rsvp'}), name='event-rsvp'),
    path('api/events/<uuid:event_id>/comments/', EventViewSet.as_view({'post': 'comments'}), name='event-comments'),

]
