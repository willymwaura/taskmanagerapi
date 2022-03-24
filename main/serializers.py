from django.db import models
from django.db.models import fields
from rest_framework import serializers
from.models import Buying

class BuyingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Buying
        fields="__all__"
class BuySerializer(serializers.ModelSerializer):

    class Meta:
        model=Buying
        fields=['id','stock','buyingprice','sellingprice','buyingdate','sellingdate']