#!/usr/bin/env python
# File: collect_stamps.py
# Created on: Fri 15 Jun 2012 10:11:00 AM CDT
# Last Change: Mon 18 Jun 2012 11:10:48 AM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pyfits as pyf
from mk_galaxy_struc import mk_galaxy_struc

galaxies = mk_galaxy_struc()

f1 = open('lowMass.list','wt')
f2 = open('medMass_lowicd.list','wt')
f3 = open('medMass_highicd.list','wt')
f4 = open('highMass.list','wt')

f1.writelines('#field #ID #ICD_IH #MASS #SPIRAL #ELLIPTICAL #UNCERTAIN\n')
f2.writelines('#field #ID #ICD_IH #MASS #SPIRAL #ELLIPTICAL #UNCERTAIN\n')
f3.writelines('#field #ID #ICD_IH #MASS #SPIRAL #ELLIPTICAL #UNCERTAIN\n')
f4.writelines('#field #ID #ICD_IH #MASS #SPIRAL #ELLIPTICAL #UNCERTAIN\n')

for i in range(len(galaxies)):
    if galaxies[i].ston_I >= 30.0:
        if galaxies[i].Mass <= 1e9:
            f1.writelines(str(galaxies[i].field)+' '+str(galaxies[i].ID)+\
                   ' '+str(galaxies[i].ICD_IH)+' '+str(galaxies[i].Mass)+\
                   ' '+str(galaxies[i].Spiral)+' '+str(galaxies[i].Elliptical)+\
                   ' '+str(galaxies[i].Uncertain)+'\n')
        elif 1e9 <= galaxies[i].Mass and galaxies[i].Mass <= 1e11:
            if galaxies[i].ICD_IH <= 0.05:
                f2.writelines(str(galaxies[i].field)+' '+str(galaxies[i].ID)+\
                   ' '+str(galaxies[i].ICD_IH)+' '+str(galaxies[i].Mass)+\
                   ' '+str(galaxies[i].Spiral)+' '+str(galaxies[i].Elliptical)+\
                   ' '+str(galaxies[i].Uncertain)+'\n')
            else:
                f3.writelines(str(galaxies[i].field)+' '+str(galaxies[i].ID)+\
                   ' '+str(galaxies[i].ICD_IH)+' '+str(galaxies[i].Mass)+\
                   ' '+str(galaxies[i].Spiral)+' '+str(galaxies[i].Elliptical)+\
                   ' '+str(galaxies[i].Uncertain)+'\n')
        elif 1e11 <= galaxies[i].Mass:
            f4.writelines(str(galaxies[i].field)+' '+str(galaxies[i].ID)+\
                ' '+str(galaxies[i].ICD_IH)+' '+str(galaxies[i].Mass)+\
                ' '+str(galaxies[i].Spiral)+' '+str(galaxies[i].Elliptical)+\
                ' '+str(galaxies[i].Uncertain)+'\n')

f1.close()
f2.close()
f3.close()
f4.close()
