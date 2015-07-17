#!/usr/bin/env python
# File: plot_histograms3.py
# Created on: Mon Aug 20 22:14:33 2012
# Last Change: Wed Feb 13 16:24:31 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

galaxies = mk_galaxy_struc()

verylow = low = med = high = superhigh = 0.0
verylow2 = low2 = med2 = high2 = superhigh2 = 0.0
verylow3 = low3 = med3 = high3 = superhigh3 = 0.0
verylow4 = low4 = med4 = high4 = superhigh4 = 0.0

for galaxy in galaxies:
    if galaxy.ston_I >=30. and galaxy.sersic < 1:
        if -0.02 < galaxy.ICD_IH <= 0.04:
                verylow += 1.
        if 0.04 < galaxy.ICD_IH <= 0.08:
                low += 1.
        if 0.08 < galaxy.ICD_IH <= 0.12:
                med += 1.
        if 0.12 < galaxy.ICD_IH <= 0.16:
                high += 1.
        if 0.16 < galaxy.ICD_IH <= 0.20:
                superhigh += 1.
    elif galaxy.ston_I >= 30. and 1 < galaxy.sersic < 2:
        if -0.02 < galaxy.ICD_IH <= 0.04:
                verylow2 += 1.
        if 0.04 < galaxy.ICD_IH <= 0.08:
                low2 += 1.
        if 0.08 < galaxy.ICD_IH <= 0.12:
                med2 += 1.
        if 0.12 < galaxy.ICD_IH <= 0.16:
                high2 += 1.
        if 0.16 < galaxy.ICD_IH <= 0.20:
                superhigh2 += 1.
    elif galaxy.ston_I >= 30. and 2 < galaxy.sersic < 3:
        if -0.02 < galaxy.ICD_IH <= 0.04:
                verylow3 += 1.
        if 0.04 < galaxy.ICD_IH <= 0.08:
                low3 += 1.
        if 0.08 < galaxy.ICD_IH <= 0.12:
                med3 += 1.
        if 0.12 < galaxy.ICD_IH <= 0.16:
                high3 += 1.
        if 0.16 < galaxy.ICD_IH <= 0.20:
                superhigh3 += 1.
    elif galaxy.ston_I >= 30. and 3 < galaxy.sersic:
        if -0.02 < galaxy.ICD_IH <= 0.04:
                verylow4 += 1.
        if 0.04 < galaxy.ICD_IH <= 0.08:
                low4 += 1.
        if 0.08 < galaxy.ICD_IH <= 0.12:
                med4 += 1.
        if 0.12 < galaxy.ICD_IH <= 0.16:
                high4 += 1.
        if 0.16 < galaxy.ICD_IH <= 0.20:
                superhigh4 += 1.

f1, f1s = pyl.subplots(1, 4,figsize=(9.5,3))
f1s1 = f1s[0]
f1s2 = f1s[1]
f1s3 = f1s[2]
f1s4 = f1s[3]

total = verylow + low + med + high + superhigh
total2 = verylow2 + low2 + med2 + high2 + superhigh2
total3 = verylow3 + low3 + med3 + high3 + superhigh3
total4 = verylow4 + low4 + med4 + high4 + superhigh4

labels = r'$\xi$<4%', r'4%<$\xi$<8%', r'8%<$\xi$<12%', r'12%<$\xi$<16%', r'16%<$\xi$<20%'

fractions = [verylow/total, low/total, med/total, high/total, superhigh/total]
p=f1s1.pie(fractions, autopct='%1.f%%', pctdistance=1.2, shadow=True)
f1s1.legend((p[0]),labels,loc=(-0.1,-0.5), ncol=5)
pyl.figtext(.15, .2, 'n < 1', fontsize=18, ha='center')


fractions = [verylow2/total2, low2/total2, med2/total2, high2/total2,
            superhigh2/total2]
f1s2.pie(fractions, autopct='%1.f%%', pctdistance=1.2, shadow=True)
pyl.figtext(.37, .2, '1 < n < 2', fontsize=18, ha='center')


fractions = [verylow3/total3, low3/total3, med3/total3, high3/total3,
            superhigh3/total3]
f1s3.pie(fractions, autopct='%1.f%%', pctdistance=1.2, shadow=True)
pyl.figtext(.59, .2, '1 < n < 2', fontsize=18, ha='center')

fractions = [verylow4/total4, low4/total4, med4/total4, high4/total4,
            superhigh4/total4]
f1s4.pie(fractions, autopct='%1.f%%', pctdistance=1.2, shadow=True)
pyl.figtext(.82, .2, '3 < n', fontsize=18, ha='center')

pyl.subplots_adjust(left=0.05, bottom=0.30)
#pyl.tight_layout()
pyl.savefig('sersic_icd_pie.eps',bbox='tight')

pyl.show()
