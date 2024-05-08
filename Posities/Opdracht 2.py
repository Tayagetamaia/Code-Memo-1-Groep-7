import numpy as np

# Constants
E = 170e9  # Young's modulus for Silicon in Pascals
thickness = 2e-6  # Thickness in meters
density = 2330  # Density of silicon in kg/m^3


max_length = 200e-6
max_width = 200e-6

# Calculate spring constant and resonant frequency
def calculate_spring_constant(width, length):
    return E * (thickness * width**3) / (length**3)

def calculate_mass(width, length):
    return density * thickness * width * length

def calculate_resonant_frequency(k, m):
    return 1 / (2 * np.pi) * np.sqrt(k / m)


min_frequency = np.inf
optimal_design = None




for width, length in zip(np.linspace(1e-6, max_width, 100), np.linspace(1e-6, max_length, 100)):
    k = calculate_spring_constant(width, length)
    m = calculate_mass(width, length)
    f_0 = calculate_resonant_frequency(k, m)
    
    if f_0 < min_frequency:
        min_frequency = f_0
        
        optimal_design = (width, length, f_0, k, m)


width, length, f_0, k, m = optimal_design
print(f"Optimal Width: {width*1e6} µm")
print(f"Optimal Length: {length*1e6} µm")
print(f"Resonant Frequency: {f_0} Hz")
print(f"Spring Constant: {k} N/m")
print(f"Mass: {m*1e9} ng")
