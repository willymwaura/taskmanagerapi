from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Feature (models.Model):
    email=models.EmailField( max_length=254,default="user@gmail.com")
    task=models.CharField(max_length=100000)
    due_date=models.DateField()

    def __string__(self):
        return self.task
    


