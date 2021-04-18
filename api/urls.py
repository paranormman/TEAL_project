from django.conf.urls import url
from . views import FileViewSet, calculations
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', FileViewSet.as_view)



# urlpatterns = [
#     url(r'^upload/$', FileView.as_view(), name='file_upload'),
#     url(r'^calculate/$', calculations.as_view(), name='calculation'),
# ]