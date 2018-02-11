import numpy as np
import matplotlib.pyplot as plt

Fs1 = 360.0       # sampling frequency for signal in 'ecg_noisy.dat' and 'ecg_orig.dat'

x=np.loadtxt('ecg_noisy.dat',delimiter=',')

ind = np.arange(x.size)
t=ind*(1/Fs1)

plt.plot(t,x)
plt.ylabel('Corrupted ECG')
plt.xlabel('Time in sec')
plt.show()



x2=np.loadtxt('ecg_orig.dat',delimiter=',')

ind = np.arange(x2.size)
t2=ind*(1/Fs1)

plt.plot(t2,x2)
plt.ylabel('Corrupted ECG')
plt.xlabel('Time in sec')
plt.show()



Fs2 = 500.0         # sampling frequency for signal in 'ecg_hfn_ds.dat'
x3=np.loadtxt('ecg_hfn_ds.dat',delimiter=',')

ind = np.arange(x3.size)
t3=ind*(1/Fs2)

plt.plot(t3,x3)
plt.ylabel('Corrupted ECG')
plt.xlabel('Time in sec')
plt.show()
