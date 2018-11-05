# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 21:06:50 2018

@author: Ben
"""
import numpy as np

def rng(N):
    a = 5 
    M = 11
    r = np.zeros(N+1)
    R = np.zeros(N+1)
    r[0] = 1
    for i in range(1,N+1):
        r[i] = (a*r[i-1])%M
        R[i] = float(r[i])/float(M)
    return R

def rng_ibm(N): 
    a = 65539 
    M =  2**31
    r = np.zeros(N+1)
    R = np.zeros(N+1)
    r[0] = 1
    for i in range(1,N+1):
        r[i] = (a*r[i-1])%M
        R[i] = float(r[i])/float (M)
    return R