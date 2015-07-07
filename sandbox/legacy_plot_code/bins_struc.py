#File: bins_struc.py
#Created: Wed 06 Jun 2012 03:20:41 PM CDT
#Last Change: Tue 12 Jun 2012 03:43:41 PM CDT
#Author: Steven Boada

import numpy as np
import math as m
from mk_galaxy_struc import mk_galaxy_struc
from drange import drange

sample = []
# get galaxy info
galaxies = mk_galaxy_struc()
for i in range(len(galaxies)):
	if galaxies[i].ston_I > 30.0 and galaxies[i].ICD_IH <= 0.25:
		sample.append([galaxies[i].ICD_IH,galaxies[i].Mass])

sample = np.asarray(sample)

# make the bins
bins = []
for i in drange(7.0,12.5,0.1):
	bins.append(10.0**i)
bins = np.asarray(bins)

# digitize the sample
inds = np.digitize(sample[:,1],bins)

# put the sample in the postboxes
sorted =[]
for i in range(bins.size):
	sorted.append([])
for i in range(inds.size):
	j = int(inds[i])
       	sorted[j].append(i)

# match the sample to the icd's
for i in range(bins.size):
	for j in range(len(sorted[i][:])):
		sorted[i][j] = sample[sorted[i][j]][0]
	

# sort the bins
values = []
for i in range(bins.size):
	x = np.sort(np.asarray(sorted[i][:]))
	y = round(0.50*len(x)+0.5)
	try:
		print x[y-1]
		values.append(x[y-1])
	except:
		print '0.0'
		values.append(0.0)

values = np.asarray(values)
