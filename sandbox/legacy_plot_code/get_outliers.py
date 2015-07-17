#!/usr/bin/env python
# File: get_outliers.py
# Created on: Wed Feb 20 14:12:45 2013
# Last Change: Thu Feb 21 16:02:23 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

from mk_galaxy_struc import mk_galaxy_struc
from random import choice

galaxies = mk_galaxy_struc()

galaxies = filter(lambda galaxy: galaxy.ston_I >30., galaxies)

high_group = [galaxy.ID for galaxy in galaxies if galaxy.ICD_IH > 0.25]
group = [galaxy.ID for galaxy in galaxies if 0.1 > galaxy.ICD_IH > 0 and
    galaxy.field ==1]
low_group =[choice(group) for i in range(len(high_group))]

with open('outlierstamps.sh','wt') as f1:
    f1.writelines('#/bin/bash\n')
    f1.writelines('ds9 ')

    base1 = './GSD_IJH_20kpc/'
    base2 = './GSD_IaH_colormaps/'
    base3 = './GSD_SEGS/'

    for ID in low_group:
        f1.writelines('-frame new -file ')
        f1.writelines(base2+'GSD_'+str(int(ID))+'I_a_H.fits ')
    for ID in low_group:
        f1.writelines('-frame new -file ')
        f1.writelines(base3+'GSD_'+str(int(ID))+'_seg.fits ')
    for ID in low_group:
        f1.writelines('-rgb ')
        f1.writelines('-blue '+base1+'GSD_'+str(int(ID))+'_I.fits ')
        f1.writelines('-green '+base1+'GSD_'+str(int(ID))+'_J.fits ')
        f1.writelines('-red '+base1+'GSD_'+str(int(ID))+'_H.fits ')


    for ID in high_group:
        f1.writelines('-frame new -file ')
        f1.writelines(base2+'GSD_'+str(int(ID))+'I_a_H.fits ')
    for ID in high_group:
        f1.writelines('-frame new -file ')
        f1.writelines(base3+'GSD_'+str(int(ID))+'_seg.fits ')
    for ID in high_group:
        f1.writelines('-rgb ')
        f1.writelines('-blue '+base1+'GSD_'+str(int(ID))+'_I.fits ')
        f1.writelines('-green '+base1+'GSD_'+str(int(ID))+'_J.fits ')
        f1.writelines('-red '+base1+'GSD_'+str(int(ID))+'_H.fits ')


