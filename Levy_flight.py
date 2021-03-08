# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:06:29 2021

@author: ZongSing_NB
"""

import numpy as np
import math
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------

size = 100
pt = np.zeros([size, 2])
#------------------------------------------------------------------------------

beta = 1.5
sigma_v = 1
sigma_u = ( ( math.gamma(1+beta)*np.sin(np.pi*beta/2) ) / ( beta*math.gamma((1+beta)/2)*2**((beta-1)/2) ) )**(1/beta)

for i in range(size-1):
    u = np.random.normal(0, sigma_u**2, size=1)
    v = np.random.normal(0, sigma_v**2, size=1)
    s1 = u/(np.abs(v)**(1/beta))
    
    u = np.random.normal(0, sigma_u, size=1)
    v = np.random.normal(0, sigma_v, size=1)
    s2 = u/(np.abs(v)**(1/beta))

    pt[i+1, 0] = pt[i, 0] + s1
    pt[i+1, 1] = pt[i, 1] + s2
#------------------------------------------------------------------------------

plt.figure(0)
plt.plot(pt[:, 0], pt[:, 1])
plt.show()

