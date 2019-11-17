# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:48:35 2019

@author: Kryzha Lei Aguilar
"""

import numpy as np

X = np.random.random((5,5))
DataMean = np.mean(X)
StandardDev = np.std(X)

Z = (X-DataMean)/StandardDev

print (Z)