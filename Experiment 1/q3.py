import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio
import math as math

mat = spio.loadmat('data_ecg_original.mat', squeeze_me=True)
orig_ecg = mat['ecg_original'] 
fsample = mat['fs'] 

rnd_noise = (np.linalg.norm(orig_ecg)/math.sqrt(len(orig_ecg)))*np.random.normal(0,1,len(orig_ecg))

ecg_noisy_wgn = orig_ecg + rnd_noise
snr = 20*np.log10(np.linalg.norm(orig_ecg)/np.linalg.norm(rnd_noise))

fs = 360
ny = 0.5*fs

def fltr_func(fc, order):
  fc_norm = fc/ny
  b, a = signal.butter(order, fc_norm, 'low', analog=False)
  w, h = signal.freqz(b, a)
  y1 = signal.filtfilt(b, a, ecg_noisy_wgn)
  y1_s = signal.filtfilt(b, a, orig_ecg)
  y1_n = signal.filtfilt(b, a, rnd_noise)
  
  snr1 = 20*np.log10(np.linalg.norm(y1_s)/np.linalg.norm(y1_n))
  sdr1 = 20*np.log10(np.linalg.norm(orig_ecg)/np.linalg.norm(orig_ecg-y1_s))
    
  plt.plot(ecg_noisy_wgn[0:999]) 
  plt.plot(orig_ecg[0:999])
  plt.plot(y1[0:999])   
  plt.ylabel('ECG')
  plt.xlabel('Sample index')
  plt.legend(('Noisy Signal','Original Signal','Filtered Signal'), loc='best')  
  print(snr1-snr)
  print(sdr1)
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
  
fltr_func(10,8)
fltr_func(20,8)
fltr_func(40,8)
fltr_func(70,8)




