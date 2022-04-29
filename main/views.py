from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Buying
from main.serializers import BuyingSerializer,BuySerializer
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.


<<<<<<< HEAD
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
@permission_classes ((IsAuthenticated,))
class Tasklist(APIView):
=======
class allstock(APIView):
>>>>>>> 1ccf01c2b0728803b05a5307707395259193fbc4
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



      
   
