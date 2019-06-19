import sys
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import time, sys
from pygame import mixer




def to_mono(fname, channel=0):

    (freq, sig) = wav.read(fname)
    if sig.ndim == 2:
        return (sig[:,channel], freq)
    return (sig, freq)


def cut(data, freq, start, end):

    end = int(end*freq)
    if end > len(data):
        return data[int(start*freq):]
    return data[int(start*freq):end]


def seconds(data, freq):

    return len(data)/freq


def process(data, callback=None):

    if not callback:
        def callback(t):
            return t
    output = np.empty(shape=[len(data)], dtype=np.int16)
    for i in xrange(0, len(data)):
        output.put(i, callback(data[i]))
    return output




def save(filename, data, freq):

    wav.write(filename=filename, rate=freq, data=data)




def spectrogram(data, freq, NFFT=256, noverlap=128, mode='psd', sides='default'):

    sec = seconds(data, freq)
    xtick = np.linspace(0, sec, num=len(data))
    ax1 = plt.subplot(211)
    plt.plot(xtick,data)
    plt.subplot(212, sharex=ax1)
    spec, f, t, i = plt.specgram(data, NFFT=NFFT, Fs=freq, noverlap=noverlap, mode=mode, sides=sides)
    return (plt, spec, f, t, i)


if __name__ == '__main__':
    print("O audio selecionado será reproduzido.")
    print("Spectograma do audio será plotado ex. python audio.py test.wav")
    if len(sys.argv) == 2:
        mixer.init()
        sound = mixer.Sound(sys.argv[1])
        sound.play()
        time.sleep(1)        
        spectrogram(*to_mono(sys.argv[1]))[0].show()


