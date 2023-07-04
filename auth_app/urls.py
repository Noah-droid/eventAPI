from django.urls import path
from auth_app import views

urlpatterns = [
    path('api/register/', views.UserCreateView.as_view(), name='user-register'),
    # path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
