import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio
import math as math

noisy_ecg = np.loadtxt('ecg_hfn_ds.dat', delimiter = ',')
fs = 500   
y1 = signal.wiener(noisy_ecg)
snr = 10*np.log10(1/((np.linalg.norm(noisy_ecg)/np.linalg.norm(y1))*(np.linalg.norm(noisy_ecg)/np.linalg.norm(y1))-1))

plt.figure
plt.plot(noisy_ecg[0:999], 'b')
plt.plot(y1[0:999], 'k')
plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
plt.grid(True)
plt.show()
print(snr)

