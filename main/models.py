from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Buying (models.Model):
    
    stock=models.CharField(max_length=1000)
    buyingprice=models.IntegerField()
    buyingdate=models.DateField()
    sellingprice=models.IntegerField()
    sellingdate=models.DateField()
    profit=models.IntegerField()
    loss=models.IntegerField()

    def __string__(self):
        return self.stock    


