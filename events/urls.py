from django.urls import path
from events import views

urlpatterns = [
    path('api/events/', views.EventListCreateView.as_view(), name='event-list'),
    path('api/events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
]
