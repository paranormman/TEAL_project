from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
import pandas as pd
import numpy as np
from rest_framework import serializers
from . models import Files

from .serializers import FilesSerializer

class FileViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):

        file_serializer = FilesSerializer(data=request.data)
        if file_serializer.is_valid():  
            # try:                                                                      #getting sampling frequency value if not valid
            #     sampling_serializer = SampleSerializer(value = request.value)
            file_serializer.save()
            return Response(file_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class calculations(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format = 'csv'):
        up_file = request.Files['file']
        csv = pd.read_csv(up_file, error_bad_lines=False)
        n = len(up_file.columns.tolist())
        print(n)
        if n == 0:
           raise ValidationError(u'No Column to parse ')
        elif n == 1:
           raise ValidationError(u'No time value in the file ')
        elif n == 2:
           raise ValidationError(u'Missing amplitude value in the file')
        else:
            val = len(csv['time'])
            num = csv['time']. iloc[-1]
            sf = int((val/num)*1000)
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

