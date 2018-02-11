import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio
import math as math

mat = spio.loadmat('data_ecg_original.mat', squeeze_me=True)
orig_ecg = mat['ecg_original'] 
fsample = mat['fs'] 

var = raw_input("Enter 0 for AWGN and 1 for power line noise: ")

if (var == '0'):
  rnd_noise = (np.linalg.norm(orig_ecg)/math.sqrt(len(orig_ecg)))*np.random.normal(0,1,len(orig_ecg))
if (var == '1'):
  rnd_noise = []
  for i in range(len(orig_ecg)):
    rnd_noise.append(0.1*np.sin(2*np.pi*60*i/fsample))
  
ecg_noisy_wgn = orig_ecg + rnd_noise
snr = 20*np.log10(np.linalg.norm(orig_ecg)/np.linalg.norm(rnd_noise))

rf = ecg_noisy_wgn[5158:5445]
lnrf = len(rf)
sync = np.zeros(lnrf)
sync_s = np.zeros(lnrf)
sync_n = np.zeros(lnrf)
count = 0

for i in range(len(ecg_noisy_wgn)-lnrf):
  tmp = ecg_noisy_wgn[i:i+lnrf]
  corr = np.dot(tmp,rf) 
  if (corr > 5):
    sync += ecg_noisy_wgn[i:i+lnrf]
    sync_s += orig_ecg[i:i+lnrf]
    sync_n += rnd_noise[i:i+lnrf]
    count += 1
for j in range(lnrf):
  sync[j] = sync[j]/count
  sync_s[j] = sync_s[j]/count
  sync_n[j] = sync_n[j]/count

snr0 = 20*np.log10(np.linalg.norm(sync_s)/np.linalg.norm(sync_n))

print(snr0-snr)    
print(10*np.log10(count))
plt.plot(sync) # Plot first 1000 samples
plt.plot(orig_ecg[5158:5445])
plt.plot(ecg_noisy_wgn[5158:5445])
plt.ylabel('ECG')
plt.xlabel('Sample index')
plt.legend(('Averaged Signal','Original Signal','Noisy Signal'), loc='best')
plt.show()

snr1 = []
def sync_no(cnt):
  rf = ecg_noisy_wgn[5158:5445]
  lnrf = len(rf)
  sync = np.zeros(lnrf)
  sync_s = np.zeros(lnrf)
  sync_n = np.zeros(lnrf)
  count = 0

  for i in range(len(ecg_noisy_wgn)-lnrf):
    tmp = ecg_noisy_wgn[i:i+lnrf]
    corr = np.dot(tmp,rf) 
    if (corr > 5):
      sync += ecg_noisy_wgn[i:i+lnrf]
      sync_s += orig_ecg[i:i+lnrf]
      sync_n += rnd_noise[i:i+lnrf]
      count += 1
      if (count == cnt):
        break
  for j in range(lnrf):
    sync[j] = sync[j]/count
    sync_s[j] = sync_s[j]/count
    sync_n[j] = sync_n[j]/count

  snr1.append(20*np.log10(np.linalg.norm(sync_s)/np.linalg.norm(sync_n))-snr)  

srt = []
for c in range(1,500):
  sync_no(c)
  srt.append(10*np.log10(c))
plt.plot(snr1)
plt.plot(srt)
plt.ylabel('SNR')
plt.xlabel('Number of beats used for averaging')
plt.show()

