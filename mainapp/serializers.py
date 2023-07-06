from rest_framework import serializers, exceptions

from mainapp.models import (
    Category, Course, Client, CourseSchedule, LearningTechnology, Comment, Publication
)

# from django.contrib.auth import get_user_model

# User = get_user_model()

class CourseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSchedule
        fields = (
            'id', 'course', 'start_date', 'end_date',
        )


class CourseSerializer(serializers.ModelSerializer):
    course_schedule = CourseScheduleSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = (
            'id', 'user', 'category', 'name', 'description', 'start_date', 
            'end_date', 'price', 'adress', 'additional_info', 'course_schedule'
        )


class CategorySerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'course',
        )


class LearningTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningTechnology
        fields = (
            'id', 'name'
        )


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id', 'username', 'name', 'surname', 'phone_number', 'email', 'password', 'links_to_ourses', 'role'
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

        
class RegistrationSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()
    email= serializers.CharField()
    def validate_password(self,value):
        if len(value) <8:
            raise exceptions.ValidationError('Password is too short')
        elif len (value) >24:
            raise exceptions.ValidationError ('Password is too long')
        return value

class AuthorizationSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()
