import sys
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

""" PROCESS DATA """


def to_mono(fname, channel=0):
    """
    Opens wav file and returns it as mono file if stereo
    :param fname: file name
    :param channel: channel index - default 0
    :return: tuple of frequency and data numpy array
    """
    (freq, sig) = wav.read(fname)
    if sig.ndim == 2:
        return (sig[:,channel], freq)
    return (sig, freq)


def cut(data, freq, start, end):
    """
    Cut track array from start (in seconds) to end (in seconds)
    or till end of track if end second is bigger then track length
    :param track: wav audio data
    :param start: start (in seconds)
    :param end: end (in seconds)
    :param freq: frequency of audio data
    :return:
    """
    end = int(end*freq)
    if end > len(data):
        return data[int(start*freq):]
    return data[int(start*freq):end]


def seconds(data, freq):
    """
    Returns number of seconds from track data based on frequency
    :param track: wav audio data
    :param freq: frequency of audio data
    :return: number of seconds
    """
    return len(data)/freq


def process(data, callback=None):
    """
    Can modify audio signal with callback function applied to every frame of data
    or simply return copy of the track if callback is None
    :param data: wav audio data
    :param callback: method to be invoked every step of track
    :return: copy of track with applied modifications
    """
    if not callback:
        def callback(t):
            return t
    output = np.empty(shape=[len(data)], dtype=np.int16)
    for i in xrange(0, len(data)):
        output.put(i, callback(data[i]))
    return output

""" FILE UTILS """


def save(filename, data, freq):
    """
    Wrapper for scipy.io.wavfile write method
    :param filename: name of wav file
    :param freq: frequency of audio data
    :param data: wav audio data
    """
    wav.write(filename=filename, rate=freq, data=data)

""" DRAW DATA """


def spectrogram(data, freq, NFFT=256, noverlap=128, mode='psd', sides='default'):
    """
    Draws spectrogram of audio file with audio file data using matplotlib specgram method
    minimal arguments are audio data and frequency
    :param data: wav audio data
    :param freq: see matplotlib.specgram Fs - here frequency of audio data
    :param NFFT: see matplotlib.specgram
    :param noverlap: see.matplotlib.specgram
    :param mode: see matplotlib.specgram
    :param sides: see matplotlib.specgram
    :return: see matplotlib.specgram - first parameter is matplotlib.pyplot
    """
    sec = seconds(data, freq)
    xtick = np.linspace(0, sec, num=len(data))
    ax1 = plt.subplot(211)
    plt.plot(xtick, data)
    plt.subplot(212, sharex=ax1)
    spec, f, t, i = plt.specgram(data, NFFT=NFFT, Fs=freq, noverlap=noverlap, mode=mode, sides=sides)
    return (plt, spec, f, t, i)


if __name__ == '__main__':
    print("Will draw spectrogram of given audio file ex. python audio.py test.wav")
    if len(sys.argv) == 2:
        spectrogram(*to_mono(sys.argv[1]))[0].show()
