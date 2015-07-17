#!/usr/bin/env python
# File: plot_sersic_vs_icd_vs_colorgrad.py
# Created on: Thu 27 Sep 2012 11:09:10 AM CDT
# Last Change: Fri Sep 28 16:28:36 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_sersic_vs_icd_vs_colorgrad():
    galaxies = mk_galaxy_struc()

    f1 = pyl.figure(1,figsize=(8,8))
    f1s1 = f1.add_subplot(221)
    f1s2 = f1.add_subplot(222)
    f1s3 = f1.add_subplot(223)
    f1s4 = f1.add_subplot(224)

    for galaxy in galaxies:
        if galaxy.ston_I >30. and galaxy.sersic != None:
            if 1.5 < galaxy.z and  galaxy.z < 2.:
                col1 =f1s1.scatter(galaxy.sersic, galaxy.ICD_IH, s=50, c='r',
                        edgecolor='w',zorder=0,lw='1',label='1.5 < z < 2')
            if 2. < galaxy.z and  galaxy.z < 2.5:
                col2 =f1s2.scatter(galaxy.sersic, galaxy.ICD_IH, s=50, c='g',
                        edgecolor='w',zorder=1)
            if 2.5 < galaxy.z and  galaxy.z < 3.:
                col3 =f1s3.scatter(galaxy.sersic, galaxy.ICD_IH, s=50, c='b',
                        edgecolor='w',zorder=2)
            if 3. <  galaxy.z and galaxy.z < 3.5:
                col4 =f1s4.scatter(galaxy.sersic, galaxy.ICD_IH, s=50, c='k',
                        edgecolor='w',zorder=3)

    f1s1.set_xlim(-0.1,8.5)
    f1s1.set_ylim(-0.01,0.3)
    f1s2.set_xlim(-0.1,8.5)
    f1s2.set_ylim(-0.01,0.3)
    f1s3.set_xlim(-0.1,8.5)
    f1s3.set_ylim(-0.01,0.3)
    f1s4.set_xlim(-0.1,8.5)
    f1s4.set_ylim(-0.01,0.3)

    f1s1.legend([col1],['1.5 < z < 2'],scatterpoints=1)
    f1s2.legend([col2],['2 < z < 2.5'],scatterpoints=1)
    f1s3.legend([col3],['2.5 < z < 3'],scatterpoints=1)
    f1s4.legend([col4],['3 < z < 3.5'],scatterpoints=1)

    f1s1.set_xlabel('Sersic Index, n')
    f1s1.set_ylabel(r'$\xi[I,H]$')

    #pyl.subplots_adjust(left=0.15,bottom=0.15)

    pyl.savefig('sersic_vs_icd_vs_colorgrad.eps',bbox='tight')

    pyl.show()

if __name__ == '__main__':
    plot_sersic_vs_icd_vs_colorgrad()
