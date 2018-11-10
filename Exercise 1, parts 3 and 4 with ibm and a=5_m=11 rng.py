# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:05:18 2018

@author: Ben
"""

import numpy as np
from rng_functions import rng, rng_ibm

ngroups = 16

n0 = 100000
I1 = np.zeros(n0)
I2 = np.zeros(n0)
r1 = rng_ibm(n0)
r2 = rng(n0)
for j in range(n0):
    x1 = r1[j]
    x2 = r2[j]
    I1[j] = 4*np.sqrt(1-x1**2)
    I2[j] = 4*np.sqrt(1-x2**2)

def group_measurements(ngroups):
    global I1,I2,n0
    
    nmeasurements = n0/ngroups
    for n in range(ngroups):
        I1g = 0.
        I1g2 = 0.
        I2g = 0.
        I2g2 = 0.
        for i in range(int(n*nmeasurements),int((n+1)*nmeasurements)):
            I1g += I1[i]
            I2g += I2[i]
            I1g2 += I1[i]**2
            I2g2 += I2[i]**2
        I1g /= nmeasurements
        I2g /= nmeasurements
        I1g2 /=nmeasurements
        I2g2 /= nmeasurements
        sigma1 = I1g2-I1g**2
        sigma2 = I2g2-I2g**2
        print(I1g,I1g2,sigma1,I2g,I2g2,sigma2)
        
group_measurements(10)
print("=============================")
group_measurements(20)
print("=============================")
group_measurements(1)