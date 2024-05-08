import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# paramaters
k = 42  # N / m
m = 1.9372e-3  # kg
y = 0.045101  # kg / s



data = np.genfromtxt("posities_1_Team_07.txt", delimiter="  ", skip_header=1)
data2 = np.genfromtxt("posities_2_Team_07.txt", delimiter="  ", skip_header=1)

tijd = data[:, 0]
positie_x = data[:, 1]

tijd2 = data2[:, 0]
positie_x2 = data2[:, 1]



snelheid_x = np.gradient(positie_x, tijd) 
versnelling_x = np.gradient(snelheid_x, tijd)


snelheid_x2 = np.gradient(positie_x2, tijd2) 
versnelling_x2 = np.gradient(snelheid_x2, tijd2)


plt.xlabel('tijd')
plt.ylabel('versnelling_x')
plt.plot(tijd, versnelling_x*0.0005)
plt.plot(tijd2, versnelling_x2*0.0005)
plt.show()