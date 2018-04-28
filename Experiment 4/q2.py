import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

mat = spio.loadmat('..\Data\emg_dog2.mat', squeeze_me=True)
emg = mat['emg'] 
fs = mat['fs1']

mat = spio.loadmat('..\Data\emg_dog2_flo.mat', squeeze_me=True)
input_flow = mat['flow'] # inspiratory airflow measured with a pneumo-tachograph, in liters/second
fsample_flow = 1000; # sampling frequency (scalar) equals 1000Hz

def rms(x):
  y = 0
  for i in range(len(x)):
    y += x[i]*x[i]
  return np.sqrt(y)  
  
def tc(x, th):
  y = 0
  for i in range(len(x)-1):
    if (((x[i+1] < x[i]) and (x[i-1] > x[i])) or ((x[i+1] > x[i]) and (x[i-1] < x[i]))):
      y += 1    
  if (y < th):
    y = 0
  return y

def slw_func(wl, th):
  emg_rms = np.zeros(len(emg)-wl)
  for i in range(len(emg)-wl):
    emg_rms[i] = rms(emg[i:i+wl])
  
  emg_tc = np.zeros(len(emg)-wl)
  for i in range(len(emg)-wl):
    emg_tc[i] = tc(emg[i:i+wl], th)  
  
  plt.figure
  plt.subplot(4,1,1)
  plt.plot(emg, 'b')
  plt.grid(True) 
  plt.subplot(4,1,2)
  plt.plot(emg_rms, 'k')  
  plt.grid(True)  
  plt.subplot(4,1,3)
  plt.plot(emg_tc, 'k')
  plt.grid(True)
  plt.subplot(4,1,4)
  plt.plot(input_flow, 'g')
  plt.grid(True)
  plt.show()

slw_func(500,100)  
slw_func(500,150)
slw_func(500,200)
slw_func(700,150)
slw_func(1000,150)

