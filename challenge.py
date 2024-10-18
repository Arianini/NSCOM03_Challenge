import numpy as np
import matplotlib.pyplot as plt

# Define parameters
message = [0, 1, 0, 0, 1, 1, 0, 1]  # Binary message
amplitude = 5  # Amplitude of the cosine wave
carrier_frequency = 10  # Carrier frequency in Hz
sampling_rate = 1000  # Samples per second
bit_duration = 0.125  # Duration for each bit (1/8 second for 8 bits over 1 second)
duration = bit_duration * len(message)  # Total duration based on the message

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Carrier signal (cosine wave)
carrier = amplitude * np.cos(2 * np.pi * carrier_frequency * t)

# Define noise components with a frequency of 1 Hz (one cycle per second)
noise_amplitude = 2.5
noise_frequency = 1  # 1 Hz frequency to complete 1 cycle every second

# Create noise signals (one cycle each)
noise_1 = noise_amplitude * np.cos(2 * np.pi * noise_frequency * t)
noise_2 = noise_amplitude * np.cos(2 * np.pi * noise_frequency * t + np.pi / 2)  # Phase shift for variation

# Combine noise components to create a modulation factor
modulation_factor = (noise_1 + noise_2) / 5  # Normalize to avoid extreme values

# Apply the binary message to the carrier for ASK modulation
modulated_carrier = np.zeros_like(t)

# Encode message using ASK
for i, bit in enumerate(message):
    start = int(i * bit_duration * sampling_rate)
    end = int((i + 1) * bit_duration * sampling_rate)
    modulated_carrier[start:end] = carrier[start:end] if bit == 1 else 0

# Multiply the modulated carrier by the modulation factor
modulated_signal = modulated_carrier * (1 + modulation_factor)  # Add 1 to ensure positive scaling

# Plot the signals
plt.figure(figsize=(12, 8))

# Plot the carrier signal
plt.subplot(3, 1, 1)
plt.plot(t, modulated_carrier, label='Modulated Carrier (ASK with Message)', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Modulated Carrier Signal with Message [0100 1101]')
plt.grid(True)

# Plot the modulation factor (combined noise)
plt.subplot(3, 1, 2)
plt.plot(t, modulation_factor, label='Modulation Factor (Noise)', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Modulation Factor from Combined Noise')
plt.grid(True)

# Plot the modulated signal with noise
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, label='AM Modulated Signal with Multiplicative Noise', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('AM Modulation (ASK) with Message and Multiplicative Noise')
plt.grid(True)

# Adjust layout and show plot
plt.tight_layout()
plt.show()
