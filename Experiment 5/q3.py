import numpy as np
import scipy.signal as signal
import scipy.stats as stats
import matplotlib.pyplot as plt
import scipy.io as spio

eeg1 = np.loadtxt('..\Data\eeg1-c4.dat')
eeg2 = np.loadtxt('..\Data\eeg1-f3.dat')
eeg3 = np.loadtxt('..\Data\eeg1-o1.dat')
eeg4 = np.loadtxt('..\Data\eeg1-p4.dat')
fs = 100.0
ny = 0.5*fs

# ind = np.arange(x.size)
# t = ind*(1/fs)
# plt.plot(t,x)
# plt.ylabel('EEG Signal')
# plt.xlabel('Time in sec')
# plt.grid(True)
# plt.show()

def prdgrm_w(eeg,ns,wdw):    
  z = np.zeros(ns)
  fz,Pzz = signal.welch(z[:ns],fs,wdw)
  Pyy = np.zeros(fz.size)  
  for j in np.arange(eeg.size-ns):
    f,Pyy_t = signal.welch(eeg[j:j+ns],fs,wdw)
    Pyy += Pyy_t 
  return f,Pyy  

tm1 = 0.5
ns1 = int((tm1+1.0/fs)*fs)
tm2 = 2
ns2 = int((tm2+1.0/fs)*fs)

def q3_w(eeg,ns,wstring):
  wdw = signal.get_window(wstring,ns)
  f,Pyy = prdgrm_w(eeg,ns,wdw)
  plt.figure
  plt.semilogy(f,Pyy)
  plt.ylim([1e-1, 1e10])
  plt.xlabel('Frequency [Hz]')
  plt.ylabel('PSD [V**2/Hz]')
  plt.grid(True)
  plt.show()  
  
def prdgrm_full(x):
  f,Pxx = signal.welch(x,fs)
  plt.figure
  plt.semilogy(f,Pxx)
  plt.xlabel('Frequency [Hz]')
  plt.ylabel('PSD [V**2/Hz]')
  plt.grid(True)
  plt.show()
  return f,Pxx

def q3_full(eeg):
  f,Pvg = prdgrm_full(eeg) 
  
q3_full(eeg1)
q3_full(eeg2)
q3_full(eeg3)
q3_full(eeg4)

q3_w(eeg1,ns1,'boxcar')
q3_w(eeg1,ns2,'boxcar')
q3_w(eeg1,ns1,'hanning')
q3_w(eeg1,ns2,'hanning')

q3_w(eeg2,ns1,'boxcar')
q3_w(eeg2,ns2,'boxcar')
q3_w(eeg2,ns1,'hanning')
q3_w(eeg2,ns2,'hanning')

q3_w(eeg3,ns1,'boxcar')
q3_w(eeg3,ns2,'boxcar')
q3_w(eeg3,ns1,'hanning')
q3_w(eeg3,ns2,'hanning')

q3_w(eeg4,ns1,'boxcar')
q3_w(eeg4,ns2,'boxcar')
q3_w(eeg4,ns1,'hanning')
q3_w(eeg4,ns2,'hanning')

