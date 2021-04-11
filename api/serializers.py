from rest_framework import serializers
from . models import Files, SamplingFrequency

class FilesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Files
        fields = ('file', 'remark', 'timestamp',)

# Declaring sampling frequency field to get samplig frequency value 
# if time field is not present in the uploaded file

# class SampleSerializer(serializers.ModelSerializer):              
#     class Meta():
#         model = SamplingFrequency
#         fields = ('sampling frequency',)

