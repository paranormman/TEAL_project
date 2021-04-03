from rest_framework import serializers
from . models import Files, Atributes

class FilesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Files
        fields = ('file', 'remark', 'timestamp')

class Attributes(serializers.ModelSerializer):
    class Meta():
        model = Atributes
        fields = ('time', 'amplitude', 'sampling_frequency')
