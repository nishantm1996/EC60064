import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio
import math as math

fs = 100.0
ny = 0.5*fs

eeg2c4 = np.loadtxt('Data\eeg2-c4.dat', delimiter = ',')
# ind = np.arange(eeg2c4.size)
# t = ind*(1/fs)
plt.subplot(11,1,1)
plt.plot(eeg2c4)
plt.ylabel('Ref c4')
plt.grid(True)

eeg2c3 = np.loadtxt('Data\eeg2-c3.dat', delimiter = ',')
eeg2f3 = np.loadtxt('Data\eeg2-f3.dat', delimiter = ',')
eeg2f4 = np.loadtxt('Data\eeg2-f4.dat', delimiter = ',')
eeg2o1 = np.loadtxt('Data\eeg2-o1.dat', delimiter = ',')
eeg2o2 = np.loadtxt('Data\eeg2-o2.dat', delimiter = ',')
eeg2p3 = np.loadtxt('Data\eeg2-p3.dat', delimiter = ',')
eeg2p4 = np.loadtxt('Data\eeg2-p4.dat', delimiter = ',')
eeg2t3 = np.loadtxt('Data\eeg2-t3.dat', delimiter = ',')
eeg2t4 = np.loadtxt('Data\eeg2-t4.dat', delimiter = ',')

rf = eeg2c4[120:146]-np.mean(eeg2c4[120:146])
lnrf = len(rf)

corr_c3 = []
det_c3 = []
corr_c4 = []
det_c4 = []

corr_f3 = []
det_f3 = []
corr_f4 = []
det_f4 = []

corr_o1 = []
det_o1 = []
corr_o2 = []
det_o2 = []

corr_p3 = []
det_p3 = []
corr_p4 = []
det_p4 = []

corr_t3 = []
det_t3 = []
corr_t4 = []
det_t4 = []


for i in range(len(eeg2c3)-lnrf):
  
  tmp_c3 = eeg2c3[i:i+lnrf]-np.mean(eeg2c3[i:i+lnrf])
  tmp_c4 = eeg2c4[i:i+lnrf]-np.mean(eeg2c4[i:i+lnrf])
  a_crr_c3 = np.dot(tmp_c3,rf)/math.sqrt(np.dot(tmp_c3,tmp_c3)*np.dot(rf,rf))
  a_crr_c4 = np.dot(tmp_c4,rf)/math.sqrt(np.dot(tmp_c4,tmp_c4)*np.dot(rf,rf))
  corr_c3.append(a_crr_c3)
  corr_c4.append(a_crr_c4)
  det_c3.append(a_crr_c3 > 0.5)
  det_c4.append(a_crr_c4 > 0.5)
  
  tmp_f3 = eeg2f3[i:i+lnrf]-np.mean(eeg2f3[i:i+lnrf])
  tmp_f4 = eeg2f4[i:i+lnrf]-np.mean(eeg2f4[i:i+lnrf])
  a_crr_f3 = np.dot(tmp_f3,rf)/math.sqrt(np.dot(tmp_f3,tmp_f3)*np.dot(rf,rf))
  a_crr_f4 = np.dot(tmp_f4,rf)/math.sqrt(np.dot(tmp_f4,tmp_f4)*np.dot(rf,rf))
  corr_f3.append(a_crr_f3)
  corr_f4.append(a_crr_f4)
  det_f3.append(a_crr_f3 > 0.5)
  det_f4.append(a_crr_f4 > 0.5)
  
  tmp_o1 = eeg2o1[i:i+lnrf]-np.mean(eeg2o1[i:i+lnrf])
  tmp_o2 = eeg2o2[i:i+lnrf]-np.mean(eeg2o2[i:i+lnrf])
  a_crr_o1 = np.dot(tmp_o1,rf)/math.sqrt(np.dot(tmp_o1,tmp_o1)*np.dot(rf,rf))
  a_crr_o2 = np.dot(tmp_o2,rf)/math.sqrt(np.dot(tmp_o2,tmp_o2)*np.dot(rf,rf))
  corr_o1.append(a_crr_o1)
  corr_o2.append(a_crr_o2)
  det_o1.append(a_crr_o1 > 0.5)
  det_o2.append(a_crr_o2 > 0.5)
  
  tmp_p3 = eeg2p3[i:i+lnrf]-np.mean(eeg2p3[i:i+lnrf])
  tmp_p4 = eeg2p4[i:i+lnrf]-np.mean(eeg2p4[i:i+lnrf])
  a_crr_p3 = np.dot(tmp_p3,rf)/math.sqrt(np.dot(tmp_p3,tmp_p3)*np.dot(rf,rf))
  a_crr_p4 = np.dot(tmp_p4,rf)/math.sqrt(np.dot(tmp_p4,tmp_p4)*np.dot(rf,rf))
  corr_p3.append(a_crr_p3)
  corr_p4.append(a_crr_p4)
  det_p3.append(a_crr_p3 > 0.5)
  det_p4.append(a_crr_p4 > 0.5)
  
  tmp_t3 = eeg2t3[i:i+lnrf]-np.mean(eeg2t3[i:i+lnrf])
  tmp_t4 = eeg2t4[i:i+lnrf]-np.mean(eeg2t4[i:i+lnrf])
  a_crr_t3 = np.dot(tmp_t3,rf)/math.sqrt(np.dot(tmp_t3,tmp_t3)*np.dot(rf,rf))
  a_crr_t4 = np.dot(tmp_t4,rf)/math.sqrt(np.dot(tmp_t4,tmp_t4)*np.dot(rf,rf))
  corr_t3.append(a_crr_t3)
  corr_t4.append(a_crr_t4)
  det_t3.append(a_crr_t3 > 0.5)
  det_t4.append(a_crr_t4 > 0.5)

plt.subplot(11,1,2)
plt.plot(corr_c3)
plt.plot(det_c3)
plt.ylabel('Corr c3')
plt.grid(True)

plt.subplot(11,1,3)
plt.plot(corr_c4)
plt.plot(det_c4)
plt.ylabel('Corr c4')
plt.grid(True)

plt.subplot(11,1,4)
plt.plot(corr_f3)
plt.plot(det_f3)
plt.ylabel('Corr f3')
plt.grid(True)

plt.subplot(11,1,5)
plt.plot(corr_f4)
plt.plot(det_f4)
plt.ylabel('Corr f4')
plt.grid(True)

plt.subplot(11,1,6)
plt.plot(corr_o1)
plt.plot(det_o1)
plt.ylabel('Corr o1')
plt.grid(True)

plt.subplot(11,1,7)
plt.plot(corr_o2)
plt.plot(det_o2)
plt.ylabel('Corr o2')
plt.grid(True)

plt.subplot(11,1,8)
plt.plot(corr_p3)
plt.plot(det_p3)
plt.ylabel('Corr p3')
plt.grid(True)

plt.subplot(11,1,9)
plt.plot(corr_p4)
plt.plot(det_p4)
plt.ylabel('Corr p4')
plt.grid(True)

plt.subplot(11,1,10)
plt.plot(corr_t3)
plt.plot(det_t3)
plt.ylabel('Corr t3')
plt.grid(True)

plt.subplot(11,1,11)
plt.plot(corr_t4)
plt.plot(det_t4)
plt.grid(True)
plt.ylabel('Corr t4')

plt.show()







