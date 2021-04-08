from django.conf.urls import url
from . views import FileView


urlpatterns = [
    url(r'^upload/$', FileView.as_view(), name='file_upload'),
    # url(r'^calculate/$', calculations.as_view(), name='calculation'),
]