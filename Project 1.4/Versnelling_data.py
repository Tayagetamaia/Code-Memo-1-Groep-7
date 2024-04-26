# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:33:21 2024

@author: guush
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Data\posities\posities_1_Team_07.txt', delim_whitespace=True)


data["v (m/s)"] = (data["x"] - data["x"].shift(1)) / (data["t"] - data["t"].shift(1))
data["a (m/s^2)"] = (data["v (m/s)"] - data["v (m/s)"].shift(1)) / (data["t"] - data["t"].shift(1))


plt.plot(data["t"], data["a (m/s^2)"])