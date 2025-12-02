'''
Author; Shishir Tumma
Collaborator: Aayush Kumar
Homwork: HW05
Date: 10/9/25
'''

'''
Question 1 Part C
'''

import numpy as np

#The array of all the dimensions
n = [2,3, 6]

#Intiialize the omega matrix for 3x3
omega_3 = 0

#Loop structure to print out the omega matrices
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

#Print out the results
print("--- (ii) IDFT for X = [1, 4, 4] ---")
print("IDFT Result (Standard numpy.fft.ifft):\n", np.round(standard_idft_result, 4))
print("-" * 30)


'''
Question 2
'''

import matplotlib.pyplot as plt
nu = 2**19  # Number of samples (nu = N)
N = nu
L = 2 * np.pi  # Domain length
fs = N / L  # Sampling frequency
dt = L / N  # Sample time step

# Define the function
def f_t(t):
    """The function f(t) = sin(30t) * exp(2 * cos(5t))."""
    return np.sin(30 * t) * np.exp(2 * np.cos(5 * t))

# Sample points t_j = 2*pi*j / nu
j = np.arange(N)
t = j * dt
f_sampled = f_t(t)

#Get the fourier coefficeints
fft_coeff = np.fft.fft(f_sampled)

#Get the ordered coefficients from (0 to N-1)
c_k_fft_ordered = fft_coeff / N

#Shift the coefficients back
c_k = np.fft.fftshift(c_k_fft_ordered)

#Frequencies range from -N/2 to N/2 - 1
k_all = np.fft.fftshift(np.fft.fftfreq(N, d=dt/(2*np.pi)))

#Plot the double-sided power spectrum
k_range = np.arange(-100, 101)
indices = k_range + N//2
c_k_array = c_k[indices]

#Calc the power spectrum
power_spectrum = np.abs(c_k_array)**2

plt.figure(figsize = (10,10))
plt.stem(k_range, power_spectrum)
plt.xlabel('Frequency index (k)')
plt.ylabel("Power (|c_k|^2)")
plt.title(r'Two-Sided Power Spectrum $|\mathbf{c}_k|^2$ for $k \in [-100, 100]$')
plt.grid(True)
plt.show()

#Get the single-sided power spectrum
power_spectrum_single = power_spectrum[0:101]
k_range_single = k_range[0:101]

plt.figure(figsize = (10,10))
plt.stem(k_range_single, power_spectrum_single)
plt.xlabel('Frequency index (k)')
plt.ylabel("Power (|c_k|^2)")
plt.title(r'Single-Sided Power Spectrum $|\mathbf{c}_k|^2$ for $k \in [0, 100]$')
plt.grid(True)
plt.show()

threshold = 0.000001
mask = np.abs(c_k) > threshold
k_nz = k_all[mask]
c_k_nz = c_k[mask]

#Sort by magnitude
sorted_indices = np.argsort(np.abs(c_k_nz))

k_sorted = k_nz[sorted_indices]
c_k_sorted = c_k_nz[sorted_indices]

k_inf_guess = sorted(list(set(np.abs(c_k_sorted[np.abs(c_k_sorted)**2 > threshold]))))

print("\n" + "="*50)
print(f"a) Estimated K_inf Frequencies (Absolute values of k with |c_k|^2 > 1e-10):\n{k_inf_guess}")
print("Theoretical K_inf = {k | k = ±30 + 5m, m ∈ Z}")
print("="*50 + "\n")


'''Question 2 Part B and C and D'''

S_coeffs = c_k_sorted[:12]
S_k = k_sorted[:12]

K_coeffs = c_k_sorted[:28]
K_k = k_sorted[:28]

def reconstruct_approximations(t, coeffs, frequencies):
    p_t = np.zeros_like(t, dtype = np.complex128)

    for c, k in zip(coeffs, frequencies):
        p_t += c * np.exp(-1j * k * t)

    return np.real(p_t)

p_S_t = reconstruct_approximations(t, S_coeffs, S_k)
p_K_t = reconstruct_approximations(t, K_coeffs, K_k)

plot_start = 0
plot_end = 2 * np.pi

idx_start = np.argmin(np.abs(t - plot_start))
idx_end = np.argmin(np.abs(t - plot_end))


print("\n" + "="*50)
print("b & c & d) Approximations of f(t) using equations S and K:\n")
plt.figure(figsize = (10,10))
plt.plot(t[idx_start:idx_end], f_sampled[idx_start:idx_end], label = "f(t)")
plt.plot(t[idx_start:idx_end], p_S_t[idx_start:idx_end], label = "S")
plt.plot(t[idx_start:idx_end], p_K_t[idx_start:idx_end], label = "K")
plt.title("Approximations of f(t) using equations S and K")
plt.legend(loc = 'best')
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)
plt.show()
print("="*50 + "\n")


'''Question 2 Part E'''

#Create the norm of the fourier function
norm_f = np.sqrt(dt * np.sum(np.abs(f_sampled)**2))

#Calculate the error and norm of the function with S
error_S = f_sampled - p_S_t
norm_error_S = np.sqrt(dt * np.sum(np.abs(error_S)**2))

#Calculate the error and norm of the function with K
error_K = f_sampled - p_K_t
norm_error_K = np.sqrt(dt * np.sum(np.abs(error_K)**2))


print("\n" + "="*50)
print("e) Norm Computations (Approximation of L2 Norm):")
print(f"||f|| = sqrt((2*pi/N) * sum(|f_j|^2)) ≈ {norm_f:.6f}")
print(f"||f - p_S|| (12 coeffs) ≈ {norm_error_S:.6f}")
print(f"||f - p_K|| (28 coeffs) ≈ {norm_error_K:.6f}")
print("="*50)=f