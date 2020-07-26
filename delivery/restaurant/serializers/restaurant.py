
# Django
from django.conf import settings
from django.core.validators import RegexValidator


# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator



#models
from delivery.restaurant.models import  Restaurant,Menu,TypeMenu,Product

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'