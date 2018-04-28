# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:09:04 2018

@author: User
"""
import scipy.io as sio
import matplotlib.pyplot as plt
# Loading neural network's output and target
pec = sio.loadmat('pec33.mat')
pec = pec['pec33'];

#x=pec[:,0]
#plt.plot(x)

plt.subplot(311)
plt.plot(pec[:,0])

plt.subplot(312)
plt.plot(pec[:,1])

plt.subplot(313)
plt.plot(pec[:,2])

