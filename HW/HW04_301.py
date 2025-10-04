'''
Author: Shishir Tumma
Assignment: HW04
Date: 9/11/25
'''

import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

M=20000

t_bounds = np.linspace(0.0, 2*PI, M+1)
t_int = t_bounds[:-1]

f_int = t_int * np.sin(t_int)

#Define the size of arrays
n_max = 100

#Solve for a0
a0 = (1.0/(2*PI)) * np.trapz(f_int, t_int)

alpha = np.zeros(n_max)
beta = np.zeros(n_max)

# Part B

for k in range(1, n_max+1):
    alpha[k-1] = (1.0/(PI)) * np.trapz(f_int * np.cos(k*t_int), t_int)
    beta[k-1] = (1.0/(PI)) * np.trapz(f_int * np.sin(k*t_int), t_int)

#Create the logic for the periodic extensions
t_range = np.linspace(0.0, 6*PI, 6000)
t_repeat = np.mod(t_range, 2*PI)
f_plot = t_repeat * np.sin(t_repeat)

plt.figure()
plt.plot(t_range, f_plot, label = "f(t)")

for n in (2, 5, 20):
    s = a0 * np.ones_like(t_range)
    for k in range(1, n+1):
        #Calculate the summation
        s+= alpha[k-1] * np.cos(k * t_range) + beta[k-1] * np.sin(k * t_range)
    plt.plot(t_range, s, label = f"p_{n}(t)")

plt.xlim([0.0, 6*PI])
plt.xlabel("t")
plt.ylabel("f(t)")
plt.legend(loc = 'best')
plt.title('HW 4 Problem 4')
plt.show()

#Part C

for n in (2,10):
    s = a0 * np.ones_like(t_int)  # Changed to use t_int instead of t_range
    for k in range(1, n+1):
        s += alpha[k-1] * np.cos(k * t_int) + beta[k-1] * np.sin(k * t_int)  # Using t_int for evaluation
    g2 = (f_int - s)**2
    plain = np.sqrt(np.trapz(g2, t_int))
    norm = np.sqrt((1.0/(2*PI)) * np.trapz(g2, t_int))
    print(f'n = {n}, ||f - p_n(t)|| = {plain:.4f}, L2_norm = {norm:.4f}')