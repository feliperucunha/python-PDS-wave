import sys
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import time, sys
from pygame import mixer

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

(freq,sig) = wav.read("address")
Fs = freq
n = np.arange(0, 1/Fs, 1/Fs)
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
