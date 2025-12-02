#Shishir TUmma
#Homework 8
#Date: 11/7/25

import numpy as np
from sympy import *

# --- 1. Parameters and Structural Analysis ---
h = symbols('h') # The variable to solve for
P = 750
q_lb_ft = 110
L1_ft = 3
L2_ft = 8
L3_ft = 5
b = 2.5
t = 3/8
sigma_t_allow = 18000 # psi
sigma_c_allow = 12000 # psi

# Maximum moment (from right overhang)
M_max = Abs(- (q_lb_ft * L3_ft) * (L3_ft / 2) * 12) 

#Geometric properties
A_flange = b * t
A_web = t * h
A_total = A_flange + A_web

# Centroid (y_bar) from the BOTTOM
y_bar = (A_flange * (t/2) + A_web * (t + h/2)) / A_total

# Moment of Inertia (I)
I_flange = (b * t**3) / 12 + A_flange * (y_bar - t/2)**2
I_web = (t * h**3) / 12 + A_web * ((t + h/2) - y_bar)**2
I = I_flange + I_web

# Distances to Extreme Fibers (Flange at bottom, Web at top)
c_tension = y_bar        # Bottom fiber (Tension from M_max hogging)
c_compression = (t + h) - y_bar  # Top fiber (Compression from M_max hogging)

# --- 3. Design Constraint Equations (f(h) = 0) ---
# The design is governed by the maximum stress being equal to the allowable stress.
tension_constraint = (M_max * c_tension / I) - sigma_t_allow
compression_constraint = (M_max * c_compression / I) - sigma_c_allow

# --- 4. Numerical Solution for h ---
h_guess = 5.0

# Solve for h for each constraint
h_tension = nsolve(tension_constraint, h, h_guess, verify=False)
h_compression = nsolve(compression_constraint, h, h_guess, verify=False)

# The required h is the larger (governing) value
h_required = np.max([float(h_tension), float(h_compression)])

# --- 5. Output Results ---
print(f"--- Required Depth (h) Calculation (Part D) ---")
print(f"Maximum Bending Moment: {M_max:.2f} lb-in")
print(f"Allowable Tension Stress: {sigma_t_allow/1000:.0f} ksi")
print(f"Allowable Compression Stress: {sigma_c_allow/1000:.0f} ksi")
print("-" * 45)
print(f"h required by Tension constraint: {float(h_tension):.4f} in")
print(f"h required by Compression constraint: {float(h_compression):.4f} in")
print("-" * 45)
print(f"Governing Required Web Depth h = {h_required:.4f} in")