from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import ClientTrainer
from .models import ForumPost
from .models import ForumReply
from .models import TrainerReview
from .models import TrainerBlog
from .models import Workout
from .serializers import ClientTrainerSerializer, TrainerBlogSerializer, TrainerReviewSerializer, WorkoutSerializer
from .serializers import ForumPostSerializer
from .serializers import ForumReplySerializer
from .serializers import TrainerReview
from .serializers import TrainerBlog
from .serializers import Workout
from django.http.response import Http404
from django.contrib.auth import get_user_model
User = get_user_model()

class WorkoutList(APIView):

    permission_classes = [AllowAny]
    
    def get(self,request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ViewClientWorkout(APIView):

    permission_classes = [AllowAny]
    
    def get_object(self,pk):
        try:
            return Workout.objects.get(pk=pk)
        except Workout.DoesNotExist:
            raise Http404

    def get(self,request,user_id):
        workout = Workout.objects.filter(user_id = user_id)
        serializer = WorkoutSerializer(workout, many=True)
        return Response(serializer.data)

    def put(self,request,user_id):
        workout = self.get_object(user_id)
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignTrainer(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        clients = ClientTrainer.objects.all()
        serializer = ClientTrainer(clients, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ClientTrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TrainerClients(APIView):

    permission_classes = [AllowAny]

    def get_object(self,pk):
        try:
            return ClientTrainer.objects.get(pk=pk)
        except ClientTrainer.DoesNotExist:
            raise Http404

    def get(self,request,trainer_id):
        clients = ClientTrainer.objects.filter(trainer_id = trainer_id)
        serializer = ClientsTrainer(clients, many=True)
        return Response(serializer.data)


class ClientsTrainer(APIView):

    permission_classes = [AllowAny]

    def get_object(self,pk):
        try:
            return ClientTrainer.objects.get(pk=pk)
        except ClientTrainer.DoesNotExist:
            raise Http404

    def get(self,request,client_id):
        trainer = ClientTrainer.objects.filter(client_id = client_id)
        serializer = ClientTrainerSerializer(trainer, many=True)
        return Response(serializer.data)

class ForumPostList(APIView):

    permission_classes =[AllowAny]

    def get(self,request):
        post = ForumPost.objects.all()
        serializer = ForumPostSerializer(post, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ForumPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ForumReplyList(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        reply = ForumReply.objects.all()
        serializer = ForumReplySerializer(reply, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ForumReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ViewReply(APIView):
    def get_object(self,pk):
        try:
            return ForumReply.objects.get(pk=pk)
        except ForumReply.DoesNotExist:
            raise Http404
    
    def get(self,request, comment):
        reply = ForumReply.objects.filter(comment_id=comment)
        serializer = ForumReplySerializer(reply, many=True)
        return Response(serializer.data)

class TrainerReviews(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        review = TrainerReview.objects.all()
        serializer = ForumPostSerializer(review, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TrainerReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TrainerReviewDetails(APIView):
    
    permission_classes = [AllowAny]

    def get_object(self,pk):
        try:
            return TrainerReview.objects.get(pk=pk)
        except TrainerReview.DoesNotExist:
            raise Http404
    
    def get(self,request,user_id):
        review = TrainerReview.objects.filter(user_id = user_id)
        serializer = TrainerReviewSerializer(review, many=True)
        return Response(serializer.data)

class TrainerBlogList(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        review = TrainerBlog.objects.all()
        serializer = TrainerBlogSerializer(review, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TrainerReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TrainerBlogDetail(APIView):

    permission_classes = [AllowAny]

    def get_object(self,pk):
        try:
            return TrainerBlog.objects.get(pk=pk)
        except TrainerReview.DoesNotExist:
            raise Http404
    
    def get(self,request,user_id):
        review = TrainerBlog.objects.filter(user_id = user_id)
        serializer = TrainerBlogSerializer(review, many=True)
        return Response(serializer.data)