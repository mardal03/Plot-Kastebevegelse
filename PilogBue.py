# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:27:54 2021

@author: Bruker
"""

import math
import matplotlib.pyplot as plt

x = []
y = []

v_0 = 49
t_t = 4.32
y_0 = 2
v_0y = 42.44
v_0x = 24.5
t_f = 8.7
g = 9.81

for i in range(1000):
    t = i/115
    x.append(v_0*math.cos(math.radians(60))*t)

for i in range(1000):
    t = i/115
    y.append(2+v_0*math.sin(math.radians(60))*t-(5*t*t))
    
plt.figure(1)

plt.plot(x,y)
plt.title("Pil og Bue")
plt.xlabel("Distanse[m]")
plt.ylabel("Høyde[m]")

y_t = v_0y * t_t - 0.5 * g * t_t * t_t + y_0
x_f = v_0x * t_f

print("Buen skjøt " + str(round(x_f, 2)) + " meter langt.")
print("Pilens høyeste punkt er " + str(round(y_t, 1)) + " m over bakken.")