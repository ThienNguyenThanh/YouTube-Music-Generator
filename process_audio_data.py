
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# waveform
signal, sr = librosa.load("video1.wav")
librosa.display.waveshow(signal, sr=sr)

# plt.xlabel("Time")
# plt.ylabel("Amptitude")
# plt.show()


# fft (fast fourier transform)
fft = np.fft.fft(signal)

magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))

left_magnitude = magnitude[:int(len(frequency) / 2 )]
left_frequency = frequency[:int(len(frequency) / 2 )]

# plt.plot(left_frequency, left_magnitude)
# plt.xlabel("Frequency")
# plt.ylabel("Magnitude")
# plt.show()


# stft (short time fourier transform)

n_fft = 2048
hop_len = 512

stft = librosa.core.stft(signal, hop_length=hop_len, n_fft=n_fft)
spectogram = np.abs(stft)

log_spectogram = librosa.amplitude_to_db(spectogram)

# librosa.display.specshow(log_spectogram, sr=sr, hop_length=hop_len)
# plt.xlabel("Time")
# plt.ylabel("Frequency")
# plt.colorbar()
# plt.show()


# MFCCs
MFFCs = librosa.feature.mfcc(signal, n_fft=n_fft, hop_length=hop_len, n_mfcc=13)
librosa.display.specshow(MFFCs, sr=sr, hop_length=hop_len)
plt.xlabel("Time")
plt.ylabel("MFCC")
plt.colorbar()
plt.show()
