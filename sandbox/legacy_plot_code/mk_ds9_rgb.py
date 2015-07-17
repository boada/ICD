#!/usr/bin/env python
# File: mk_ds9_rgb.py
# Created on: Mon 18 Jun 2012 11:20:57 AM CDT
# Last Change: Tue Mar  5 11:46:25 2013
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

#Enable sorting by a keyword
import operator
galaxies.sort(key=operator.attrgetter('ICD_IH'))

for a in range(1,600,100):
    # open output file
    f1 = open('display_stamps_contours'+str(a)+'.sh','wt')

    # write everything to a single line
    f1.writelines('#!/bin/bash\n')
    f1.writelines('ds9 ')

    #for ID, icd, mass, s, e, u in zip(data[:,1], data[:,2], data[:,3], data[:,4],
    #        data[:,5], data[:,6]):

    i =1

    for galaxy in galaxies:

        ID = galaxy.ID
        icd = galaxy.ICD_IH
        #mass = np.log10(galaxy.Mass)
        sersic = galaxy.sersic
        #s = galaxy.Spiral
        #e = galaxy.Elliptical
        #u = galaxy.Uncertain
        z = galaxy.z
        #grad = galaxy.Color_grad

        if galaxy.ston_I >= 30.:
            if i >= a:
                if galaxy.field ==1:
                    base ='./GSD_IJH_20kpc/'
                # make the images
                    f1.writelines('-rgb ')
                    f1.writelines('-blue '+base+'GSD_'+str(int(ID))+'_I.fits ')
                    f1.writelines('-green '+base+'GSD_'+str(int(ID))+'_J.fits ')
                    f1.writelines('-red '+base+'GSD_'+str(int(ID))+'_H.fits ')
                    color='white'
                    f1.writelines('-regions command ')
                    label = "'"+str(int(ID))+"'"
                    f1.writelines('"circle 10 30 0 #color='+color+' text='+label+'" ')

                    f1.writelines('-regions command ')
                    z1 = "'%3.2f'" % z
                    f1.writelines('"circle 31 30 0 #color='+color+' text='+z1+'" ')

                    f1.writelines('-regions command ')
                    icd1 = "'%4.2f'" % icd
                    f1.writelines('"circle 31 0 0 #color='+color+' text='+icd1+'" ')

                    #f1.writelines('-regions command ')
                    #mass = "'%4.2f'" % mass
                    #f1.writelines('"circle 12 0 0#color='+color+' text='+mass+'" ')
                    f1.writelines('-regions command ')
                    if sersic != None:
                        sersic = "'%3.2f'" % sersic
                        f1.writelines('"circle 12 0 0 #color='+color+' text='+sersic+'" ')
                    else:
                        sersic =-1
                        sersic = "'%3.2f'" % sersic
                        f1.writelines('"circle 12 0 0 #color='+color+' text='+sersic+'" ')
                    base ='./GSD_contours/'
                    f1.writelines('-contour load '+base+'GSD_'+str(int(ID))+'_seg.con ')

                elif galaxy.field==2:
                    base ='./UDF_IJH_20kpc/'
                    f1.writelines('-rgb ')
                    f1.writelines('-blue '+base+'UDF_'+str(int(ID))+'_I.fits ')
                    f1.writelines('-green '+base+'UDF_'+str(int(ID))+'_J.fits ')
                    f1.writelines('-red '+base+'UDF_'+str(int(ID))+'_H.fits ')
                    color='yellow'
                    f1.writelines('-regions command ')
                    label = "'"+str(int(ID))+"'"
                    f1.writelines('"circle 20 60 0 #color='+color+' text='+label+'" ')

                    f1.writelines('-regions command ')
                    z1 = "'%3.2f'" % z
                    f1.writelines('"circle 62 60 0 #color='+color+' text='+z1+'" ')

                    f1.writelines('-regions command ')
                    icd1 = "'%4.2f'" % icd
                    f1.writelines('"circle 62 0 0 #color='+color+' text='+icd1+'" ')

                    #f1.writelines('-regions command ')
                    #mass = "'%4.2f'" % mass
                    #f1.writelines('"circle 24 0 0#color='+color+' text='+mass+'" ')

                    f1.writelines('-regions command ')
                    if sersic != None:
                        sersic = "'%3.2f'" % sersic
                        f1.writelines('"circle 24 0 0 #color='+color+' text='+sersic+'" ')
                    else:
                        sersic =-1
                        sersic = "'%3.2f'" % sersic
                        f1.writelines('"circle 24 0 0 #color='+color+' text='+sersic+'" ')
                    base ='./UDF_contours/'
                    f1.writelines('-contour load '+base+'UDF_'+str(int(ID))+'_seg.con ')

            i+=1

            if i > a+99:
                break
        else:
            pass

    f1.close()

#os.fchmod('display_stamps.sh',stat.S_IXUSR)

