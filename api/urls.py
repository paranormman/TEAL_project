from django.conf.urls import url
from . views import FileView, calculations



urlpatterns = [
    url(r'^upload/$', FileView.as_view(), name='file_upload'),
    url(r'^calculate/$', calculations.as_view(), name='calculation'),
]