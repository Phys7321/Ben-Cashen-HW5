# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:14:25 2018

@author: Ben
"""

# Simple Monte Carlo Integration w/ IBM rng and a = 5, m = 11 rng

import numpy as np
from matplotlib import pyplot
from rng_functions import rng, rng_ibm

ngroups = 16

I1 = np.zeros(ngroups)
I2 = np.zeros(ngroups)
N = np.zeros(ngroups)
Dev1 = np.zeros(ngroups)
Dev2 = np.zeros(ngroups)

n0 = 100
for i in range(ngroups):

    N[i] = n0
    r1 = rng_ibm(n0)
    r2 = rng(n0)
    I1[i] = 0.
    I2[i] = 0.
    for j in range(n0):
        x1 = r1[j]
        x2 = r2[j]
        I1[i] += np.sqrt(1-x1**2)
        I2[i] += np.sqrt(1-x2**2)
        
    I1[i] *= 4./float(n0)
    I2[i] *= 4./float(n0)
    Dev1[i] = abs(I1[i]-np.pi)
    Dev2[i] = abs(I2[i]-np.pi)
    print(n0,I1[i],Dev1[i],I2[i],Dev2[i])
    n0 *= 2
    
            
pyplot.plot(N,Dev1,ls='-',c='red',lw=3,label='IBM Deviation');
pyplot.plot(N,Dev2,ls='-',c='green',lw=3,label='a = 5, m = 11 Deviation')
pyplot.plot(N,1/np.sqrt(N),ls='-',c='blue',lw=3,label='1/sqrt(N)');
pyplot.xscale('log')
pyplot.yscale('log')
pyplot.title('Simple MC')