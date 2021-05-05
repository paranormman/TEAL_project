from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse
import logging
from django.contrib import messages
import requests
import pandas as pd
import numpy as np
import json

from .forms import csvwithouttime

# Create your views here.
api_url = "http://127.0.0.1:8000/csvrestapi/"
class Home(TemplateView):
	template_name = "csvapp/home.html"

def index(request):
	if request.method == "POST":
	#return HttpResponse()
		print("1")
	return render(request, "csvapp/index.html")
    #return render('template:index.html', {})
 
def upload_csv(request):
    
	data = {}
   
	if "GET" == request.method:
       
		return render(request, "csvapp/upload.html", data)
	if "POST" == request.method:
		csv_file = request.FILES['file1']
		
		

		if csv_file.name.endswith(".csv") != True:
			messages.error(request,'File is not CSV type')
			
			# return render(request, "csvapp/upload.html", data)
       

		csv=pd.read_csv(csv_file,error_bad_lines=False)
		col=csv.columns.tolist()
		n=len(col)
		if n == 0:
			messages.error(request,'No columns to parse')			
			return render(request, "csvapp/upload.html", data)
		if n != 2:
			messages.error(request,'File doesnt have either amplitude or time')			
			return render(request, "csvapp/upload.html", data)
		if col[0] != 'time' or col[1] != 'amplitude':
			messages.error(request,'File column names mismatch')			
			return render(request, "csvapp/upload.html", data)
		#try:
		print("inside")
		input_file1 = request.FILES.get(u'file1')
		if input_file1:
			#input_file_df1 = pd.read_csv(input_file1)
			df_json1 = json.dumps(csv.to_json(orient='records'))
		
		print(df_json1)
		url = api_url + "upload_csv/"
		payload = {"input_file":df_json1}
		url_response = requests.post(url, data = payload)
		fftdata1=url_response.json()
		print(fftdata1)

		return render(request, "csvapp/fftdata.html", {"fftdata":fftdata1})			




def upload_withouttime(request):
	data1 ={}
	if "GET" == request.method :
		print("uutrfvb")
        
		return render(request, "csvapp/upload.html", data1)

    # if not GET, then proceed
	#try:	
	data1={}
	CSVData = csvwithouttime(request.POST,request.FILES)
		
		
	csv_file = request.FILES['file']
		
	sampfreq1 = request.POST.get("sampfreq")
	
	sampfreq2=int(sampfreq1)
	

		

	#check if csv file or not
	if not csv_file.name.endswith('.csv'):
		print("not ending with .csv")
		messages.error(request,'File is not CSV type')
			
		return render(request, "csvapp/upload.html", data1)
	csv=pd.read_csv(csv_file,error_bad_lines=False) 
	col=csv.columns.tolist()
		
	n = len(col)

	if n == 0:
		messages.error(request,'No columns to parse')			
		return render(request, "csvapp/upload.html", data1)
		
	if n != 1:
		messages.error(request,'File has more than 1 column')			
		return render(request, "csvapp/upload.html", data1)

	if col[0] != 'amplitude':
		messages.error(request,'File column names mismatch')			
		return render(request, "csvapp/upload.html", data1)


	input_file = request.FILES.get(u'file')
	if input_file:
		#input_file_df = pd.read_csv(input_file)
		df_json = json.dumps(csv.to_json(orient='records'))
	sampfreq1 = int(request.POST.get("sampfreq"))

	print(sampfreq1)
	url = api_url + "test/"
	payload = {"input_file":df_json,"frequency":sampfreq1}
	url_response = requests.post(url, data = payload)
	fftdata1=url_response.json()
	fftdata2 = json.dumps(fftdata1)
	print(fftdata1)
        
	#messages.error(request,"fft plotted")
	return render(request, "csvapp/fftdata.html", {"fftdata":fftdata1})

        #return render (request, 'visual/index.html', {"something": True, "frequency": frequencies, "amplitude" : amplitude }, {'data':uri})
	# except Exception as e:
	# 	logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
	# 	messages.error(request,"Unable to upload file. "+repr(e))

	#return HttpResponseRedirect(reverse("csvapp:upload")) 
	#return render(request, "csvapp/upload.html", data1)


def fftdata(request):
	if request.method == "GET":
	#return HttpResponse()
		print("get fftdata")

		return render(request, "csvapp/fftdata.html")
    #return render('template:index.html', {})
 
	if request.method == "POST":
	#return HttpResponse()
		
		return render(request, "csvapp/fftdata.html")
    #return render('template:index.html', {})
 