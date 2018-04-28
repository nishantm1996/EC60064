
import matplotlib.pyplot as plt
import scipy.io as spio

# Questions 1 and 2 - Sample code for loading emg, envelope and flow signals

mat = spio.loadmat('emg_dog2.mat', squeeze_me=True)
input_emg = mat['emg'] # emg data in microvolts (array)
fsample = mat['fs1'] # sampling frequency (scalar) equals 10,000Hz

plt.plot(input_emg) # Plot EMG signal
plt.ylabel('EMG in microvolts')
plt.xlabel('Sample index')
plt.show()

mat = spio.loadmat('emg_dog2_env.mat', squeeze_me=True)
input_env = mat['env'] # envelope of EMG obtained using a full-wave rectifier and a modified Bessel filter
fsample_env = mat['fs2'] # sampling frequency (scalar) equals 1000Hz

plt.plot(input_env) # Plot envelope signal
plt.ylabel('Envelope')
plt.xlabel('Sample index')
plt.show()

mat = spio.loadmat('emg_dog2_flo.mat', squeeze_me=True)
input_flow = mat['flow'] # inspiratory airflow measured with a pneumo-tachograph, in liters/second
fsample_flow = 1000; # sampling frequency (scalar) equals 1000Hz

plt.plot(input_flow) # Plot flow signal
plt.ylabel('Inspiratory flow')
plt.xlabel('Sample index')
plt.show()

# Question 3 - sample code for loading 'safety' sound signal

mat = spio.loadmat('safety_sound.mat', squeeze_me=True)
input_speech = mat['soundx'] # speech utterance
fsample = mat['fs']; # sampling rate of the 'safety' speech signal is 8000 Hz (male speaker)

plt.plot(input_speech) # Plot speech signal
plt.ylabel('Amplitude')
plt.xlabel('Sample index')
plt.show()

# Question 4 - Load pec data; consists of PCG, ECG and cartoid pulse signals; shown for 'pec1.mat' - similar for others

mat = spio.loadmat('pec1.mat', squeeze_me=True)
input_pcg = mat['pcg'] # PCG signal
input_ecg = mat['ecg'] # ECG signal
input_car = mat['car'] # Cartoid pulse signal
fsample = 1000; # sampling rate of the signals

plt.plot(input_pcg) 
plt.ylabel('PCG')
plt.xlabel('Sample index')
plt.show()

plt.plot(input_ecg) 
plt.ylabel('ECG')
plt.xlabel('Sample index')
plt.show()

plt.plot(input_car) 
plt.ylabel('Cartoid pulse')
plt.xlabel('Sample index')
plt.show()

# Question 5 - sample code for loading ecg_pvc.mat

mat = spio.loadmat('ecg_pvc.mat', squeeze_me=True)
input_ecg = mat['ecg_pvc'] # ECG signal with PVC beats
fsample = mat['fs']; # sampling rate of ecg

plt.plot(input_ecg) 
plt.ylabel('ECG amplitude')
plt.xlabel('Sample index')
plt.show()            
             

