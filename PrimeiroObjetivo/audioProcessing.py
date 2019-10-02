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

(freq,sig) = wav.read(address) # Loads up the desired audio

mixer.init()
sound = mixer.Sound(address)
sound.play()
time.sleep(5)
plt.plot(sig)
plt.show()

