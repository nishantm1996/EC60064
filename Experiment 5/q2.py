import numpy as np
import scipy.signal as signal
import scipy.stats as stats
import matplotlib.pyplot as plt
import scipy.io as spio

vg1 = np.loadtxt('..\Data\vag1.dat')
vg2 = np.loadtxt('..\Data\vag2.dat')
fs = 2e3
ny = 0.5*fs

# ind = np.arange(x.size)
# t = ind*(1/fs)
# plt.plot(t,x)
# plt.ylabel('EEG Signal')
# plt.xlabel('Time in sec')
# plt.grid(True)
# plt.show()

def prdgrm_func(x):
  f,Pxx = signal.periodogram(x,fs)
  plt.figure
  plt.semilogy(f,Pxx)
  plt.ylim([1e-9, 1e-3])
  plt.xlabel('Frequency [Hz]')
  plt.ylabel('PSD [V**2/Hz]')
  plt.grid(True)
  plt.show()
  return f,Pxx

f1,Pvg1 = prdgrm_func(vg1)
mpsd1 = np.dot(f1,Pvg1)/sum(Pvg1)
skew1 = stats.skew(Pvg1)
print(mpsd1,skew1)
f2,Pvg2 = prdgrm_func(vg2)
mpsd2 = np.dot(f2,Pvg2)/sum(Pvg2)
skew2 = stats.skew(Pvg2)
print(mpsd2,skew2)
