import numpy as np
import matplotlib.pyplot as plt

Fs1 = 100.0       # sampling frequency for signal in 'ecg_noisy.dat' and 'ecg_orig.dat'

x=np.loadtxt('eeg1-c3.dat',delimiter=',')

ind = np.arange(x.size)
t=ind*(1/Fs1)

plt.plot(t,x)
plt.ylabel('EEG Signal')
plt.xlabel('Time in sec')
plt.show()



