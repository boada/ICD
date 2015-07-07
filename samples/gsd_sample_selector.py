#!/usr/bin/env python
# File: gsd_sample_selector.py
# Created on: Tue Oct 30 14:17:45 2012
# Last Change: Wed May 29 12:03:10 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import sys
from numpy import loadtxt, genfromtxt
from mk_magnitude import mk_magnitude
from load_fits import load_fits


def dowork(i, redshift, flux, z, f1):
    fluxi = flux[redshift[i][0]-1][16]
    fluxz = flux[redshift[i][0]-1][19]
    fluxj = flux[redshift[i][0]-1][31]
    fluxh = flux[redshift[i][0]-1][34]
    if fluxi > 0.0 and fluxz > 0.0 and fluxj > 0.0 and fluxh > 0.0:
        magI = mk_magnitude(fluxi,'uJy')
        magZ = mk_magnitude(fluxz,'uJy')
        magJ = mk_magnitude(fluxj,'uJy')
        magH = mk_magnitude(fluxh,'uJy')
        if magH < 25.0:
            print int(redshift[i][0])
            f1.writelines(str(int(redshift[i][0]))+" ")
            f1.writelines(str(flux[i][2])+" ")
            f1.writelines(str(flux[i][3])+" ")
            f1.writelines(str(magI)+" ")
            f1.writelines(str(magZ)+" ")
            f1.writelines(str(magJ)+" ")
            f1.writelines(str(magH)+" ")
            f1.writelines(str(z)+"\n")

def gsd_sample_selector():

    base = "/Users/steven/Projects/image_fields/CANDELS/GOODS_S_complete/catalogs/"
    redshift = loadtxt(base+"gs_all_tf_h_120919a_PHOTOZ.v1.0.cat")
    flux =genfromtxt(base+"gs_all_tf_h_130511b_multi.cat")

    f1 = open('sample_1.5_3.5_gs_all2.txt','wt')
    for i in range(len(redshift[:,0])):
        if 1.5 <= redshift[i][5] <= 3.5: #spec-z's
            z = redshift[i][5]
            dowork(i, redshift, flux, z, f1)
        elif 1.5 <= redshift[i][9] <=3.5 and redshift[i][5] < 0: #photo-z's
            z = redshift[i][9]
            dowork(i, redshift, flux, z, f1)
        else:
            pass


    f1.close()

if __name__ == '__main__':
    sys.exit(gsd_sample_selector())

