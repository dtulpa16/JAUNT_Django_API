from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','is_employee','age','calories','goal','height','weight','gender','experience')

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_employee=validated_data['is_employee'],
            age=validated_data['age'],
            goal=validated_data['goal'],
            height=validated_data['height'],
            weight=validated_data['weight'],
            gender=validated_data['gender'],
            experience=validated_data['experience'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
