import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio
import math as math

noisy_ecg = np.loadtxt('ecg_noisy.dat', delimiter = ',')
orig_ecg = np.loadtxt('ecg_orig.dat', delimiter = ',')
noise = noisy_ecg - orig_ecg

snr = 20*np.log10(np.linalg.norm(orig_ecg)/np.linalg.norm(noise))

fs = 360
ny = 0.5*fs

def fltr_func(fc, order):
  fc_norm = fc/ny
  b, a = signal.butter(order, fc_norm, 'high', analog=False)
  w, h = signal.freqz(b, a)
  y1 = signal.filtfilt(b, a, noisy_ecg)
  y1_s = signal.filtfilt(b, a, orig_ecg)
  y1_n = signal.filtfilt(b, a, noise)
  
  snr1 = 20*np.log10(np.linalg.norm(y1_s)/np.linalg.norm(y1_n))
    
  plt.plot(noisy_ecg[0:999]) 
  plt.plot(orig_ecg[0:999])
  plt.plot(y1[0:999])   
  plt.ylabel('ECG')
  plt.xlabel('Sample index')
  plt.legend(('Noisy Signal','Original Signal','Filtered Signal'), loc='best')  
  print(snr1)
  plt.grid(True)
  plt.show()
  
  plt.plot(0.5*fs*w/np.pi, 20 * np.log10(abs(h)))
  plt.xscale('log')
  plt.title('Butterworth filter frequency response')
  plt.xlabel('Frequency [Hz]')
  plt.ylabel('Amplitude [dB]')
  plt.margins(0, 0.1)
  plt.grid(which='both', axis='both')
  plt.axvline(fc, color='green')   
  plt.show() 
  
fc = float(raw_input("Enter Butterworth high pass filter cut-off frequency: "))
order = float(raw_input("Enter Butterworth high pass filter order: "))
fltr_func(fc,order)





