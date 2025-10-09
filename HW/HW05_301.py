'''
Author; Shishir Tumma
Collaborator: Aayush Kumar
Homwork: HW05
Date: 10/9/25
'''
import numpy as np


#The dimnsion of the matrix
n = [2,3, 6]

omega_3 = 0

for N in n:
    #Build the matrix where i and k represents the rows and column indices
    i, k = np.meshgrid(np.arange(N), np.arange(N))

    #Build the omega matrix
    omega = np.exp(-2j * np.pi * i * k / N)
    
    if N == 3:
        omega_3 = omega

    print(f"--- (i) {N} x {N} DFT Matrix ---")
    print(np.round(omega, 4))
    print("-" * 30)


# Initialize the dataset
data = np.array([1, 4, 4])

# Using the numpy IDFT function (np.fft.ifft)
standard_idft_result = np.fft.ifft(data)

print("--- (ii) IDFT for X = [1, 4, 4] ---")
print("IDFT Result (Standard numpy.fft.ifft):\n", np.round(standard_idft_result, 4))
print("-" * 30)