#!/usr/bin/env python
# File: add_hist_lines.py
# Created on: Mon Oct 22 14:56:24 2012
# Last Change: Mon Oct 22 15:36:16 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

from hist_overlap import hist_overlap
from mk_galaxy_struc import mk_galaxy_struc
import numpy as np

# make some bins
start = 1.5
stop = 3.5
step = 0.1

lower = np.arange(start,stop-step,step)
upper = np.arange(start+ 2.*step,stop+step,step)

# build bin array
bins = []
bins_append = bins.append
for x,y in zip(lower,upper):
    bins_append((x,y))

galaxies = mk_galaxy_struc()
galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)

# build data array
data = []
data_append=data.append
data_total = []
data_total_append=data_total.append
for galaxy in galaxies:
    if galaxy.ICD_IH > 0.04:
        data_append(galaxy.z)
    data_total_append(galaxy.z)

number, bin_centers = hist_overlap(data,bins)
number_total, bin_centers = hist_overlap(data_total,bins)

fraction = []
fraction_append = fraction.append
for n,n_t in zip(number,number_total):
    fraction_append(float(n)/float(n_t))


