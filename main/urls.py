from django.urls import path
from.import views
from . views import allstock,deletestock

urlpatterns = [
path('allstock/',allstock.as_view()),
path('deletestock/<int:pk>',deletestock.as_view())

    
]
