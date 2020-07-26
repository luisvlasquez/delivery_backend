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
from .serializers.restaurant import RestaurantSerializer

#model 
from .models import Restaurant

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

