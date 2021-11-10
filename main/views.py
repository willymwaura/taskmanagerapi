from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from rest_framework import serializers,status
from.models import Feature
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Feature
from main.serializers import FeatureSerializer
from rest_framework.status import HTTP_204_NO_CONTENT

# Create your views here.
def index(request):
 
   queryset=Feature.objects.all()

   return render(request,"display.html",{"objectlist":queryset})

def data(request):
   b=request.GET['todo']
   
   c=request.GET['due_date']
   e=request.GET["email"]
   d=Feature(task=b,due_date=c,email=e)
   d.save()
   return redirect("index")

def remove(request, task_id):
   d=Feature.objects.get(pk=task_id)
   d.delete()
   return redirect("index")

class Tasklist(APIView):
   def get(self,request):
      Tasklist=Feature.objects.all()
      serializers=FeatureSerializer(Tasklist,many=True)
      return Response(serializers.data)
   def post(self,request):
      serializer=FeatureSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
class Delete(APIView):    
   def delete (self,request,pk):
      s=Feature.objects.get(id=pk)
      s.delete()
      return response.JsonResponse({'message': "delete successful"})

class getemail(APIView):
   def get(self,request,pk):
      s=Feature.objects.filter(email=pk)
      serializers=FeatureSerializer(s,many=True)
      return Response(serializers.data)
      
   
