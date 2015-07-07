#!/usr/bin/env python
# File: plot_histograms3.py
# Created on: Mon Aug 20 22:14:33 2012
# Last Change: Mon Dec  3 10:27:58 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

galaxies = mk_galaxy_struc()

verylow = low = med = high = superhigh = 0.0
verylow2 = low2 = med2 = high2 = superhigh2 = 0.0

for galaxy in galaxies:
    if galaxy.ston_I >=30. and galaxy.sersic < 2:
        if -0.02 < galaxy.ICD_IH <= 0.04:
                verylow+=1
        if 0.04 < galaxy.ICD_IH <= 0.08:
                low+=1
        if 0.08 < galaxy.ICD_IH <= 0.12:
                med+=1
        if 0.12 < galaxy.ICD_IH <= 0.16:
                high+=1
        if 0.16 < galaxy.ICD_IH <= 0.20:
                superhigh+=1
    if galaxy.ston_I >=30. and galaxy.sersic > 2:
        if -0.02 < galaxy.ICD_IH <= 0.04:
                verylow2+=1
        if 0.04 < galaxy.ICD_IH <= 0.08:
                low2+=1
        if 0.08 < galaxy.ICD_IH <= 0.12:
                med2+=1
        if 0.12 < galaxy.ICD_IH <= 0.16:
                high2+=1
        if 0.16 < galaxy.ICD_IH <= 0.20:
                superhigh2+=1

pyl.figure(1,figsize=(5,3.09))

pyl.bar(-2,verylow/verylow,width=6, ec='k', fc=None, fill=False)
pyl.bar(4,low/verylow,width=4, ec='k', fc=None, fill=False)
pyl.bar(8,med/verylow,width=4, ec='k', fc=None, fill=False)
pyl.bar(12,high/verylow,width=4, ec='k', fc=None, fill=False)
pyl.bar(16,superhigh/verylow,width=4, ec='k', fc=None, fill=False)

pyl.bar(-1,verylow2/verylow2,width=6, ec='r', fc=None, fill=False)
pyl.bar(5,low2/verylow2,width=4, ec='r', fc=None, fill=False)
pyl.bar(9,med2/verylow2,width=4, ec='r', fc=None, fill=False)
pyl.bar(13,high2/verylow2,width=4, ec='r', fc=None, fill=False)
pyl.bar(17,superhigh2/verylow2,width=4, ec='r', fc=None, fill=False)

pyl.subplots_adjust(left=0.15, bottom=0.15)
pyl.xlabel("ICD")
pyl.ylabel(r"$N/N_{bin}$")
pyl.xticks([-2, 4, 8, 12, 16, 20])

pyl.savefig('sersic_icd_hist.eps',bbox='tight')

pyl.show()
