from rest_framework import serializers
from .models import SourceFile


class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = SourceFile
    fields = ('file', 'remark',)