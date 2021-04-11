# # Python example - Fourier transform using numpy.fft method
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('E:\\Django_proj\\mysite\\media\\Acc_time.csv')
# length = 40960

# # How many time points are needed i,e., Sampling Frequency
# samplingFrequency  = length;

# # At what intervals time points are sampled
# samplingInterval       = 1 / samplingFrequency;

# # # Create subplot
# # figure, axis = plotter.subplots(4, 1)
# # plotter.subplots_adjust(hspace=1)

# # Time points
# time = df['time']
# amplitude = df['amplitude']

# # Frequency domain representation
# fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
# fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
# tpCount     = len(amplitude)
# values      = np.arange(int(tpCount/2))
# timePeriod  = tpCount/samplingFrequency
# frequencies = values/timePeriod

# # Frequency domain representation

# plt.title('Fourier transform depicting the frequency components')
# plt.plot(frequencies, abs(fourierTransform))
# plt.xlabel('Frequency')
# plt.ylabel('Amplitude')
# plt.show()



import csv
import pandas as pd
# import numpy as np

file = ("E:\\Django_proj\\mysite\\media\\media\\Acc_time.csv")
# csv = pd.read_csv(file)
csv = pd.read_csv(file, header=0, nrows=0).columns.tolist()
first = csv.index('time')
second = csv.index('amplitude')
# if first != 0:
#     print('yes')
print(first)


# time = len(csv[0])
# num = csv['time']. iloc[1]
# sf = int((time/num)*1000)
# print(sf)
# val = len(file.columns)
# print(time)



# def upload_csv(request):
#     data = {}
#     if "GET" == request.method:
#         return render(request, "myapp/upload_csv.html", data)
#     # if not GET, then proceed with processing
#     try:
#         csv_file = request.FILES["csv_file"]
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request,'File is not CSV type')
#             return HttpResponseRedirect(reverse("myapp:upload_csv"))
#     #if file is too large, return message
#         if csv_file.multiple_chunks():
#             messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
#             return HttpResponseRedirect(reverse("myapp:upload_csv"))
#             file_data = csv_file.read().decode("utf-8")          
#             lines = file_data.split("\n")
#     #loop over the lines and save them in db. If error shows up , store as string and then display
#             for line in lines:                                          
#                 fields = line.split(",")
#                 data_dict = {}
#                 data_dict["name"] = fields[0]
#                 data_dict["start_date_time"] = fields[1]
#                 data_dict["end_date_time"] = fields[2]
#                 data_dict["notes"] = fields[3]
#             try:
#                 form = EventsForm(data_dict)
#                 if form.is_valid():
#                     form.save()                                  
#                 else:
#                     logging.getLogger("error_logger").error(form.errors.as_json())                                                                                    
#             except Exception as e:
#                 logging.getLogger("error_logger").error(repr(e))                             
#                     pass

#         except Exception as e:
#             logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
#             messages.error(request,"Unable to upload CVS file. "+repr(e))

#             return HttpResponseRedirect(reverse("myapp:upload_csv"))
        