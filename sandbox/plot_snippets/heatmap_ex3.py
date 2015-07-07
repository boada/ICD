#!/usr/bin/env python
# File: heatmap_ex3.py
# Created on: Tue 07 Aug 2012 02:13:55 PM CDT
# Last Change: Tue 07 Aug 2012 02:16:44 PM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada
import numpy as np
import numpy.random
import matplotlib.pyplot as plt

# Generate some test data
#x = np.random.randn(8873)
#y = np.random.randn(8873)


import math as m
from mk_galaxy_struc import mk_galaxy_struc
galaxies = mk_galaxy_struc()
x=[]
y=[]
for galaxy in galaxies:
    if galaxy.ston_I >30.:
        x.append(m.log10(galaxy.Mass))
        y.append(galaxy.ICD_IH)

heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap, extent=extent)
plt.show()
