""" Users serilizers """

# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator


# Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token


#models
from delivery.users.models import  User




class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number'
           
        )


class UserRegisterSerializer(serializers.Serializer):
    """ Register serializer """
    
    #email 
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
 

    # Phone number
    phone_regex = RegexValidator(regex = "^\+?[1-9]{1}[0-9]{3,14}$", message = "si contiene indicativo luego debe haber un numero,si no siempre debe empezar en numero positivo")

    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password2 = serializers.CharField(style={
        'input_type':'password'
    },write_only=True)
    
    
    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self,data):
        """ Verify passwords match """
        passwd = data['password']
        passwd2 = data['password2']

        if passwd != passwd2:
            raise serializers.ValidationError("las contraseñas no son iguales")
        password_validation.validate_password(passwd)
        return data

    def create(self,data):
        data.pop('password2')
        username = data['phone_number']
        user = User.objects.create_user(username,**data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=5, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key