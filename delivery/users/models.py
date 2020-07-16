from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import pre_save



class User(AbstractUser):
    """modelo de usuario
    Extiende de django abstract user
    ("https://github.com/django/django/blob/master/django/contrib/auth/models.py")
    donde cambiaremos el inicio de sesion a traves del email y agregaremos mas campos
     """
    username  = models.CharField('username',max_length= 14,null=True, blank= True)
    email = models.EmailField(
        'email',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese Email'
        },
    )
    phone_regex = RegexValidator(regex = "^\+?[1-9]{1}[0-9]{3,14}$", message = "si contiene indicativo luego debe haber un numero, y siempre debe empezar en numero positivo")
    phone_number = models.CharField('celular', validators=[phone_regex], unique=True, max_length=14, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','first_name', 'last_name', 'phone_number']  # valores minimos


def set_username(sender, instance, *args, **kwargs):  # callback
    if instance.phone_number and not instance.username:
        username = instance.phone_number
        instance.username = username


pre_save.connect(set_username, sender=User)