import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

noisy_ecg = np.loadtxt('ecg_noisy.dat', delimiter = ',')
orig_ecg = np.loadtxt('ecg_orig.dat', delimiter = ',')
noise = noisy_ecg - orig_ecg
fs = 360 

def flt_fnc(a,b):
  w, h = signal.freqz(b, a)
  f = w*180/np.pi
  y = signal.filtfilt(b, a, noisy_ecg)
  y_s = signal.filtfilt(b, a, orig_ecg)
  y_n = signal.filtfilt(b, a, noise)
  snr = 20*np.log10(np.linalg.norm(y_s)/np.linalg.norm(y_n))

  plt.figure
  plt.title('Digital filter frequency response')
  plt.plot(f, np.abs(h), 'b')
  plt.ylabel('Amplitude Response (dB)')
  plt.xlabel('Frequency (Hz)')
  plt.grid(True)
  plt.show()  

  plt.figure
  plt.plot(noisy_ecg[0:999], 'b')
  plt.plot(y[0:999], 'k')
  plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
  plt.grid(True)
  plt.show()
  
  print(snr)

b = [1, -1]
a = [1]

flt_fnc(a,b)

b = [1, 0, -1]
a = [2]

flt_fnc(a,b)

r = float(raw_input("Enter pole location: "))

b = [1, -1]
a = [1, -r]

flt_fnc(a,b)
