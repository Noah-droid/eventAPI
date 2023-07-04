from django.urls import path, include
from events.viewsets import EventViewSet 
from rest_framework.routers import DefaultRouter
from events.viewsets import EventViewSet

router = DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/events/', views.EventListCreateView.as_view(), name='event-list'),
    # path('api/events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
]
