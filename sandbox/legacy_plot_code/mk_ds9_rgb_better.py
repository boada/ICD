#!/usr/bin/env python
# File: mk_ds9_rgb.py
# Created on: Mon 18 Jun 2012 11:20:57 AM CDT
# Last Change: Fri 05 Oct 2012 04:01:24 PM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import numpy as np
import sys
import os
import stat


# read info files from comamnd line
#data = np.loadtxt(sys.argv[1])

#Does the same thing...
from mk_galaxy_struc import mk_galaxy_struc
galaxies = mk_galaxy_struc()
galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)

#Enable sorting by a keyword
#import operator
#galaxies.sort(key=operator.attrgetter('Mass'))


if len(galaxies) %  100  == 0:
    a = len(galaxies) % 100
else:
    a = len(galaxies) % 100 +1


for i in range(1,a):
    # open output file
    f1 = open('display_stamps'+str(i)+'.sh','wt')

    # write everything to a single line
    f1.writelines('#!/bin/bash\n')
    f1.writelines('ds9 ')

    
    for galaxy in galaxies:

        ID = galaxy.ID
        icd = galaxy.ICD_IH
        mass = np.log10(galaxy.Mass)
        #s = galaxy.Spiral
        #e = galaxy.Elliptical
        #u = galaxy.Uncertain
        z = galaxy.z
        #grad = galaxy.Color_grad

        if galaxy.field ==1:
            # make the images
            f1.writelines('-rgb ')
            f1.writelines('-blue gsd_'+str(int(ID))+'_I.fits ')
            f1.writelines('-green gsd_'+str(int(ID))+'_J.fits ')
            f1.writelines('-red gsd_'+str(int(ID))+'_H.fits ')
            color='white'
        elif galaxy.field ==2:
            # make the images
            f1.writelines('-rgb ')
            f1.writelines('-blue gsd_'+str(int(ID))+'_I.fits ')
            f1.writelines('-green gsd_'+str(int(ID))+'_J.fits ')
            f1.writelines('-red gsd_'+str(int(ID))+'_H.fits ')
            color='yellow'
        else:
            print 'ERROR!!!'
            break

        # set color
        #if icd >= 0.04 and s == 1 and grad <= 0 and grad != None:
        #if icd >= 0.04 and grad <= 0 and grad != None:
        #    color = 'yellow'
        #else:
        #    color = 'white'

        # add info
        f1.writelines('-regions command ')
        label = "'"+str(int(ID))+"'"
        f1.writelines('"circle 10 30 0 #color='+color+' text='+label+'" ')

        f1.writelines('-regions command ')
        z1 = "'%3.2f'" % z
        f1.writelines('"circle 31 30 0 #color='+color+' text='+z1+'" ')

        f1.writelines('-regions command ')
        icd1 = "'%4.2f'" % icd
        f1.writelines('"circle 35 0 0 #color='+color+' text='+icd1+'" ')

        f1.writelines('-regions command ')
        mass = "'%4.2f'" % mass
        f1.writelines('"circle 12 0 0 #color='+color+' text='+mass+'" ')

        #f1.writelines('-regions command ')
        #icd1 = "'%4.2f'" % icd
        #f1.writelines('"circle 31 30 0 #color='+color+' text='+icd1+'" ')

        # if s ==1:
        #     kind ="'"+str('s')+"'"
        # elif e ==1:
        #     kind ="'"+str('e')+"'"
        # elif u ==1:
        #     kind ="'"+str('m')+"'"
        # else:
        #     kind ="'"+str('???')+"'"
        # f1.writelines('-regions command ')
        # f1.writelines('"circle 35 0 0 #color='+color+' text='+kind+'" ')

        #if grad != None:
        #    grad = "'%4.3f'" % grad
        #else:
        #    grad = 'None'
        #f1.writelines('"circle 12 0 0 #color='+color+' text='+grad+'" ')

        if i == a*100


    f1.close()

#os.fchmod('display_stamps.sh',stat.S_IXUSR)

