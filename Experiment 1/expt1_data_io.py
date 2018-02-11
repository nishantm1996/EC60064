
import matplotlib.pyplot as plt
import scipy.io as spio

# Question 1 - Sample code for loading noisy ecg data into python and plotting

mat = spio.loadmat('data_ecg_noisy.mat', squeeze_me=True)
noisy_ecg = mat['ecg_noisy'] # ecg data with powerline noise (array)
fsample = mat['fs'] # sampling frequency (scalar)

plt.plot(noisy_ecg[0:999]) # Plot first 1000 samples
plt.ylabel('Corrupted ECG')
plt.xlabel('Sample index')
plt.show()

# Question 2 - Sample code for loading original ecg data into python and plotting

mat = spio.loadmat('data_ecg_original.mat', squeeze_me=True)
input_ecg = mat['ecg_original'] # ecg data (array)
fsample = mat['fs'] # sampling frequency (scalar)

plt.plot(input_ecg[0:999]) # Plot first 1000 samples
plt.ylabel('Original ECG')
plt.xlabel('Sample index')
plt.show()

# Question 2 - save an array in .mat format (to save ecg corrupted with white 
# noise stored in variable 'ecg_noisy_wgn'), use the following:
    
# spio.savemat('data_ecg_noisy_wgn.mat',mdict={'ecg_noisy_wgn': ecg_noisy_wgn,'fs':fsample})







