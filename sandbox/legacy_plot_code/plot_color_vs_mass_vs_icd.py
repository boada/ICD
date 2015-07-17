#!/usr/bin/env python
# File: plot_color_vs_mass_vs_icd.py
# Created on: Mon 19 Mar 2012 12:01:47 PM CDT
# Last Change: Mon Feb 18 16:51:17 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc
from colsort import colsort


def plot_color_vs_mass_vs_icd():
    galaxies=mk_galaxy_struc()
    # Add the figures

#    pyl.rcParams.update(mplparams.aps['params'])

    # Mass vs color plot I-H
    f1 = pyl.figure('CM_ICD_IH',figsize=(6,4))
    f1s1 = f1.add_subplot(111)

    # Mass vs color plot J-H
    f2 = pyl.figure('CM_ICD_ZH',figsize=(8,8))
    f2s1 = f2.add_subplot(111)

    # Mass vs color plot Z-H
    f3 = pyl.figure('CM_ICD_JH',figsize=(8,8))
    f3s1 = f3.add_subplot(111)

    color1 = []
    mass1 = []
    icd1 = []
    color2 = []
    mass2 = []
    icd2 = []
    color3 = []
    mass3 = []
    icd3 = []

    for i in range(len(galaxies)):
        if galaxies[i].ston_I >30.0:
            if -0.05 < galaxies[i].ICD_IH and galaxies[i].ICD_IH < 0.25:
                mass1.append(galaxies[i].Mass)
                color1.append(galaxies[i].Imag-galaxies[i].Hmag)
                icd1.append(galaxies[i].ICD_IH*100.)
            else:
                mass1.append(galaxies[i].Mass)
                color1.append(galaxies[i].Imag-galaxies[i].Hmag)
                icd1.append(0.25*100.)

        if galaxies[i].ston_Z >30.0:
            if -0.05 < galaxies[i].ICD_ZH and galaxies[i].ICD_ZH < 0.25:
                mass2.append(galaxies[i].Mass)
                color2.append(galaxies[i].Zmag-galaxies[i].Hmag)
                icd2.append(galaxies[i].ICD_ZH)
            else:
                mass2.append(galaxies[i].Mass)
                color2.append(galaxies[i].Zmag-galaxies[i].Hmag)
                icd2.append(0.3)

        if galaxies[i].ston_J >30.0:
            if -0.05 < galaxies[i].ICD_JH and galaxies[i].ICD_JH < 0.25:
                mass3.append(galaxies[i].Mass)
                color3.append(galaxies[i].Jmag-galaxies[i].Hmag)
                icd3.append(galaxies[i].ICD_JH)
            else:
                mass3.append(galaxies[i].Mass)
                color3.append(galaxies[i].Jmag-galaxies[i].Hmag)
                icd3.append(0.3)

    # Sort the arrays by ICD
    mass1 = pyl.asarray(mass1)
    color1 = pyl.asarray(color1)
    icd1 = pyl.asarray(icd1)
    mass2 = pyl.asarray(mass2)
    color2 = pyl.asarray(color2)
    icd2 = pyl.asarray(icd2)
    mass3 = pyl.asarray(mass3)
    color3 = pyl.asarray(color3)
    icd3 = pyl.asarray(icd3)

    IH_array = pyl.column_stack((mass1,color1,icd1))
    ZH_array = pyl.column_stack((mass2,color2,icd2))
    JH_array = pyl.column_stack((mass3,color3,icd3))

    IH_array = colsort(IH_array,3)
    ZH_array = colsort(ZH_array,3)
    JH_array = colsort(JH_array,3)

    sc1 = f1s1.scatter(IH_array[:,0], IH_array[:,1], c=IH_array[:,2], s=50,
    cmap='spectral',edgecolor='w')
    sc2 = f2s1.scatter(ZH_array[:,0], ZH_array[:,1], c=ZH_array[:,2], s=50,
    cmap='spectral')
    sc3 = f3s1.scatter(JH_array[:,0], JH_array[:,1], c=JH_array[:,2], s=50,
    cmap='spectral')


    ############
    # FIGURE 1 #
    ############
    pyl.figure('CM_ICD_IH')

    bar = pyl.colorbar(sc1)
    bar.set_label(r"$\xi[I,H]$ (%)")

    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(0.0,3.5)
    f1s1.set_xlabel(r"Mass $[M_{\odot}]$")
    f1s1.set_ylabel("$(I-H)_{Observed}$")

    pyl.subplots_adjust(left=0.16, bottom=0.23, right=0.74)
    #pyl.tight_layout()
    pyl.savefig('color_vs_mass_vs_icd_IH.eps',bbox='tight')

    ############
    # FIGURE 2 #
    ############
    pyl.figure('CM_ICD_ZH')
    bar = pyl.colorbar(sc2)
    bar.set_label(r"$\xi[Z,H]$",fontsize=20)

    f2s1.set_xscale('log')
    f2s1.set_xlim(3e7,1e12)
    f2s1.set_ylim(0.0,3.5)
    f2s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
    f2s1.set_ylabel("$(Z-H)_{Observed}$",fontsize=20)
    f2s1.tick_params(axis='both',pad=7)
    pyl.savefig('color_vs_mass_vs_icd_ZH.eps')

    ############
    # FIGURE 3 #
    ############
    pyl.figure('CM_ICD_JH')
    bar = pyl.colorbar(sc3)
    bar.set_label(r"$\xi[J,H]$",fontsize=20)

    f3s1.set_xscale('log')
    f3s1.set_xlim(3e7,1e12)
    f3s1.set_ylim(-0.5,1.5)
    f3s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
    f3s1.set_ylabel("$(J-H)_{Observed}$",fontsize=20)
    f3s1.tick_params(axis='both',pad=7)
    pyl.savefig('color_vs_mass_vs_icd_JH.eps')

    pyl.show()


if __name__=='__main__':
    plot_color_vs_mass_vs_icd()
