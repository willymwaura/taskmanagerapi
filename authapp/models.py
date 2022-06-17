from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=12,unique=True)
    phone=models.CharField(max_length=12)
    REQUIRED_FIELDS=['email']
    def get_username(self):
        return self.email