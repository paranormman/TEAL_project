# Python example - Fourier transform using numpy.fft method
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:\\Django_proj\\mysite\\media\\Acc_time.csv')
length = 40960

# How many time points are needed i,e., Sampling Frequency
samplingFrequency  = length;

# At what intervals time points are sampled
samplingInterval       = 1 / samplingFrequency;

# # Create subplot
# figure, axis = plotter.subplots(4, 1)
# plotter.subplots_adjust(hspace=1)

# Time points
time = df['time']
amplitude = df['amplitude']

# Frequency domain representation
fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

# Frequency domain representation

plt.title('Fourier transform depicting the frequency components')
plt.plot(frequencies, abs(fourierTransform))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()