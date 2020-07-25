#Django
from django.shortcuts import render

# Django Rest Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
#Serializer
from .serializers.users import UserRegisterSerializer,UserModelSerializer,UserLoginSerializer

#model 
from .models import User


class UserViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login',]:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user,token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data, 
            'access_token': token

        }
        return Response(data, status=status.HTTP_201_CREATED)
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserRegisterSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
    @action(detail=False, methods=['get'])
    def listUser(self, request):
        data= {
            'nombre' : 'Lisa',
            'apellido': 'simpsom'
        }
        return Response(data, status=status.HTTP_200_OK)
       
     
