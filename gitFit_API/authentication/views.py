
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework import generics, response
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class UserView(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many = True)
        return Response(serializer.data)
