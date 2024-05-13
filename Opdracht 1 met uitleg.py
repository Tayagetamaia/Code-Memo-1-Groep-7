# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define physical parameters for the system
k = 42  # Spring constant in N/m
m = 1.9372e-6  # Mass of the object in kg
y = 0.045101  # Damping coefficient in kg/s

# Read in the position data from a text file, assuming whitespace delimiter
data = pd.read_csv('posities_1_Team_07.txt', sep='\s+')    

# Calculate velocity by finite difference of position 'x' with respect to time 't'
# Shift(1) moves the data down one row for subtraction, division by time interval gives velocity
data["v (m/s)"] = (data["x"] - data["x"].shift(1)) / (data["t"] - data["t"].shift(1))

# Calculate acceleration by finite difference of velocity with respect to time
# Resulting NaN values from shift are replaced with 0
data["a (m/s^2)"] = (data["v (m/s)"] - data["v (m/s)"].shift(1)) / (data["t"] - data["t"].shift(1))
data = data.fillna(0)

# Convert time column to a numpy array for numerical operations
t = np.array(data["t"].values)

# Convert the acceleration data for use in numerical integration and initialize arrays
xf = np.array(data["a (m/s^2)"].values)  # External force from acceleration data
x = np.zeros_like(t)  # Array to store position values calculated by Euler's method
x_prime = np.zeros_like(t)  # Array to store velocity values calculated by Euler's method

# Implement Euler's method to solve the differential equation for motion
# This loop iterates over each time step, updating the position 'x' and velocity 'x_prime'
for i in range(len(t)-1):
    # Calculate the net acceleration from force balance: F = ma, considering damping and spring force
    x_2prime = (m*xf[i] - y*x_prime[i] - k * x[i]) / m
    # Update velocity using Euler's forward method: v = v0 + a*dt
    x_prime[i+1] = x_prime[i] + (t[i+1] - t[i]) * x_2prime
    # Update position using Euler's forward method: x = x0 + v*dt
    x[i+1] = x[i] + (t[i+1] - t[i]) * x_prime[i]

# Plotting the results for visualization
plt.plot(data['t'], data['a (m/s^2)'] * 0.00005, label='Scaled Acceleration')  # Scale acceleration for visibility
plt.twinx()  # Create a second y-axis for different scale
plt.plot(data["t"], x, color='orange', label='Position from Euler’s method')  # Plot position over time
plt.title("Acceleration and Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.show()
