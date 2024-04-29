# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:33:21 2024

@author: guush
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# paramaters
k = 42  # N / m
m = 1.9372e-3  # kg
y = 0.045101  # kg / s

# read in data
data = pd.read_csv('Data\posities\posities_1_Team_07.txt', sep='\s+')



# make velocity and acceleration columns and fill Nans with 0
data["v (m/s)"] = (data["x"] - data["x"].shift(1)) / (data["t"] - data["t"].shift(1))
data["a (m/s^2)"] = (data["v (m/s)"] - data["v (m/s)"].shift(1)) / (data["t"] - data["t"].shift(1))
data = data.fillna(0)

# make array with time data
t = np.array(data["t"].values)

# get acceleration and make empty arrays for Eulers method
xf = np.array(data["a (m/s^2)"].values)
x = np.zeros_like(t)
x_prime = np.zeros_like(t)


# apply euelers method
for i in range(len(t)-1):
    x_2prime = (m*xf[i] - y*x_prime - k * x[i]) / m
    x_prime[i+1] = x_prime[i] + (t[i+1] - t[i]) * x_2prime[i]
    x[i+1] = x[i] + (t[i+1] - t[i]) * x_prime[i]
                
# plot the acceleration and differential equation
plt.plot(data['t'], data['a (m/s^2)'] * 0.00005) # * 0.0005 scales the values down so it fits in one graph
plt.plot(data["t"], x)