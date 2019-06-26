import sys
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import time, sys
from pygame import mixer

(freq,sig) = wav.read("c:/Users/DraKo/Documents/PDS/SegundoObjetivo/audio1.wav")
Fs = 31123.25
n = np.arange(0, 8, 1/Fs)
Fc =6
Ac = 3
carrier = Ac*np.cos(2*np.pi*Fc*n)
modulatedSig = carrier*sig
demodulatedSig = modulatedSig * Ac*np.cos(2*np.pi*3*n)
fig, ax = plt.subplots(3, 1)
ax[0].plot(n,sig)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(n,modulatedSig,'r') 
ax[1].set_xlabel('Carrier')
ax[2].plot(n,demodulatedSig)
ax[2].set_xlabel('Modulated Signal')
plt.show()
