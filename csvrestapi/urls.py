from django.urls import path
from django.contrib import admin
from . import views
from csvrestapi.views import index,upload_csv

urlpatterns = [
    
    #path('', views.Home.as_view(), name = "Home"),
    path('test/', index,name = 'index'),
    path('upload_csv/', upload_csv,name = 'upload_csv'),
    #path('test/<int:pk>/', getaccesstokenfftdata.as_view()),
   
]
