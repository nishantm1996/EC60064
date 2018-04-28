import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

x = np.linspace(0,4.999,5000)
y = np.cos(2*np.pi*50*x) + np.cos(2*np.pi*55*x)

fs = 1000
ny = 0.5*fs

# y_ps = np.abs(np.fft.fft(y))**2
# freqs = np.fft.fftfreq(y.size,1.0/fs)
# idx = np.argsort(freqs)
# plt.figure
# plt.plot(freqs[idx],y_ps[idx])
# plt.grid(True)
# plt.show()

def prdgrm_func(ns,wdw):    
  z = np.zeros(ns)
  fz,Pzz = signal.periodogram(z[:ns],fs,wdw)
  Pyy = np.zeros(fz.size)  
  for j in np.arange(y.size-ns):
    f,Pyy_t = signal.periodogram(y[j:j+ns],fs,wdw)
    Pyy += Pyy_t 
  return f,Pyy  

tm1 = 0.5
ns1 = int((tm1+1.0/fs)*fs)
tm2 = 2
ns2 = int((tm2+1.0/fs)*fs)

wdw1 = signal.get_window('boxcar',ns1)
f,Pyy = prdgrm_func(ns1,wdw1)
plt.figure
plt.semilogy(f,Pyy)
plt.ylim([1e-1, 1e4])
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.grid(True)
plt.show()

wdw2 = signal.get_window('boxcar',ns2)
f,Pyy = prdgrm_func(ns2,wdw2)
plt.figure
plt.semilogy(f,Pyy)
plt.ylim([1e-3, 1e4])
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.grid(True)
plt.show()

wdw3 = signal.get_window('hanning',ns1)
f,Pyy = prdgrm_func(ns1,wdw3)
plt.figure
plt.semilogy(f,Pyy)
plt.ylim([1e-7, 1e4])
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.grid(True)
plt.show()

wdw4 = signal.get_window('hanning',ns2)
f,Pyy = prdgrm_func(ns2,wdw4)
plt.figure
plt.semilogy(f,Pyy)
plt.ylim([1e-11, 1e4])
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.grid(True)
plt.show()