import numpy as np

# Constants
E = 170e9  # Young's modulus for Silicon in Pascals (Pa)
thickness = 2e-6  # Thickness of the beam in meters (m)
density = 2330  # Density of silicon in kilograms per cubic meter (kg/m^3)

max_length = 200e-6  # Maximum length of the beam in meters (m)
max_width = 200e-6  # Maximum width of the beam in meters (m)

# Function to calculate the spring constant of the beam
def calculate_spring_constant(width, length):
    """
    Calculate the spring constant of a rectangular silicon beam.

    Parameters:
    width (float): Width of the beam in meters.
    length (float): Length of the beam in meters.

    Returns:
    float: Calculated spring constant in Newtons per meter (N/m).
    """
    return E * (thickness * width**3) / (length**3)

# Function to calculate the mass of the beam
def calculate_mass(width, length):
    """
    Calculate the mass of a rectangular silicon beam.

    Parameters:
    width (float): Width of the beam in meters.
    length (float): Length of the beam in meters.

    Returns:
    float: Calculated mass in kilograms (kg).
    """
    return density * thickness * width * length

# Function to calculate the resonant frequency of the beam
def calculate_resonant_frequency(k, m):
    """
    Calculate the resonant frequency of the beam based on its spring constant and mass.

    Parameters:
    k (float): Spring constant in Newtons per meter (N/m).
    m (float): Mass in kilograms (kg).

    Returns:
    float: Resonant frequency in Hertz (Hz).
    """
    return 1 / (2 * np.pi) * np.sqrt(k / m)

min_frequency = np.inf  # Initialize the minimum frequency found to infinity
optimal_design = None  # Initialize the optimal design variables

# Iterate over possible widths and lengths within the specified range
for width, length in zip(np.linspace(1e-6, max_width, 100), np.linspace(1e-6, max_length, 100)):
    k = calculate_spring_constant(width, length)  # Calculate spring constant
    m = calculate_mass(width, length)  # Calculate mass
    f_0 = calculate_resonant_frequency(k, m)  # Calculate resonant frequency
    
    # Check if the current design results in a lower resonant frequency
    if f_0 < min_frequency:
        min_frequency = f_0
        optimal_design = (width, length, f_0, k, m)  # Update optimal design

# Extracting the optimal design parameters
width, length, f_0, k, m = optimal_design
print(f"Optimal Width: {width*1e6} µm")
print(f"Optimal Length: {length*1e6} µm")
print(f"Resonant Frequency: {f_0} Hz")
print(f"Spring Constant: {k} N/m")
print(f"Mass: {m*1e9} ng")
