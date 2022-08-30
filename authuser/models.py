from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=300)    
    role = models.CharField(max_length=30)
    isFirstTimeLogin = models.BooleanField(default=0)
    
    