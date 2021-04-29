from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework import status
import requests
import json
import numpy as np
from rest_framework.views import APIView
from pymongo import MongoClient
#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer
# Create your views here.
from rest_framework.generics import CreateAPIView
from .serializers import ContactSerializer
import pandas as pd

class ContactCreateAPI(CreateAPIView):
    serializer_class = ContactSerializer

class Home(TemplateView):
	template_name = "csvrestapi/apihome.html"

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        csv_file=request.data
        return Response(data="hi",status=status.HTTP_200_OK)
    if request.method == 'POST':
        #serializer = SnippetSerializer(data=request.data)
        #csv_file = request.data.get("file")
        samplingfreq = int(request.data.get("frequency"))
        input_file_json = json.loads(request.data.get('input_file'))
        df_in_second_api = pd.read_json(input_file_json)
        #print(df_in_second_api)

        
        data1={"sampfreq":samplingfreq}

        # to calculate fft
        
        amplitude=df_in_second_api['amplitude']
        xCount=len(amplitude)
        values=np.arange(int(xCount/2))
        timePeriod=xCount/samplingfreq
        frequencies=values/timePeriod
        fourierTransform=np.fft.fft(amplitude)/xCount
        fourierTransform=fourierTransform[range(int(len(amplitude)/2))]
        a=frequencies.tolist()
        b=abs(fourierTransform).tolist()
        FFT_dict={"Frequencies":a,"Amplitude":b}
        #FFT_dict={"Frequencies":frequencies,"Amplitude":abs(fourierTransform)}
        #FFTZip = dict(zip(frequencies,abs(fourierTransform)))
        
        return JsonResponse(FFT_dict)
        #return HttpResponse(json.dumps(FFTZip))
        #return Response(data={responsedata},status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def upload_csv(request):
    if request.method == 'GET':
        csv_file=request.data
        return Response(data="hi",status=status.HTTP_200_OK)
    if request.method == 'POST':
        #serializer = SnippetSerializer(data=request.data)
        #csv_file = request.data.get("file")
        
        
        input_file_json = json.loads(request.data.get('input_file'))
        df_in_second_api = pd.read_json(input_file_json)
        
        # to calculate fft
        
        val = len(df_in_second_api['time'])
        num = df_in_second_api['time']. iloc[-1]
        sf = int((val/num)*1000)
        samplingFrequency = sf
        
        
        amplitude=df_in_second_api['amplitude']
        xCount=len(amplitude)
        values=np.arange(int(xCount/2))
        timePeriod=xCount/samplingFrequency
        frequencies=values/timePeriod
        fourierTransform=np.fft.fft(amplitude)/xCount
        fourierTransform=fourierTransform[range(int(len(amplitude)/2))]
        a=frequencies.tolist()
        b=abs(fourierTransform).tolist()
        FFT_dict={"Frequencies":a,"Amplitude":b}
        #FFT_dict={"Frequencies":frequencies,"Amplitude":abs(fourierTransform)}
        
        return JsonResponse(FFT_dict)
        #return HttpResponse(json.dumps(FFTZip))
        #return Response(data={responsedata},status=status.HTTP_200_OK)
