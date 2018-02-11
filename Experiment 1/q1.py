import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

mat = spio.loadmat('data_ecg_noisy.mat', squeeze_me=True)
noisy_ecg = mat['ecg_noisy'] 
fsample = mat['fs'] 

r = float(raw_input("Enter radius for poles: "))

b = [1, -1, 1]
a = [1, -r, r*r]
w, h = signal.freqz(b, a)
f = w*180/np.pi
y = signal.filtfilt(b, a, noisy_ecg)

plt.figure
plt.title('Digital filter frequency response')
plt.plot(f, 20*np.log10(np.abs(h)), 'b')
plt.ylabel('Amplitude Response (dB)')
plt.xlabel('Frequency (rad/sample)')
plt.grid(True)
plt.show()

plt.figure
plt.plot(noisy_ecg[0:999], 'b')
plt.plot(y[0:999], 'k')
plt.legend(('Noisy Signal', 'Filtered Signal'), loc='best')
plt.grid(True)
plt.show()


