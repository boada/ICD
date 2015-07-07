#!/usr/bin/env python
# File: plot_histograms3.py
# Created on: Mon Aug 20 22:14:33 2012
# Last Change: Tue Jan 15 16:03:45 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

galaxies = mk_galaxy_struc()
verylow =[]
low =[]
med=[]
high=[]

appendverylow = verylow.append
appendlow = low.append
appendmed = med.append
appendhigh = high.append

for galaxy in galaxies:
    if galaxy.ston_I >=30.:
        if 0.04 <= galaxy.ICD_IH and galaxy.ICD_IH <= 0.11:
                appendlow(galaxy.z)
        if 0.11 <= galaxy.ICD_IH and galaxy.ICD_IH <= 0.18:
                appendmed(galaxy.z)
        if 0.18 <= galaxy.ICD_IH and galaxy.ICD_IH <= 0.25:
                appendhigh(galaxy.z)
        else:
                appendverylow(galaxy.z)

verylow1 = verylow2=verylow3=verylow4 = 0
low_1 = low_2 = low_3 = low_4 = 0
med_1 = med_2 = med_3 = med_4 = 0
high_1 = high_2 = high_3 = high_4 = 0


for z in verylow:
    if 1.5 < z and z < 2.0:
        verylow1 +=1
    if 2.0 < z and z < 2.5:
        verylow2 +=1
    if 2.0 < z and z < 2.5:
        verylow3 +=1
    if 3.0 < z and z < 3.5:
        verylow4 +=1

for z in low:
    if 1.5 < z and z < 2.0:
        low_1 +=1
    if 2.0 < z and z < 2.5:
        low_2 +=1
    if 2.0 < z and z < 2.5:
        low_3 +=1
    if 3.0 < z and z < 3.5:
        low_4 +=1
for z in med:
    if 1.5 < z and z < 2.0:
        med_1 +=1
    if 2.0 < z and z < 2.5:
        med_2 +=1
    if 2.0 < z and z < 2.5:
        med_3 +=1
    if 3.0 < z and z < 3.5:
        med_4 +=1
for z in high:
    if 1.5 < z and z < 2.0:
        high_1 +=1
    if 2.0 < z and z < 2.5:
        high_2 +=1
    if 2.0 < z and z < 2.5:
        high_3 +=1
    if 3.0 < z and z < 3.5:
        high_4 +=1

total1 = float(low_1 + med_1 + high_1 +verylow1)
total2 = float(low_2 + med_2 + high_2 +verylow2)
total3 = float(low_3 + med_3 + high_3 +verylow3)
total4 = float(low_4 + med_4 + high_4 +verylow4)

f1, f1s = pyl.subplots(4, 1, figsize=(3,9))
f1s1 = f1s[0]
f1s2 = f1s[1]
f1s3 = f1s[2]
f1s4 = f1s[3]

labels = '1.5 < z < 2.0', '2.0 < z < 2.5', '2.5 < z < 3.0', '3.0 < z < 3.5'

fractions =[verylow1/total1, low_1/total1, med_1/total1, high_1/total1]
f1s1.pie(fractions, autopct='%1.f%%', pctdistance=1.2, shadow=True)

fractions =[verylow2/total2, low_2/total2, med_2/total2, high_2/total2]
f1s2.pie(fractions, autopct='%1.f%%', pctdistance=1.2, shadow=True)

fractions =[verylow3/total3, low_3/total3, med_3/total3, high_3/total3]
f1s3.pie(fractions, autopct='%1.f%%', pctdistance=1.2, shadow=True)

fractions =[verylow4/total4, low_4/total4, med_4/total4, high_4/total4]
f1s4.pie(fractions, autopct='%1.f%%', pctdistance=1.2, shadow=True)

# Tweak the plot.

#pyl.legend(loc='center right')

#pyl.subplots_adjust(left=0.15, bottom=0.15)
#pyl.xlabel("Redshift")
#pyl.ylabel(r"$N/N_{bin}$")

#pyl.savefig('icd_vs_z_hist_IH.eps',bbox='tight')

pyl.show()
