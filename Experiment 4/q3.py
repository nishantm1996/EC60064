import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

mat = spio.loadmat('..\Data\safety_sound.mat', squeeze_me=True)
input_speech = mat['soundx'] # speech utterance
fsample = mat['fs']; # sampling rate of the 'safety' speech signal is 8000 Hz (male speaker)

dinput_speech = np.diff(input_speech)

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
  input_speech_rms = np.zeros(len(input_speech)-wl)
  for i in range(len(input_speech)-wl):
    input_speech_rms[i] = rms(input_speech[i:i+wl])
  
  input_speech_tc = np.zeros(len(input_speech)-wl)
  for i in range(len(input_speech)-wl):
    input_speech_tc[i] = tc(input_speech[i:i+wl], th)  
  
  plt.figure
  plt.subplot(3,1,1)
  plt.plot(input_speech, 'b')
  plt.grid(True) 
  plt.subplot(3,1,2)
  plt.plot(input_speech_rms, 'k')  
  plt.grid(True)  
  plt.subplot(3,1,3)
  plt.plot(input_speech_tc, 'k')
  plt.grid(True)  
  plt.show()
  
def dslw_func(wl, th):
  dinput_speech_rms = np.zeros(len(dinput_speech)-wl)
  for i in range(len(dinput_speech)-wl):
    dinput_speech_rms[i] = rms(dinput_speech[i:i+wl])
  
  dinput_speech_tc = np.zeros(len(dinput_speech)-wl)
  for i in range(len(dinput_speech)-wl):
    dinput_speech_tc[i] = tc(dinput_speech[i:i+wl], th)  
  
  plt.figure
  plt.subplot(3,1,1)
  plt.plot(dinput_speech, 'b')
  plt.grid(True) 
  plt.subplot(3,1,2)
  plt.plot(dinput_speech_rms, 'k')  
  plt.grid(True)  
  plt.subplot(3,1,3)
  plt.plot(dinput_speech_tc, 'k')
  plt.grid(True)  
  plt.show()

slw_func(500,100)
dslw_func(500,50)  