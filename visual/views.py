from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
import csv
import json
from . models import FFT

# Create your views here.

class Home(TemplateView):
    template_name = "visual/home.html"

# df = pd.read_csv('E:\\Django_proj\\mysite\\media\\Acc_time.csv')
# results_list = []

# for i, row in df.iterrows():
#     result = (row['time']) * row['amplitude']
#     results_list.append(result)
# df['frequency'] = results_list
# print(df.head(3))

# def make_json(csvFilePath, jsonFilePath):
#     data = {}
#     with open(csvFilePath, encoding='utf-8') as csvf:
#         csvReader = csv.DictReader(csvf)

#         for rows in csvReader:

#             key = rows['No']
#             data[key] = rows

#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#         jsonf.write(json.dumps(data, indent=4))

# csvFilePath = r'E:\\Django_proj\\mysite\\media\\Acc_time.csv'
# jsonFilePath = r'E:\\Django_proj\\mysite\\media\\Acc_time.json'

# make_json(csvFilePath, jsonFilePath)



def index(request):
    if request.method =="POST":
        file = request.FILES["document"]
        csv = pd.read_csv(file)
        length = 40960
        samplingFrequency = length;
        samplingInterval = 1 / samplingFrequency;
        signal1Frequency     = 4;
        signal2Frequency     = 7;
        time = csv['time']
        amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
        amplitude2 = np.sin(2*np.pi*signal2Frequency*time)
        amplitude = amplitude1 + amplitude2
        fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
        fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
        tpCount     = len(amplitude)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/samplingFrequency
        frequencies = values/timePeriod

        return render (request, 'visual/index.html', {"something": True, "frequency": frequencies, "amplitude" : amplitude })
    else:
        return render (request,'visual/index.html')



# df = pd.read_csv('E:\\Django_proj\\mysite\\media\\Acc_time.csv')
# length = 40960
# print(length)
# # How many time points are needed i,e., Sampling Frequency
# samplingFrequency   = length;

# # At what intervals time points are sampled
# samplingInterval       = 1 / samplingFrequency;

# # # Begin time period of the signals
# # beginTime           = 0;

# # # End time period of the signals
# # endTime             = 10; 

# # Frequency of the signals
# signal1Frequency     = 4;
# signal2Frequency     = 7;

# # Time points
# time = df['time']

# # Create two sine waves
# amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
# amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

# # print amplitude
# print(time, amplitude1)

# # time and amplitude 2
# print(time, amplitude2)

# # Add the sine waves
# amplitude = amplitude1 + amplitude2

# # print the value of time and amplitude(sum)
# print(time, amplitude)

# # Frequency domain representation
# fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
# fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
# tpCount     = len(amplitude)
# values      = np.arange(int(tpCount/2))
# timePeriod  = tpCount/samplingFrequency
# frequencies = values/timePeriod
# # print values of amplitude and frequency

# print(amplitude, frequencies)

# def get_data(request, time):
#     if request.method == 'GET':
#         try:
#             ft = FFT.objects.get(name=time)
#             response = json.dumps([{ 'Time': ft.time, 'Amplitude': ft.amplitude}])
#         except:
#             response = json.dumps([{ 'Error': 'Enter the appropriate value'}])
#     return HttpResponse(response, content_type='text/json')

# @csrf_exempt
# def add_data(request):
#     # f = open('E:\\Django_proj\\mysite\\media\\Acc_time.json')
#     # ft = json.load(f)
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         time = payload['time']
#         amplitude = payload['top_speed']
#         ft = FFT(name=time, amplitude=amplitude)
#         try:
#             ft.save()
#             response = json.dumps([{ 'Success': 'data added successfully!'}])
#         except:
#             response = json.dumps([{ 'Error': 'data could not be added!'}])
#     return HttpResponse(response, content_type='text/json')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        
    return render (request, 'visual/upload.html', context)

