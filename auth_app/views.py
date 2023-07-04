from rest_framework import generics
from rest_framework.permissions import AllowAny
from serializers.user import UserSerializer, TokenObtainPairSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



# class TokenObtainPairView(TokenObtainPairView):
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         token_pair = serializer.validated_data
#         return Response(token_pair, status=status.HTTP_200_OK)
