# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:50:33 2018

@author: Ben
"""

import numpy as np
from matplotlib import pyplot
from rng_functions import rng

ngroups = 16

I = np.zeros(ngroups)
N = np.zeros(ngroups)
Dev = np.zeros(ngroups)

n0 = 100
for i in range(ngroups):

    N[i] = n0
    x = rng(n0)
    y = rng(n0)
    I[i] = 0.
    Nin = 0
    for j in range(n0):
        if(y[j] < np.sqrt(1-x[j]**2)):
            Nin += 1
            
    I[i] = 4.*float(Nin)/float(n0)
    Dev[i] = abs(I[i]-np.pi)
    print (n0,Nin,I[i],Dev[i])
    n0 *= 2
    
            
pyplot.plot(N,Dev,ls='-',c='red',lw=3,label='Deviation');
pyplot.plot(N,1/np.sqrt(N),ls='-',c='blue',lw=3, label='1/sqrt(N)');
pyplot.xscale('log')
pyplot.yscale('log')
pyplot.legend()
pyplot.title('RNG w/ a = 5, M = 11')