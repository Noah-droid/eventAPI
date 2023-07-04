from rest_framework import generics
from rest_framework.permissions import AllowAny
from serializers.user import UserSerializer, MyTokenObtainPairSerializer
from .models import User

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class TokenObtainPairView(generics.CreateAPIView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [AllowAny]
