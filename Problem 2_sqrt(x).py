# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:56:06 2018

@author: Ben
"""

import numpy as np
from matplotlib import pyplot

def g(x):
    return np.sqrt(x)

N = 100000

# Simple Monte Carlo integration
n0 = N
a = np.arange(0.5,5.0,0.1)
I = np.zeros(np.size(a))
Ivar = np.zeros(np.size(a))


r = np.random.random(n0)

I0 = np.sum(np.sqrt(r))
print("Simple Monte Carlo: ", I0/n0)

# Importance Sampling
print("Importance Sampling: ")
              
i = 0
for ai in a:
    norm = (ai-1+np.exp(-ai))/ai #You need a normalized probability distribution
    x = -norm*np.log(1-(r))/ai

    Itot = 0.
    Nin = 0
    I2 = 0.
    for xi in x:
        if(xi <= 1):
            Nin += 1
            Itot += g(xi)/(1-np.exp(-xi*ai))
            I2 += (g(xi)/(1-np.exp(-xi*ai)))**2
            
    Itot *= norm
    I2 *= norm

    I[i] = Itot/Nin
    Ivar[i] = np.sqrt(abs(Itot**2/Nin**2-I2/Nin))/np.sqrt(Nin)
    print(ai,Itot/Nin,Ivar[i])
    i += 1
 

pyplot.plot(a, Ivar)
pyplot.xlabel('a')
pyplot.ylabel('Variance of MC integral')
pyplot.show()
