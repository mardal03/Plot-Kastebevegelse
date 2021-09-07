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

for i in range(10):
    t = i
    x.append(v_0*math.cos(math.radians(60))*t)

for i in range(10):
    t = i
    y.append(2+v_0*math.sin(math.radians(60))*t-(5*t*t))
    
plt.figure(1)

plt.plot(x,y)
plt.title("Pil og Bue")
plt.xlabel("Distanse[m]")
plt.ylabel("Høyde[m]")