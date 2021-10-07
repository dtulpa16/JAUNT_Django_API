from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import ClientTrainer
from .models import ForumPost
from .models import ForumReply
from .models import TrainerBlog
from .models import TrainerReview
from .models import Workout
from django.contrib.auth import get_user_model
User = get_user_model()


class ClientTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTrainer
        fields = ('id', 'client','trainer')
 

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ('id', 'user', 'body')

class ForumReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumReply
        fields = ('id', 'comment', 'body')

class TrainerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerReview
        fields = ('id', 'user', 'body')


class TrainerBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerBlog
        fields = ('id', 'user', 'body')

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = (
            'id', 
            'user', 
            'notes', 
            'day1ex1', 
            'day1ex1sets', 
            'day1ex1reps', 
            'day1ex2', 
            'day1ex2reps', 
            'day1ex2sets', 
            'day1ex3', 
            'day1ex3sets', 
            'day1ex3reps', 
            'day1ex4', 
            'day1ex4sets', 
            'day1ex4reps', 
            'day2ex1', 
            'day2ex1sets', 
            'day2ex1reps', 
            'day2ex2', 
            'day2ex2reps', 
            'day2ex2sets', 
            'day2ex3', 
            'day2ex3sets', 
            'day2ex3reps', 
            'day2ex4', 
            'day2ex4sets', 
            'day2ex4reps', 
            'day3ex1', 
            'day3ex1sets', 
            'day3ex1reps', 
            'day3ex2', 
            'day3ex2reps', 
            'day3ex2sets', 
            'day3ex3', 
            'day3ex3sets', 
            'day3ex3reps', 
            'day3ex4', 
            'day3ex4sets', 
            'day3ex4reps'
        )