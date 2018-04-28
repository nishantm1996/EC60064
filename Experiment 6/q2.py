import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio
import math as math

e3 = np.loadtxt('..\Data\ECG3.dat')
e4 = np.loadtxt('..\Data\ECG4.dat')
e5 = np.loadtxt('..\Data\ECG5.dat')
e6 = np.loadtxt('..\Data\ECG6.dat')

fs = 200

def pt_qrs(input_ecg,fs,th):
  ecgx = input_ecg - np.mean(input_ecg)
  ecgx = ecgx/np.std(ecgx)
  pt(ecgx,fs,th)

def pt(ecg,fs,th):
  def flt_fnc(a,b,x):
    w, h = signal.freqz(b, a)
    f = w*180/np.pi
    y = signal.lfilter(b, a, x)
    # plt.plot(x, 'b')
    # plt.plot(y, 'k')
    # plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
    # plt.grid(True)
    return y

  b1 = [1,0,0,0,0,0,-2,0,0,0,0,0,1]
  a1 = [32,-64,32]
  e1 = flt_fnc(a1,b1,ecg)
  # plt.show()

  b2 = [-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,-32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
  a2 = [32,-32]
  e2 = flt_fnc(a2,b2,e1)
  # plt.show()

  b3 = [2,1,0,-1,-2]
  a3 = [8]
  e3 = flt_fnc(a3,b3,e2)
  # plt.show()

  def sq(arr):
    sqr = []
    for a in arr:
      sqr.append(a*a)
    return sqr

  e4 = sq(e3) 
  
  b5 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1]
  a5 = [32,-32]    
  e5 = flt_fnc(a5,b5,e4)
  e6 = []  
  for e in e5:
    e6.append(e > th)
  strt = []
  for i in np.arange(len(e6)-1):
    if (e6[i] == 0 and e6[i+1] == 1):
      strt.append(i/fs)
  avg_rr = ((strt[-1]-strt[0])/(len(strt)-1.0))
  avg_hr = 60.0/avg_rr
  print(avg_rr,avg_hr)
  
  plt.figure
  plt.subplot(2,1,1)
  plt.plot(ecg,'b')
  plt.title('ECG Signal')
  plt.grid(True)
  plt.subplot(2,1,2)
  plt.plot(e6,'k')
  plt.title('Pan Tompkins Output')
  plt.grid(True)
  plt.show()
  
  emid = e6 - np.mean(e6)
  e7 = emid/np.std(emid)
  
  f, Pxx = signal.welch(ecg, fs)
  f_pt, Pxx_pt = signal.welch(emid,fs)
  plt.figure
  plt.semilogy(f[1:],Pxx[1:], label='original ECG')
  plt.semilogy(f_pt[1:],Pxx_pt[1:], 'k', label='Pan Tompkins output')
  plt.legend()
  plt.title('Spectral Comparision')
  plt.grid(True)
  plt.show()

pt_qrs(e3,fs,0.03)
pt_qrs(e4,fs,0.02)
pt_qrs(e5,fs,0.01)
pt_qrs(e6,fs,0.01)

