import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio

mat = spio.loadmat('..\Data\emg_dog2.mat', squeeze_me=True)
emg = mat['emg'] 
fs = mat['fs1'] 

mat = spio.loadmat('..\Data\emg_dog2_env.mat', squeeze_me=True)
env = mat['env'] 

ny = 0.5*fs

emg_hw = emg*(emg > 0)
emg_fw = abs(emg)

# plt.figure
# plt.plot(emg, 'b')
# plt.plot(emg_hw, 'k')
# plt.plot(emg_fw, 'g')
# plt.legend(('Original Signal', 'HW Rectified Signal','FW Rectified Signal'), loc='best')
# plt.grid(True)
# plt.show()

def fltr_func(fc, order):
  fc_norm = fc/ny
  b, a = signal.butter(order, fc_norm, 'low', analog=False)
  w, h = signal.freqz(b, a)
  y1_h = signal.lfilter(b, a, emg_hw)
  y1_f = signal.lfilter(b, a, emg_fw)
  
  plt.subplot(2,1,1)
  plt.plot(env)
  plt.ylabel('EMG')
  plt.xlabel('Sample index')
  plt.grid(which='both', axis='both')
  
  plt.subplot(2,1,2)  
  plt.plot(y1_h)
  plt.plot(y1_f)   
  plt.ylabel('EMG')
  plt.xlabel('Sample index')
  plt.grid(which='both', axis='both')
  plt.legend(('Filtered HW Signal','Filtered FW Signal'), loc='best')  
  plt.show()
  
  # plt.plot(0.5*fs*w/np.pi, 20 * np.log10(abs(h)))
  # plt.xscale('log')
  # plt.title('Butterworth filter frequency response')
  # plt.xlabel('Frequency [Hz]')
  # plt.ylabel('Amplitude [dB]')
  # plt.margins(0, 0.1)
  # plt.grid(which='both', axis='both')
  # plt.axvline(fc, color='green')   
  # plt.show() 
  
fltr_func(10,6)
fltr_func(12,6)
fltr_func(15,6)
fltr_func(17,6)
fltr_func(20,6)
