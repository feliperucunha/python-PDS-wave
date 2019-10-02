import sys
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import time, sys
from pygame import mixer
from numpy.fft import fft


def addressReader():
    address = input("Please, insert the name of the file, or the full path if it isn't on the same folder.")
    if address[1] == ':':
        final_address = address
    else:
        final_address = "./" + address # If the input isn't the full path to the file, it assumes to be in the same folder.
    
    if address[len(address)-2:] == ".wav": # Adds .wav in case it wasn't put in beforehand.
        final_address = final_address
    else:
        final_address = final_address + ".wav"

    return final_address

address = addressReader()

(freq,sig) = wav.read(address)
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
