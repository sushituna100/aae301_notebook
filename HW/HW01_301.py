import matplotlib.pyplot as plt
import numpy as np

'''Problem 8'''

#Number of roots
n = 50

#Calc the n of unity
k_values = np.arange(n)
angles = 2 * np.pi * k_values / n
roots = np.exp(1j * angles)

#Create the figure
plt.figure(figsize = (10,10))
plt.plot(roots.real, roots.imag, 'o')
plt.title('Roots of Unity of n=50')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.savefig('HW01_301_8.png')
plt.show()


'''Problem 9.c'''

#Use Numpy's linspace to create an "linspace" arry of 100 points similar to MATLAB
theta = np.linspace(0, 2 *np.pi, 100)

#Create the complex numbers z_1 and z_2
#J is represented as the imaginary number in Python
z_1 = np.exp(3j * theta)
z_2 = 1j * np.exp(-2j * theta)

#Create the figure
plt.figure(figsize = (12,6))
plt.subplot(1,2,1)
plt.plot(z_1.real, z_1.imag, label='z_1 = e^(3jθ)')
plt.title('Parameteric Plots of z_1')
plt.xlabel('Real Part')
plt.ylabel("Imaginary Part")
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

plt.subplot(1,2,2)
plt.plot(z_2.real, z_2.imag, label='z_1 = je^(-2jθ)')
plt.title('Parameteric Plots of z_2')
plt.xlabel('Real Part')
plt.ylabel("Imaginary Part")
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

#Save and show the plots
plt.savefig('HW01_301_9c.png')
plt.show()
