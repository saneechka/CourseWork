import numpy as np
import matplotlib.pyplot as plt

def fft_butterfly_n8(x):
    N = 8
    # Stage 1: Split into even/odd
    even = x[::2]  # [x0, x2, x4, x6]
    odd = x[1::2]  # [x1, x3, x5, x7]
    
    # Twiddle factors
    W = np.exp(-2j * np.pi * np.arange(N) / N)
    
    # Stage 2: 4-point FFTs
    stage2_even = np.fft.fft(even)
    stage2_odd = np.fft.fft(odd)
    
    # Stage 3: Combine using butterfly operations
    X = np.zeros(N, dtype=complex)
    for k in range(N//2):
        X[k] = stage2_even[k] + W[k] * stage2_odd[k]
        X[k + N//2] = stage2_even[k] - W[k] * stage2_odd[k]
    
    return X

# Test with sample input
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
X = fft_butterfly_n8(x)

# Plotting
plt.figure(figsize=(12, 8))

# Plot input points
plt.plot(range(8), x, 'bo-', label='Input')

# Plot FFT result magnitude
plt.plot(range(8), np.abs(X), 'ro-', label='FFT magnitude')

plt.title('FFT Butterfly Diagram N=8')
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()
plt.show()