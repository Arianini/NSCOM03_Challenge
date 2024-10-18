import numpy as np
import matplotlib.pyplot as plt

# Define parameters
message = [0, 1, 0, 0, 1, 1, 0, 1]  # Binary message
bit_duration = 0.2  # Duration of each bit in seconds (1/5 second for 8 bits)
carrier_frequency = 5  # Carrier frequency in Hz
sampling_rate = 1000  # Samples per second
amplitude = 1  # Amplitude of the carrier signal

# Time array for the entire message
t = np.linspace(0, bit_duration * len(message), int(sampling_rate * bit_duration * len(message)), endpoint=False)

# Initialize phase for NRZ-I encoding
current_phase = 0
psk_signal = np.zeros_like(t)

# NRZ-I encoding: Phase change for '1', no change for '0'
samples_per_bit = int(sampling_rate * bit_duration)
for i, bit in enumerate(message):
    start = i * samples_per_bit
    end = (i + 1) * samples_per_bit
    
    # For '1', invert phase
    if bit == 1:
        current_phase += np.pi  # Change phase by 180 degrees (invert)
    
    # Generate the PSK modulated signal for the current bit
    psk_signal[start:end] = amplitude * np.cos(2 * np.pi * carrier_frequency * t[start:end] + current_phase)

# Plot the PSK signal
plt.figure(figsize=(10, 5))
plt.plot(t, psk_signal, label='PSK Modulated Signal (NRZ-I)', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Phase Shift Keying (PSK) with NRZ-I Encoding and Message [0100 1101]')
plt.grid(True)
plt.show()
