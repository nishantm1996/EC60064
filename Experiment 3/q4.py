import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

pec1 = spio.loadmat('Data\pec1.mat')
pec1 = pec1['pec1']
pcg1 = pec1[:,0]
ecg1 = pec1[:,1]
crt1 = pec1[:,2]

pec2 = spio.loadmat('Data\pec33.mat')
pec2 = pec2['pec33']
pcg2 = pec2[:,0]
ecg2 = pec2[:,1]
crt2 = pec2[:,2]

pec3 = spio.loadmat('Data\pec52.mat')
pec3 = pec3['pec52']
pcg3 = pec3[:,0]
ecg3 = pec3[:,1]
crt3 = pec3[:,2]

fs = 1000.0

def pt(pcg,ecg,fs):
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
  
  t = []
  for i in np.arange(len(ecg)):
    t.append(i/fs)
  plt.figure
  plt.subplot(3,1,1)
  plt.plot(t,ecg,'b')
  plt.title('ECG Signal')
  plt.grid(True)
  plt.subplot(3,1,2)
  plt.plot(t,e5,'k')
  plt.title('Pan Tompkins Output')
  plt.grid(True)
  plt.subplot(3,1,3)
  plt.plot(t,pcg,'k')
  plt.title('PCG Signal')
  plt.grid(True)
  plt.show()

def lr(crt,fs):
  def flt_fnc(a,b,x):
    w, h = signal.freqz(b, a)
    f = w*180/np.pi
    y = signal.filtfilt(b, a, x)
    # plt.plot(x, 'b')
    # plt.plot(y, 'k')
    # plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
    # plt.grid(True)
    return y

  b1 = [2,-1,-2]
  a1 = [1]
  e1 = flt_fnc(a1,b1,crt)
  
  e2 = []
  for e in e1:
    e2.append(e*e)
  
  b2 = range(32,0,-1)
  a2 = [1]
  e3 = flt_fnc(a2,b2,e2)
  
  t = []
  for i in np.arange(len(crt)):
    t.append(i/fs)
  plt.figure
  plt.subplot(2,1,1)
  plt.plot(t,crt,'b')
  plt.title('Cartoid Signal')
  plt.grid(True)
  plt.subplot(2,1,2)
  plt.plot(t,e3,'k')
  plt.title('Lehner Rangayyan Output')
  plt.grid(True)
  plt.show()

# pt(pcg1,ecg1,fs)
lr(crt1,fs)
# pt(pcg2,ecg2,fs)
lr(crt2,fs)
# pt(pcg3,ecg3,fs)
lr(crt3,fs)
