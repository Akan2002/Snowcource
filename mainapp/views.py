from mainapp.models import (
    Category, CourseSchedule, Course, LearningTechnology, Client, Publication, Comment
)
from mainapp.serializers import (
    CategorySerializer, CourseSerializer, CourseScheduleSerializer, LearningTechnologySerializer, ClientSerializer, RegistrationSerializer, AuthorizationSerializer, PublicationSerializer, CommentSerializer
)
from mainapp.send_mail import send_msg

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

User=get_user_model()

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()                   
    serializer_class = CategorySerializer


class CourseView(ModelViewSet):
    queryset = Course.objects.all()                   
    serializer_class = CourseSerializer


class CourseScheduleView(ModelViewSet):
    queryset = CourseSchedule.objects.all()                   
    serializer_class = CourseScheduleSerializer


class LearningTechnologyView(ModelViewSet):
    queryset = LearningTechnology.objects.all()                   
    serializer_class = LearningTechnologySerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()                   
    serializer_class = CommentSerializer


class PublicationView(ModelViewSet):
    queryset = Publication.objects.all()                   
    serializer_class = PublicationSerializer


class ClientView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class RegistrationView(APIView):
    def post(self,request):
        serializer= RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data


        username= data.get('username')
        email=data.get('email')
        password=data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'message':'User with such name is already exists'})
        user= User.objects.create_user(
            username=username,
            email=email,
            password=password

        )
        send_msg(email=email,username=username)
        token=Token.objects.create(user=user)
        return Response({'token':token.key})

class AuthorizationView(APIView):
    def post(self, requset):
        serializer=AuthorizationSerializer
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        
        
        username=data.get('username')
        password=data.get('password')
        user= User.objects.filter(username=username).first()
        
        if user is not None:
            if check_password(password, user.password):
                token,_=Token.objects.get_or_create(user=user)
                return Response({'token:':token.key})
            return Response ({'error':'Password is not valid'}, status=400)
        return Response({'error':'This username is not registred'},status=400)


# {
#   "username" : "akan",
#   "password" : "12345678",
#   "email" : "akanaydaraliev2002@gmail.com"
# }