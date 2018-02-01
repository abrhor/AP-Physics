#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 01:50:37 2018

@author: student
"""
# only works for [a,b] = [0,b] because np.arange includes a as element/term
# only works for f(x) = sin(x) because I forgot how to pass a function as argument to a function

import numpy as np

def R(n, a, b):
    k = step = (b-a)/n
    x = np.arange(a, b + k, k)
    app = np.sin(x)
    s = np.sum(app)
    return (1/n)*s

print(R(10000.,0.,np.pi))