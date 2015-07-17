#!/usr/bin/env python
# File: plot_color_vs_mass_vs_icd.py
# Created on: Mon 19 Mar 2012 12:01:47 PM CDT
# Last Change: Fri 28 Sep 2012 12:40:00 PM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc
from colsort import colsort


def plot_color_vs_mass_vs_icd():
    galaxies=mk_galaxy_struc()
    # Add the figures

    # Mass vs color plot I-H
    f1 = pyl.figure(1,figsize=(6,4))
    f1s1 = f1.add_subplot(212)


    color1 = []
    mass1 = []
    icd1 = []

    for i in range(len(galaxies)):
        if galaxies[i].ston_I >30.0:
            if -0.05 < galaxies[i].ICD_IH and galaxies[i].ICD_IH < 0.25:
                mass1.append(galaxies[i].Mass)
                color1.append(galaxies[i].Imag-galaxies[i].Hmag)
                icd1.append(galaxies[i].ICD_IH)
            else:
                mass1.append(galaxies[i].Mass)
                color1.append(galaxies[i].Imag-galaxies[i].Hmag)
                icd1.append(0.25)

    # Sort the arrays by ICD
    mass1 = pyl.asarray(mass1)
    color1 = pyl.asarray(color1)
    icd1 = pyl.asarray(icd1)

    IH_array = pyl.column_stack((mass1,color1,icd1))

    IH_array = colsort(IH_array,3)

    sc1 = f1s1.scatter(IH_array[:,0], IH_array[:,1], c=IH_array[:,2], s=50,
    cmap='spectral')


    ############
    # FIGURE 1 #
    ############

    bar = pyl.colorbar(sc1)
    bar.set_label(r"$\xi[I,H]$")

    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(0.0,4.0)
    f1s1.set_xlabel(r"Mass $[M_{\odot}]$")
    f1s1.set_ylabel("$(I-H)_{Observed}$")

#    pyl.subplots_adjust(left=0.15, bottom=0.15, right=.75)
#    pyl.savefig('color_vs_mass_vs_icd_IH.eps',bbox='tight')
    return f1s1

if __name__=='__main__':
    plot_color_vs_mass_vs_icd()
