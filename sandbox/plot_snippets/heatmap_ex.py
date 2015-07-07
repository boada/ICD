#!/usr/bin/env python
# File: heatmap_ex.py
# Created on: Tue 07 Aug 2012 01:48:35 PM CDT
# Last Change: Tue 07 Aug 2012 02:06:20 PM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP
import math as m

from mk_galaxy_struc import mk_galaxy_struc
galaxies = mk_galaxy_struc()
mass=[]
icd=[]
for galaxy in galaxies:
    if galaxy.ston_I >30.:
        mass.append(m.log10(galaxy.Mass))
        icd.append(galaxy.ICD_IH)

n = 1e5
x = NP.linspace(min(mass), max(mass), 100)
y = NP.linspace(-0.01, 0.25, 100)
X, Y = NP.meshgrid(x, y)
Z1 = ML.bivariate_normal(X, Y, 2, 2, 0, 0)
Z2 = ML.bivariate_normal(X, Y, 4, 1, 1, 1)
ZD = Z2 - Z1
x = X.ravel()
y = Y.ravel()
z = ZD.ravel()
gridsize=30
PLT.subplot(111)

# if 'bins=None', then color of each hexagon corresponds directly to its count
# 'C' is optional--it maps values to x-y coordinates; if 'C' is None (default)
# then 
# the result is a pure 2D histogram 

PLT.hexbin(mass, icd, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
PLT.axis([x.min(), x.max(), y.min(), y.max()])

cb = PLT.colorbar()
cb.set_label('mean value')
PLT.show()
