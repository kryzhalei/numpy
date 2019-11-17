# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:52:35 2019

@author: Kryzha Lei Aguilar
"""

import numpy as np

A = np.arange(1,101).reshape(10,10)
print ("The matrix is\n"+str(A*A))

B = (A*A)%3
x, y = np.where (B == 0)

C = A*A
D = C[x,y]

print ("The elements that are divisible by 3 are \n"+str(D))