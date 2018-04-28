import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

ecg3 = np.loadtxt('..\Data\ecg3.dat', delimiter = ',')
ecg5 = np.loadtxt('..\Data\ecg5.dat', delimiter = ',')
ecg6 = np.loadtxt('..\Data\ecg6.dat', delimiter = ',')
fs1 = 200.0 

ecg4 = np.loadtxt('..\Data\ecg4.dat', delimiter = ',')
fs2 = 360.0 

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
  strt = []
  nd = []
  mid = []
  for e in e5:
    e6.append(e > th)
  for i in np.arange(len(e6)-1):
    if (e6[i] == 0 and e6[i+1] == 1):
      strt.append(i/fs)
    elif (e6[i] == 1 and e6[i+1] == 0):
      nd.append((i+1)/fs)
  avg_hr = 60/((strt[-1]-strt[0])/(len(strt)-1))
  print(avg_hr)
  strt = strt[:min(len(strt),len(nd))]
  nd = nd[:min(len(strt),len(nd))]
  for j in np.arange(len(strt)):
    mid.append((nd[j]-strt[j])/2.0)
  avg_qs = np.mean(mid)
  print(avg_qs)
  
  t = []
  for i in np.arange(len(ecg)):
    t.append(i/fs)
  plt.figure
  plt.subplot(2,1,1)
  plt.plot(t,ecg,'b')
  plt.title('ECG Signal')
  plt.grid(True)
  plt.subplot(2,1,2)
  plt.plot(t,e5,'k')
  plt.title('Pan Tompkins Output')
  plt.grid(True)
  plt.show()

pt(ecg3,fs1,1000)
pt(ecg5,fs1,1000)
pt(ecg6,fs1,1000)
pt(ecg4,fs2,250)


