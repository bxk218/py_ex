# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:31:07 2016

@author: Administrator
"""

import numpy as np

x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
             [[21, 22, 23], [24, 25, 26], [27, 28, 29]]])
             
y = x[1:2, 1:2]
             
print(x[1,1])
print(x[:,1,1])
print(x[1,:,1])
print()
print(y)
