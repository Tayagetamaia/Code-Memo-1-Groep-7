#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:51:54 2024

@author: mesutekinci
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
df = pd.DataFrame()
t1 = time.time()

positie1 = []  
positie2 = []  

b = 0.038658
m = 1.6605e-6
vc = 36

data1 = pd.read_csv("/Users/mesutekinci/Documents/Posities/posities_1_Team_07.txt", names=("t","p"), sep='   ', engine = 'python')
data2 = pd.read_csv("/Users/mesutekinci/Documents/Posities/posities_2_Team_07.txt", names=("t","p"), sep='   ', engine = 'python')

posities1 = data1["p"].replace(None, 0)
posities2 = data2["p"].replace(None, 0)
tijd = data1["t"]

nan_columns = df.columns[df.isna().all()]
df.drop(columns=nan_columns, inplace=True)

speed1 = np.zeros_like(posities1, dtype=float)
for i in range(1, len(posities1)):
    delta_posities1 = posities1[i] - posities1[i - 1]
    delta_time = tijd[i] - tijd[i - 1]  
    if delta_time != 0:
        speed1[i] = delta_posities1 / delta_time

speed2 = np.zeros_like(posities2, dtype=float)
for i in range(1, len(posities2)):
    delta_posities2 = posities2[i] - posities2[i - 1]
    delta_time = tijd[i] - tijd[i - 1]  
    if delta_time != 0:
        speed2[i] = delta_posities2 / delta_time
        
#acceleratie
acceleration1 = np.zeros_like(speed1, dtype=float)  # Creating an empty array for acceleration
for i in range(1, len(speed1)):
    delta_speed = speed1[i] - speed1[i - 1]
    delta_time = tijd[i] - tijd[i - 1]
    
    if delta_time != 0:
        acceleration1[i] = delta_speed / delta_time
        
acceleration2 = np.zeros_like(speed2, dtype=float)  # Creating an empty array for acceleration
for i in range(1, len(speed2)):
    delta_speed = speed2[i] - speed2[i - 1]
    delta_time = tijd[i] - tijd[i - 1]
    
    if delta_time != 0:
        acceleration2[i] = delta_speed / delta_time 
       
Amassa1 = -acceleration1-((b*speed1)/m)-((vc*tijd)/m)
Amassa2 = -acceleration2-((b*speed2)/m)-((vc*tijd)/m)

def dydt1(y,acceleration1):
    dy_dt1 = np.array([0.,0])
    dy_dt1[0] = y[1]
    dy_dt1[1] = acceleration1-((b*y[1])/m)-((vc*y[0])/m)
    return dy_dt1

def Form(dydt1):
    y=np.zeros([len(tijd),2])
    y[0,:]=np.array([0,0])
    
    for i, tval in enumerate(tijd[:-1]):
        y[i+1,:] = y[i,:] + (tijd[i+1]-tijd[i])*dydt1(y[i,:],acceleration1[i])
    return y 
y1 = Form(dydt1)

def dydt2(y,acceleration2):
    dy_dt2 = np.array([0.,0])
    dy_dt2[0] = y[1]
    dy_dt2[1] = acceleration2-((b*y[1])/m)-((vc*y[0])/m)
    return dy_dt2

def Form(dydt2):
    y=np.zeros([len(tijd),2])
    y[0,:]=np.array([0,0])
    
    for i, tval in enumerate(tijd[:-1]):
        y[i+1,:] = y[i,:] + (tijd[i+1]-tijd[i])*dydt2(y[i,:],acceleration2[i])
    return y 
y2 = Form(dydt2)

fig, ax1 = plt.subplots()
plt.title('Data set 1')
color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Acceleratie', color=color)
ax1.plot(tijd, acceleration1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Response', color=color)  # we already handled the x-label with ax1
ax2.plot(tijd, y1[:,0], color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

fig, ax1 = plt.subplots()
plt.title('Data set 2')
color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Acceleratie', color=color)
ax1.plot(tijd, acceleration2, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Response', color=color)  # we already handled the x-label with ax1
ax2.plot(tijd, y2[:,0], color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

 

t2 = time.time()
print(t2-t1)