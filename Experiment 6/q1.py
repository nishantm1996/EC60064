import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import scipy.io as spio
import math as math
from nitime import utils
from nitime import algorithms as alg

pec1 = np.loadtxt('..\Data\pec1.dat')
pec2 = np.loadtxt('..\Data\pec33.dat')
pec3 = np.loadtxt('..\Data\pec52.dat')
pcg1 = pec1[:,0]
pcg2 = pec2[:,0]
pcg3 = pec3[:,0]
ecg1 = pec1[:,1]
ecg2 = pec2[:,1]
ecg3 = pec3[:,1]
crt1 = pec1[:,2]
crt2 = pec2[:,2]
crt3 = pec3[:,2]

fs = 500.0

def pcg_func (pcg1):
  sys = pcg1[5123:5440]
  dia = pcg1[5440:6104]

  ws = 317
  hs = 10

  wd = 664
  hd = 10

  def armdl_func (sys,h,w):
    s = (h,w)
    x_c = np.zeros(s) 
   
    x_c[0] = sys;
    npts1 = w
    for i in np.arange(9):
      xi=x_c[i]
      c_e, sigma_e = alg.AR_est_YW(xi, 15)
      xo, _, _ = utils.ar_generator(N=npts1, sigma=sigma_e, coefs=c_e, drop_transients=45)
      x_c[i+1][:]=xo

    plt.figure  
    plt.plot(x_c[h-1], label='estimated process')
    plt.plot(sys, 'k', label='original process')
    plt.legend()
    err = x_c[h-1] - sys
    mse = np.dot(err, err) / w
    plt.title('MSE = %1.3e' % mse)
    plt.grid(True)
    plt.show()
  
    f_sys, Pxx_sys = signal.periodogram(x_c[h-1], fs)
    f_syswel, Pxx_syswel = signal.welch(sys,fs)
    plt.figure
    plt.semilogy(f_sys[1:],Pxx_sys[1:], label='estimated process')
    plt.semilogy(f_syswel[1:],Pxx_syswel[1:], 'k', label='original process')
    plt.legend()
    plt.title('PSD')
    plt.grid(True)
    plt.show()

  armdl_func(sys,hs,ws)
  armdl_func(dia,hd,wd)
  
pcg_func(pcg1)
pcg_func(pcg2)
pcg_func(pcg3)


