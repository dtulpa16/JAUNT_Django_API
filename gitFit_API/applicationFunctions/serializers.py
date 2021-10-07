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

class ClientTrailerSerializer(serializers.ModelSerializer):
    class Meta:
        Model = ClientTrainer
        fields = ['id', 'client','trainer']

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        Model = ClientTrainer
        fields = ['user', 'body']