#!/usr/bin/env python
# File: plot_sersic_vs_icd_vs_colorgrad.py
# Created on: Thu 27 Sep 2012 11:09:10 AM CDT
# Last Change: Thu Mar 21 14:36:14 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_sersic_vs_icd_vs_colorgrad():
    galaxies = mk_galaxy_struc()

    #f1 = pyl.figure(1,figsize=(8,8))
    #f1s1 = f1.add_subplot(221)
    #f1s2 = f1.add_subplot(222, sharex=f1s1, sharey=f1s1)
    #f1s3 = f1.add_subplot(223, sharex=f1s1, sharey=f1s1)
    #f1s4 = f1.add_subplot(224, sharex=f1s1, sharey=f1s1)

    f1, f1s = pyl.subplots(2, 2, sharex=True, sharey=True,figsize=(5,5))
    f1s1 = f1s[0][0]
    f1s2 = f1s[0][1]
    f1s3 = f1s[1][0]
    f1s4 = f1s[1][1]

    for galaxy in galaxies:
        if galaxy.ston_I >30. and galaxy.sersic != None:
            if galaxy.sersic < 1.:
                col1 =f1s1.scatter((galaxy.Mass), galaxy.ICD_IH * 100., s=50, c='k',
                        edgecolor='w',zorder=2)
            if 1. < galaxy.sersic < 2.:
                col2 =f1s2.scatter((galaxy.Mass), galaxy.ICD_IH * 100., s=50, c='k',
                        edgecolor='w',zorder=0,lw='1')
            if 2. < galaxy.sersic < 3.:
                col3 =f1s3.scatter((galaxy.Mass), galaxy.ICD_IH * 100., s=50, c='k',
                        edgecolor='w',zorder=1)
            if 3. <  galaxy.sersic:
                col4 =f1s4.scatter((galaxy.Mass), galaxy.ICD_IH * 100., s=50, c='k',
                        edgecolor='w',zorder=3)

    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(-5,25)
    f1s1.hlines(0.0,3e7,1e12)
    f1s1.vlines(5e10,-5,25)

    f1s2.set_xscale('log')
    f1s2.set_xlim(3e7,1e12)
    f1s2.set_ylim(-5,25)
    f1s2.hlines(0.0,3e7,1e12)
    f1s2.vlines(5e10,-5,25)

    f1s3.set_xscale('log')
    f1s3.set_xlim(3e7,1e12)
    f1s3.set_ylim(-5,25)
    f1s3.hlines(0.0,3e7,1e12)
    f1s3.vlines(5e10,-5,25)

    f1s4.set_xscale('log')
    f1s4.set_xlim(3e7,1e12)
    f1s4.set_ylim(-5,25)
    f1s4.hlines(0.0,3e7,1e12)
    f1s4.vlines(5e10,-5,25)

    #f1s1.legend([col1],['n < 1'],scatterpoints=1)
    #f1s2.legend([col2],['1 < n < 2'],scatterpoints=1)
    #f1s3.legend([col3],['2 < n < 3.'],scatterpoints=1)
    #f1s4.legend([col4],['3 < n'],scatterpoints=1)

    pyl.figtext(0.4, 0.80, 'n < 1', ha='center')
    pyl.figtext(0.6, 0.80, '1 < n < 2', ha='center')
    pyl.figtext(0.4, 0.45, '2 < n < 3', ha='center')
    pyl.figtext(0.6, 0.45, '3 < n', ha='center')

    f1s1.set_yticks([0,5,10,15,20])
    f1s1.set_xticks([1e8,1e9,1e10,1e11])

    pyl.figtext(0.025, 0.5, r'$\xi[I,H]$ (%)', fontsize=20, va='center', rotation='vertical')
    pyl.figtext(0.5, 0.025, 'Mass ($M_\odot$)', fontsize=20, ha='center')

    pyl.subplots_adjust(hspace=0.0, wspace=0.0, bottom=0.14, left=0.14)

    #pyl.savefig('icd_vs_mass_vs_sersic_bins_IH.eps',bbox='tight')

    pyl.show()

if __name__ == '__main__':
    plot_sersic_vs_icd_vs_colorgrad()
