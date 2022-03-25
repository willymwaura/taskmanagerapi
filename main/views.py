from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Buying
from main.serializers import BuyingSerializer,BuySerializer
from rest_framework.status import HTTP_204_NO_CONTENT

# Create your views here.


class allstock(APIView):
   def get(self,request):
      Tasklist=Buying.objects.all()
      serializers=BuyingSerializer(Tasklist,many=True)
      return Response(serializers.data)
   def post(self,request):
      serializer=BuySerializer(data=request.data)
      sp=request.data['sellingprice']
      bp=request.data['buyingprice']
      print(sp)
      if ( bp>sp):
         profit=0
         loss= bp-sp
      if (bp==sp):
         profit=0
         loss=0
      if (sp>bp):
         profit=sp-bp
         loss=0

      
      if serializer.is_valid():
         serializer.save(profit=profit,loss=loss)
         return Response(serializer.data)
      return HttpResponse("failed")
      
      


class deletestock(APIView):    
   def delete (self,request,pk):
      s=Buying.objects.get(id=pk)
      s.delete()
      return response.JsonResponse({'message': "delete successful"})



      
   
