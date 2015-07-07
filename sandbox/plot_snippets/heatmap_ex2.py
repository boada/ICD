#!/usr/bin/env python
# File: heatmap_ex2.py
# Created on: Tue 07 Aug 2012 02:08:46 PM CDT
# Last Change: Tue 07 Aug 2012 02:11:26 PM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import numpy as np
import matplotlib.pyplot as plt

import math as m
from mk_galaxy_struc import mk_galaxy_struc
galaxies = mk_galaxy_struc()
x=[]
y=[]
for galaxy in galaxies:
    if galaxy.ston_I >30.:
        x.append(m.log10(galaxy.Mass))
        y.append(galaxy.ICD_IH)

#x = [1,2,3,4,5,5]
#y = [1,2,3,4,5,5]
heatmap, xedges, yedges = np.histogram2d(x, y, bins=10)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.imshow(heatmap, extent = extent)
ax1.set_title("imshow Default");
ax2 = fig.add_subplot(212)
ax2.imshow(heatmap, extent = extent,origin='lower')
ax2.set_title("imshow origin='lower'")

plt.show()
