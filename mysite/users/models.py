from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.password_validation import CommonPasswordValidator


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='images', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [email]
