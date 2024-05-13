# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:02:24 2024

@author: guush
"""

# import libraries
import numpy as np

# material constants
E = 170e9
density = 2330
thickness = 2e-6

# spring constants
b = 1e-6
L = 85e-6

# spring count
spring_count = 4


# chip constants
chip_length = 200e-6
chip_width = 200e-6

# mass constants
mass_length = 190e-6
mass_width = 150e-6


# calculate the spring constant in N /m
def calculate_spring_constant(b, L):
    segments = ((chip_width - mass_width) / 2) / 2e-6   # calculate the anount of segments of the spring
    return ((E * thickness * b**3) / L**3) * spring_count / np.floor(segments) # calculate the strength of spring and divide the number of segments

# calculate volume and multiply by density
def calculate_mass(length, width):
    return density * thickness * length * width

# calculate resonant frequency
def calculate_resonant_frequency(mass, k):
    T = 2 * np.pi * np.sqrt(mass / k)
    return 1 / T

# define constants using functions
k = calculate_spring_constant(b, L)
m = calculate_mass(mass_length, mass_width)
f = calculate_resonant_frequency(m, k)

# print results
print("k:", k)
print("m:", m)
print("f:", f)