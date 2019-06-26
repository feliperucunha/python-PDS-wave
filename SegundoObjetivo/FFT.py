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


fig, ax = plt.subplots(2, 1)
ax[0].plot(sig)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(sigFFT),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
plt.show()