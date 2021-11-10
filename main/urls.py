from django.urls import path
from.import views
from . views import Delete, Tasklist, getemail

urlpatterns = [
path('',views.index,name='index'),
path('data',views.data,name='data'),
path('remove/<task_id>',views.remove,name='remove'),
path('Tasklist/',Tasklist.as_view()),
path('Delete/<int:pk>',Delete.as_view()),
path('getemail/<str:pk>',getemail.as_view())

    
]
