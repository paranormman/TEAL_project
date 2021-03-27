from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns =[
    path('', views.Home.as_view(), name = "Home"),
    path('index/', views.index, name = "Index"),
    path('upload/', views.upload, name = "Upload"),
    # path('fft/', views.add_data, name = "Upload"),
    # path('<str:time>/', views.get_data, name = "Upload"),
]

