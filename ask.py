import numpy as np
import matplotlib.pyplot as plt


bits = '01001101'
sample_rate = 1000  
duration = 1  
amplitude = 7
frequency = 2  
phase_distortion = np.deg2rad(37)  

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

signal = np.array([])
for bit in bits:
    if bit == '1':
        wave = amplitude * np.sin(2 * np.pi * frequency * t + phase_distortion)
    else:
        wave = np.zeros_like(t)
    signal = np.concatenate((signal, wave))

t_full = np.linspace(0, len(bits) * duration, int(sample_rate * duration * len(bits)), endpoint=False)

plt.figure(figsize=(12, 6))
plt.plot(t_full, signal, label='ASK Modulated Signal', color='b')
plt.title('ASK Modulation of the Message [0100 1101]')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='--', label='Amplitude = 0 (for bit 0)')
plt.axhline(y=amplitude, color='r', linestyle='--', label='Amplitude = 7 (for bit 1)')
plt.text(0.1, 3, 'Phase Distortion: 37°', fontsize=10, color='orange')
plt.legend()
plt.show()
