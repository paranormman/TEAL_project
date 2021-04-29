from django.urls import path
from . import views


urlpatterns =[
    path('', views.Home.as_view(), name = "Home"),
    path('index/', views.index, name = "Index"),
    path('upload/', views.upload_csv, name = "Upload"),
    
    path('fftdata/', views.fftdata, name = "FFTdata"),
    path('upload_withouttime/', views.upload_withouttime, name = "Upload_withouttime"),
    path('upload_csv/', views.upload_csv, name = "Upload_csv"),
]

