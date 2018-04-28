import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

mat = spio.loadmat('..\Data\pec1.mat', squeeze_me=True)
pcg1 = mat['pcg'] # PCG signal
ecg1 = mat['ecg'] # ECG signal
car1 = mat['car'] # Cartoid pulse signal
fs1 = 1000; # sampling rate of the signals

mat = spio.loadmat('..\Data\pec33.mat', squeeze_me=True)
pcg2 = mat['pcg'] # PCG signal
ecg2 = mat['ecg'] # ECG signal
car2 = mat['car'] # Cartoid pulse signal
fs2 = 1000; # sampling rate of the signals

mat = spio.loadmat('..\Data\pec52.mat', squeeze_me=True)
pcg3 = mat['pcg'] # PCG signal
ecg3 = mat['ecg'] # ECG signal
car3 = mat['car'] # Cartoid pulse signal
fs3 = 1000; # sampling rate of the signals

def nvg(x):
  x_fft = np.fft.fft(x)
  x_fft[int(0.5*len(x))+1:] = 0
  for i in range(1,int(0.5*len(x))+1,1):
    x_fft[i] = 2*x_fft[i]
  x_rcv = np.fft.ifft(x_fft)
  nvgrm = abs(x_rcv)
  plt.figure
  plt.plot(nvgrm[2200:3154], 'b')
  plt.plot(x[2200:3154], 'g')
  plt.grid(True) 
  plt.show()
  return nvgrm

nvg1 = nvg(pcg1)  
nvg2 = nvg(pcg2)
nvg3 = nvg(pcg3)

def vg(nvg1, th):
  rf1 = nvg1[2200:3154]
  lnrf1 = len(rf1)
  sync1 = np.zeros(lnrf1)
  count = 0

  for i in range(len(nvg1)-lnrf1):
    tmp = nvg1[i:i+lnrf1]
    corr = np.dot(tmp,rf1) 
    if (corr > th):
      sync1 += nvg1[i:i+lnrf1]
      count += 1  
  sync1 = sync1/count      
  plt.figure  
  plt.subplot(2,1,1)
  plt.plot(sync1, 'g')
  plt.grid(True) 
  plt.subplot(2,1,2)
  plt.plot(nvg1[2200:3154], 'b')
  plt.grid(True) 
  plt.show()

vg(nvg1,200)
vg(nvg2,1000)
vg(nvg3,200)