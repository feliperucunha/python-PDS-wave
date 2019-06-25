import sys
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import time, sys
from pygame import mixer

(freq,sig) = wav.read(sys.argv[1])
mixer.init()
sound = mixer.Sound(sys.argv[1])
sound.play()
time.sleep(5)
plt.plot(sig)
plt.show()
