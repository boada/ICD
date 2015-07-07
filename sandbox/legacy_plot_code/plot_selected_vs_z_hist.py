#!/usr/bin/env python
# File: plot_selected_vs_z_hist.py
# Created on: Mon Aug 20 21:04:20 2012
# Last Change: Fri 28 Sep 2012 10:21:27 AM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

galaxies = mk_galaxy_struc()

low =[]
med=[]
high=[]

appendlow = low.append
appendmed = med.append
appendhigh = high.append

for galaxy in galaxies:
    if galaxy.ston_I >30. and galaxy.ICD_IH <0.25:
        if 0.04 <= galaxy.ICD_IH and galaxy.ICD_IH <= 0.11:
            appendlow(galaxy.z)
        if 0.11 <= galaxy.ICD_IH and galaxy.ICD_IH <= 0.18:
            appendmed(galaxy.z)
        if 0.18 <= galaxy.ICD_IH and galaxy.ICD_IH <= 0.25:
            appendhigh(galaxy.z)

count, bins, ignored = pyl.hist((low, med, high),
    label = (r"$0.04 \leq \xi[I,H] \leq 0.11$",
            r"$0.11 \leq \xi[I,H] \leq 0.18$",
             r"$0.18 \leq \xi[I,H] \leq 0.25$"),
         bins=2, histtype='barstacked')

pyl.legend(loc='upper right')

pyl.savefig('selected_galaxy_hist.eps',bbox='tight')


pyl.show()

