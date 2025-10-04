import numpy as np
import matplotlib.pyplot as plt

#  Add in the data
loads_lb = [
    1000, 2000, 6000, 10000, 12000, 12900, 13400, 13600, 13800,
    14000, 14400, 15200, 16800, 18400, 20000, 22400, 22600
]
elongations_in = [
    0.0002, 0.0006, 0.0019, 0.0033, 0.0039, 0.0043, 0.0047, 0.0054,
    0.0063, 0.0090, 0.0102, 0.0130, 0.0230, 0.0336, 0.0507, 0.1108, 0.1200 # The last value is the elongation at fracture
]

# Specimen dimensions
original_diameter_in = 0.505 # (in)
gage_length_in = 2.00 # (in)
final_diameter_in = 0.42 # (in)


# Calculations
def calculate_stress_strain(loads, elongations, original_area, gage_length):
    """Calculates conventional stress and strain."""
    stress_psi = np.array(loads) / original_area
    strain_in_in = np.array(elongations) / gage_length
    return stress_psi, strain_in_in

# Calculate original and final areas
original_area_in2 = np.pi * (original_diameter_in / 2)**2
final_area_in2 = np.pi * (final_diameter_in / 2)**2

# Calculate stress and strain for the entire dataset
stress, strain = calculate_stress_strain(loads_lb, elongations_in, original_area_in2, gage_length_in)


#  Plot the Conventional Stress-Strain Curve
plt.figure(figsize=(10, 6))
plt.plot(strain, stress, 'b-o', label='Stress-Strain Curve')
plt.title('Stress-Strain Curve for HSS')
plt.xlabel('Strain (in/in)')
plt.ylabel('Stress (psi)')
plt.grid(True)
plt.legend()
plt.show()


## Proportional Limit
proportional_limit_load = 12900
proportional_limit_stress = proportional_limit_load / original_area_in2
print(f"Proportional Limit Stress: {proportional_limit_stress:.2f} psi")

## Modulus of Elasticity (E)
linear_stress = stress[0:5]
linear_strain = strain[0:5]
modulus_of_elasticity, _ = np.polyfit(linear_strain, linear_stress, 1)
print(f"Modulus of Elasticity (E): {modulus_of_elasticity:.2f} psi")

## Yield Stress (0.1% offset)
# The intersection of this line parallel to the elastic region with the stress-strain curve is the yield point.
offset_strain = strain + 0.001
offset_yield_stress_slope = modulus_of_elasticity
offset_yield_stress_intercept = -offset_yield_stress_slope * 0.001
offset_line_stress = (strain * offset_yield_stress_slope) + offset_yield_stress_intercept

# Find the point where the stress crosses the offset_line_stress
diff = stress - offset_line_stress
idx = np.argmin(np.abs(diff)) # Find the index where the difference is minimal
yield_stress_01_offset = stress[idx]
print(f"Yield Stress (0.1% Offset): {yield_stress_01_offset:.2f} psi")

## Ultimate Stress
ultimate_stress = max(stress)
ultimate_load = max(loads_lb)
print(f"Ultimate Stress: {ultimate_stress:.2f} psi (from load of {ultimate_load} lb)")

## Percent Elongation
elongation_at_fracture = 0.1200 # from the problem description
percent_elongation = (elongation_at_fracture / gage_length_in) * 100
print(f"Percent Elongation: {percent_elongation:.2f}%")

## Percent Reduction in Area
percent_reduction_in_area = ((original_area_in2 - final_area_in2) / original_area_in2) * 100
print(f"Percent Reduction in Area: {percent_reduction_in_area:.2f}%")