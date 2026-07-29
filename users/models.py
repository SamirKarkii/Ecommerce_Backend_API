from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser): 
    username = None #remove username 
    email = models.EmailField(unique=True) #unique customer identity 

    USERNAME_FIELD = "email" #Login using email #django teats as main identity
    REQUIRED_FIELDS = [] #NO extra createsuperuser fields



