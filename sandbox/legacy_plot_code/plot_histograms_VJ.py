#!/usr/bin/env python
# File: plot_histograms3.py
# Created on: Mon Aug 20 22:14:33 2012
# Last Change: Mon Oct 22 09:54:21 2012
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
    if galaxy.ston_I >=30. and galaxy.Color_grad < 0. and galaxy.Color_grad !=\
None:
        if 0.04 <= galaxy.ICD_VJ and galaxy.ICD_VJ <= 0.11:
                appendlow(galaxy.z)
        if 0.11 <= galaxy.ICD_VJ and galaxy.ICD_VJ <= 0.18:
                appendmed(galaxy.z)
        if 0.18 <= galaxy.ICD_VJ and galaxy.ICD_VJ <= 0.25:
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

total_1 = float(low_1 + med_1 + high_1 +verylow1)
total_2 = float(low_2 + med_2 + high_2 +verylow2)
total_3 = float(low_3 + med_3 + high_3 +verylow3)
total_4 = float(low_4 + med_4 + high_4 +verylow4)

pyl.bar(1.5,verylow1/total_1,width=0.5, ec='k', fc='w', \
    label=r"$\xi[V,J] \leq 0.04$")
pyl.bar(2.,verylow2/total_2,width=0.5, ec='k', fc='w')
pyl.bar(2.5,verylow3/total_3,width=0.5, ec='k', fc='w')
pyl.bar(3.,verylow4/total_4,width=0.5, ec='k', fc='w')

bot1 = verylow1/total_1
bot2 = verylow2/total_2
bot3 = verylow3/total_3
bot4 = verylow4/total_4

pyl.bar(1.5,low_1/total_1,width=0.5, ec='k', fc='b', \
    label=r"$0.04 \leq \xi[V,J] \leq 0.11$",bottom=bot1)
pyl.bar(2.0,low_2/total_2,width=0.5, ec='k', fc='b',bottom=bot2)
pyl.bar(2.5,low_3/total_3,width=0.5, ec='k', fc='b',bottom=bot3)
pyl.bar(3.0,low_4/total_4,width=0.5, ec='k', fc='b',bottom=bot4)

bot1 = verylow1/total_1 +low_1/total_1
bot2 = verylow2/total_2 +low_2/total_2
bot3 = verylow3/total_3 +low_3/total_3
bot4 = verylow4/total_4 +low_4/total_4

pyl.bar(1.5,med_1/total_1,width=0.5, ec='k', fc='r', \
    label=r"$0.11 \leq \xi[V,J] \leq 0.18$",bottom=bot1)
pyl.bar(2.,med_2/total_2,width=0.5, ec='k', fc='r',bottom=bot2)
pyl.bar(2.5,med_3/total_3,width=0.5, ec='k', fc='r',bottom=bot3)
pyl.bar(3.0,med_4/total_4,width=0.5, ec='k', fc='r',bottom=bot4)

bot1 = (verylow1+low_1+med_1)/total_1
bot2 = (verylow2+low_2+med_2)/total_2
bot3 = (verylow3+low_3+med_3)/total_3
bot4 = (verylow4+low_4+med_4)/total_4

pyl.bar(1.5,high_1/total_1,width=0.5, ec='k', fc='g', \
    label=r"$0.18 \leq \xi[V,J] \leq 0.25$",bottom=bot1)
pyl.bar(2.,high_2/total_2,width=0.5, ec='k', fc='g',bottom=bot2)
pyl.bar(2.5,high_3/total_3,width=0.5, ec='k', fc='g',bottom=bot3)
pyl.bar(3.,high_4/total_4,width=0.5, ec='k', fc='g',bottom=bot4)

pyl.legend(loc='center right')

pyl.xlabel("Redshift")
pyl.ylabel(r"$N/N_{total}$")


pyl.savefig('icd_vs_z_hist_VJ.eps')

pyl.show()
