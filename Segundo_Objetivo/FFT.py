import sys
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import time, sys
from pygame import mixer
from numpy.fft import fft

(freq,sig) = wav.read(sys.argv[1])
n = len(sig)
Fs = freq  # sampling rate
Ts = 1.0/Fs  # sampling interval
t = np.arange(0,1,Ts) # time vector
k = np.arange(n)
T = n/Fs
frq = k/T
frq = frq[range(n//2)]
sigFFT = fft(sig)/n
sigFFT = sigFFT[range(n//2)]
plt.plot(frq,abs(sigFFT),'r')
plt.show()