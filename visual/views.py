from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, request
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
import csv
import io
import urllib, base64
import matplotlib.pyplot as plt
from .models import SourceFile
from .forms import UploadFileForm

# Create your views here.

class Home(TemplateView):
    template_name = "visual/home.html"



def index(request):
    if request.method =="POST":
        file = request.FILES["file"]
        csv = pd.read_csv(file, error_bad_lines=False)
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
    else:
        return render (request,'visual/index.html')


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadFileForm()
    return render (request, 'visual/upload.html', {'form' : form})




    # context = {}
    # if request.method == 'POST':
    #     uploaded_file = request.FILES['file']
    #     fs = FileSystemStorage()
    #     name = fs.save(uploaded_file.name, uploaded_file)
    #     url = fs.url(name)
    #     context['url'] = fs.url(name)
    # return render (request, 'visual/upload.html', context)
