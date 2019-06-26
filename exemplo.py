import librosa
import matplotlib.pyplot as plt
import librosa.display
import  numpy as np

# Carregar Sinal de Audio .wav 1
sig, sr = librosa.load(r'/home/damasceno/Documents/College/UFPA/5st Semester/Digital Signal Processing/Task/Codes/Filter-Project/Data/Voz01_16KHz.wav', duration=8.0)
#ipd.Audio(sig, rate=sr)
print ("Taxa de amostragem Sinal 1: ", sr)
print ("Numero de amostras Sinal 1: ", sig.shape)

Fs = 16000
n = np.arange(0, 8, 1/Fs)

# Plotar sinal de audio 1
plt.rcParams['font.family'] = ['DejaVu Sans']
plt.figure(figsize=(12, 4))
librosa.display.waveplot(sig, sr=sr)
plt.title('Sinal 1')
plt.show()

# Sinal Portadora de transmissão
Fc = 6
Ac = 3
carrier = Ac*np.cos(2*np.pi*Fc*n)
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora')
plt.plot(n, carrier)
plt.show()

# Modulação Sinal original com portadora
s = carrier * sig
plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Sinal Modulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#   Graficos de espectros
plt.subplot(2, 1, 1)
plt.magnitude_spectrum(s, Fs=Fs, color='C1')
plt.title('Espectros do Sinal Modulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.phase_spectrum(s, Fs=Fs, color='C2')
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()

# Demodulação do sinal
fa = 10
h = s * np.cos(2*np.pi*fa*n)
plt.figure(figsize=(12, 4))
plt.plot(n, h)
plt.title('Sinal Demodulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Graficos de espectros
plt.subplot(2, 1, 1)
plt.magnitude_spectrum(h, Fs=Fs, color='C1')
plt.title('Espectros do Sinal Demodulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.phase_spectrum(h, Fs=Fs, color='C2')
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()

# Carregar Sinal de Audio .wav 2
sig2, sr2 = librosa.load(r'/home/damasceno/Documents/College/UFPA/5st Semester/Digital Signal Processing/Task/Codes/Filter-Project/Data/Voz02_16KHz.wav', duration=8.0)
#ipd.Audio(sig2, rate=sr2)
print ("Taxa de amostragem Sinal 2: ", sr2)
print ("Numero de amostras Sinal 2: ", sig2.shape)

# Plotar sinal de audio 2
plt.rcParams['font.family'] = ['DejaVu Sans']
plt.figure(figsize=(12, 4))
librosa.display.waveplot(sig2, sr=sr2)
plt.title('Sinal 2')
plt.show()

# Sinal Portadora de transmissão
Fc = 6
Ac = 3
carrier = Ac*np.cos(2*np.pi*Fc*n)
plt.figure(figsize=(12, 4))
plt.title('Sinal Portadora')
plt.plot(n, carrier)
plt.show()

# Modulação Sinal original com portadora
s = carrier * sig2
plt.figure(figsize=(12, 4))
plt.plot(n, s)
plt.title('Sinal Modulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

#   Graficos de espectros
plt.subplot(2, 1, 1)
plt.magnitude_spectrum(s, Fs=Fs, color='C1')
plt.title('Espectros do Sinal Modulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.phase_spectrum(s, Fs=Fs, color='C2')
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()

# Demodulação do sinal
fa = 10
h = s * np.cos(2*np.pi*fa*n)
plt.figure(figsize=(12, 4))
plt.plot(n, h)
plt.title('Sinal Demodulado')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Graficos de espectros
plt.subplot(2, 1, 1)
plt.magnitude_spectrum(h, Fs=Fs, color='C1')
plt.title('Espectros do Sinal Demodulado')
plt.ylabel("Magnitude")
plt.xlabel('Frequência (Hz)')
plt.subplot(2, 1, 2)
plt.phase_spectrum(h, Fs=Fs, color='C2')
plt.xlabel('Frequência (Hz)')
plt.ylabel("Fase")
plt.tight_layout()
plt.show()

# # Gerar arquivos de audio .wav
# librosa.output.write_wav('/home/damasceno/Documents/College/UFPA/5st Semester/Digital Signal Processing/Task/FIles/Saida_Voz01_16KHz.wav', sig, sr)
# #ipd.Audio(sig, rate=sr)
# librosa.output.write_wav('/home/damasceno/Documents/College/UFPA/5st Semester/Digital Signal Processing/Task/FIles/Saida_Voz02_16KHz.wav', sig2, sr2)
# #ipd.Audio(sig2, rate=sr2)