from django.urls import path, include
from events.viewsets import EventViewSet, EventAttendeesViewSet, EventSearchViewSet
from rest_framework.routers import DefaultRouter
from events.viewsets import EventViewSet

router = DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/events/<event_id>/attendees/', EventAttendeesViewSet.as_view({'get': 'list'}), name='event-attendees'),
    path('api/events/search/', EventSearchViewSet.as_view({'get': 'list'}), name='event-search'),
    # path('api/events/', views.EventListCreateView.as_view(), name='event-list'),
    # path('api/events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
]
