from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class User(AbstractUser):
    username         =  None
    full_name        =  models.CharField(max_length=50)
    email            =  models.EmailField(unique=True)
    phone            =  models.CharField(max_length=15)
    is_verify        =  models.BooleanField(default=False)
    token            =  models.CharField(max_length=300, null=True, blank=True)
    otp              =  models.CharField(max_length=6, null=True, blank=True)
    two_factor       =  models.BooleanField(default=False, null=True, blank=True)
    pass_two_factor  =  models.BooleanField(default=False, null=True, blank=True)
    browser          =  models.CharField(max_length=200,null=True, blank=True)

    USERNAME_FIELD   =  'email'
    REQUIRED_FIELDS  =  ['first_name']
    objects          =  UserManager()