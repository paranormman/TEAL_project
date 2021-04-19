from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import status
import pandas as pd
import numpy as np
import csv
import io
import urllib, base64
import matplotlib.pyplot as plt
from .models import SourceFile
from .forms import UploadFileForm, SampleForm
from . validators import validate_file
from django.contrib import messages
from rest_framework.reverse import reverse
import logging
import os

# Create your views here.

class Home(TemplateView):
    template_name = "visual/home.html"



def index(request):
    if request.method =="POST":
        file = request.FILES.get('file', None)
        # name = os.path.splitext(file)
        ext = os.path.splitext(file.name)[1]
        valid_extentions = ['.csv']
        if ext.lower() in valid_extentions:
            try:
                csv = pd.read_csv(file)
                n = len(csv.columns.tolist())
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
                    plt.title('Fourier transform depicting the frequency components')
                    plt.plot(frequencies, abs(fourierTransform))
                    plt.xlabel('Frequency')
                    plt.ylabel('Amplitude')
                    plt.show()
                    fig = plt.fft()
                    buf = io.BytesIO()
                    fig.savefig(buf, format = 'png')
                    buf.seek(0)
                    string = base64.b64encode(buf.read())
                    uri = urllib.parse.quote(string)
                    return render (request, 'visual/index.html', {"something": True, "frequency": frequencies, "amplitude" : amplitude }, {'data':uri})
            except Exception as e:
                logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
                raise ValidationError("Unable to upload CVS file. "+repr(e))
        else:
            raise ValidationError("Unappropriate File type, Only .CSV can be uploaded")
    else:
        return render (request,'visual/index.html')


def upload(request):     
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_uploaded = form.save(commit=False)
            file = UploadFileForm()
            form.save()
            return redirect("<h1>Your csv file was uploaded</h1>")
    elif request.method == 'GET':
        form = UploadFileForm()
    return render (request, 'visual/upload.html', {'form' : form})


def sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("<h1>Data saved Successfully<h1>")
        elif request.method == 'GET':
            form = SampleForm()
        return render (request, 'visual/value.html', {'form' : form})
            




    # context = {}
    # if request.method == 'POST':
    #     uploaded_file = request.FILES['file']
    #     fs = FileSystemStorage()
    #     name = fs.save(uploaded_file.name, uploaded_file)
    #     url = fs.url(name)
    #     context['url'] = fs.url(name)
    # return render (request, 'visual/upload.html', context)