import sys
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import time, sys
from pygame import mixer

(freq,sig) = wav.read("c:/Users/DraKo/Documents/PDS/SegundoObjetivo/audio1.wav")

mixer.init()
sound = mixer.Sound("c:/Users/DraKo/Documents/PDS/SegundoObjetivo/audio1.wav")
sound.play()
time.sleep(5)
plt.plot(sig)
plt.show()

