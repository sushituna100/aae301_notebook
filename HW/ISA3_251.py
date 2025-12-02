'''
Author: Shishir TUmma
Assignment: ISA 3 Question 2 
Date: 11/8/25
'''

import matplotlib.pyplot as plt
import pandas as pd

# 1. Data Compilation
# Aspect Ratio (AR) and Max Range (nmi) data for commercial aircraft
data = {
    'Aircraft': [
        'Boeing 777-8', 'Airbus A350-900 ULR', 'Boeing 787-9', 
        'Airbus A350-1000', 'Boeing 747-8', 'Airbus A380', 
        'Boeing 787-10'
    ],
    'Range_nmi': [8745, 9700, 7565, 9000, 7370, 8000, 6330],
    'Aspect_Ratio': [10.0, 9.5, 10.4, 9.5, 8.5, 7.5, 10.4]
}
df = pd.DataFrame(data)

# 2. Plotting Setup
plt.figure(figsize=(10, 6))

# Create the scatter plot
plt.scatter(
    df['Range_nmi'], 
    df['Aspect_Ratio'], 
    color='darkblue', 
    marker='o', 
    s=100
)

# 3. Labeling and Aesthetics
plt.title(
    'Aspect Ratio vs. Maximum Range for Commercial Airliners', 
    fontsize=16, 
    fontweight='bold'
)
plt.xlabel('Maximum Range (nmi)', fontsize=12)
plt.ylabel('Aspect Ratio (AR)', fontsize=12)

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add labels to each point to identify the aircraft and outliers
for i, row in df.iterrows():
    # Identify key aircraft for labeling clarity
    if row['Aircraft'] in ['Airbus A380', 'Boeing 777-8', 'Airbus A350-900 ULR', 'Boeing 787-10']:
        # Adjust placement for A380 (low AR) and 787-10 (low Range)
        if row['Aircraft'] == 'Airbus A380':
            plt.annotate(row['Aircraft'], (row['Range_nmi'] + 20, row['Aspect_Ratio'] - 0.15), 
                         fontsize=9, weight='bold')
        elif row['Aircraft'] == 'Boeing 787-10':
            plt.annotate(row['Aircraft'], (row['Range_nmi'] + 20, row['Aspect_Ratio']), 
                         fontsize=9, weight='bold')
        else:
            plt.annotate(row['Aircraft'], (row['Range_nmi'] + 20, row['Aspect_Ratio']), 
                         fontsize=9, weight='bold')
    else:
        # Labeling for other points
        plt.annotate(row['Aircraft'].replace('Airbus ', '').replace('Boeing ', 'B '), 
                     (row['Range_nmi'] + 20, row['Aspect_Ratio']), 
                     fontsize=9, alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()