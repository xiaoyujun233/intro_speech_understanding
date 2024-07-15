import numpy as np

def fourier_synthesis(num_harmonics, X, T0):
    N = len(X)
    x = np.zeros(N)
    for l in range(1, num_harmonics + 1):
        for n in range(N):
            x[n] += np.abs(X[(l * N // T0) % N]) * np.cos(2 * np.pi * l * n / T0 + np.angle(X[(l * N // T0) % N]))
    
    x *= 2 / N  # Scale by 2/N
    
    return x

