
from rest_framework.status import HTTP_404_NOT_FOUND
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

class UserDetail(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise HTTP_404_NOT_FOUND
    
    def get(self,request,pk):
        comment = self.get_object(pk)
        serializer = RegistrationSerializer(comment)
        return Response(serializer.data)
