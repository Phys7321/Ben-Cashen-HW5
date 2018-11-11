# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:52:28 2018

@author: Ben
"""

import numpy as np

# Simple Monte Carlo integration
n0 = 1000000
r = np.random.random(n0)

Itot = np.sum(r**2)
print("Simple Monte Carlo: ", Itot/n0)

x = np.sqrt(r)                
Itot = np.sum(x/2)              # P(x) = 2x -----> f(x)/P(x) = x/2
print("Importance Sampling: ", Itot/n0)