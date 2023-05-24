import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile

sr, data = wavfile.read('sample.wav')
print(data.shape, sr)
signal = data[:sr,0]
Signal = fft(signal)
fig, (axt, axf) = plt.subplots(2, 1, constrained_layout=1, figsize=(11.8,3))
axt.plot(signal, lw=0.15) ; axt.grid(1)
axf.plot(np.abs(Signal[:sr//2]), lw=0.15) ; axf.grid(1)
plt.show()