''''
Author: Shishir Tumma
Assignment: HW03
Date: 9/11/25
Collaborators: Aayush Kumar
'''

import sympy as sp
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

'''Question 1'''

#Create the t arrays
t_lin= np.linspace(0, 2* np.pi, 1000)

#Create the f arrays with the proper functions
f = np.where((t_lin<= np.pi), (2 * np.pi), (-2 * np.pi))

#initalize the approx
total_approx = 0

# Initalize the number of k values (n)
n = 80

for k in range(1, n +1):
    #Only do the odd k values
    if k % 2 == 1:
        total_approx += 8 * np.sin(k*t_lin)/k

# #Plot the total approx
plt.plot(t_lin, total_approx)
plt.plot(t_lin,f)
plt.title('Question 1 part A')
plt.show()

#Part B

#Create symbols
t = sp.symbols('t', real=True)

k_list = range(-80, 81)

#Create the constants 
tau = 2 * sp.pi
w0 = 2 * sp.pi/tau

#Initialize the list for the magnitudes of ak
ak_list_mag = []

for k in tqdm(k_list):
    #Split the integral
    psi_k = sp.exp(-sp.I * w0 * k* t)

    ak_1 = (sp.integrate(2 * pi * sp.conjugate(psi_k), (t, 0, tau/2))/tau)
    ak_2 = (sp.integrate(-2 * pi * sp.conjugate(psi_k), (t, tau/2, tau))/tau)
    ak = ak_1 + ak_2
    ak_list_mag.append(np.abs(ak**2))    



#Plot the total approx
plt.plot(k_list, ak_list_mag)
plt.title('Question 1 part B')
plt.grid()
plt.show()



'''Question 3'''

#Create symbols
t = sp.symbols('t', real=True)
k = sp.symbols('k', real = True)

#Create the constants
tau = 2 * np.pi
w0 = 2 * np.pi/tau

#Initilize the linspace and function
t_lins = np.linspace(0, 2*np.pi, 100)
f = np.where(t_lins < np.pi, t_lins, (t_lins - 2*np.pi))

#Initialize the fourier approximation
approx = 0

n = 10
for k in tqdm(range(-n, n+1)):
    psi_k = np.exp(-1j * w0 * k* t_lins)
    
    if k == 0:
        ak = 0
    #Odd version
    elif k % 2 == 1:
        ak = 1j/k
    else:
        ak = -1j/k
    approx += ak*psi_k

plt.figure(figsize = (10,6))
plt.plot(t_lins, f)
plt.plot(t_lins, approx)
plt.title('Question 3')
plt.show()
