from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
from rest_framework import serializers
from . models import Files

from .serializers import FilesSerializer

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):

        file_serializer = FilesSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class calculations(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format = 'csv'):
        up_file = request.Files['file']
        destinaton = open('E:/Django_proj/restapi/media/' + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destinaton.write(chunk)
        destinaton.close()
        csv = pd.read_csv(up_file)
        sf = 40960
        samplingFrequency = sf;
        samplingInterval = 1 / samplingFrequency;
        time = csv['time']
        amplitude = csv['amplitude']
        fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
        fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
        tpCount     = len(amplitude)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/samplingFrequency
        frequencies = values/timePeriod

        return Response({
            "Frequency": frequencies,
            "Amplitude": abs(fourierTransform)
        }, status = status.HTTP_201_CREATED)