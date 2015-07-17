#!/usr/bin/env python
# File: plot_color_vs_mass_vs_icd.py
# Created on: Mon 19 Mar 2012 12:01:47 PM CDT
# Last Change: Wed Oct  3 10:34:07 2012
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

    label =[]
    color = []
    mass = []
    sersic = []

    for galaxy in galaxies:
        if galaxy.ston_I >30. and galaxy.sersic <= 1.6 and galaxy.sersic >= 0.:
            if galaxy.sersic > 1.6:
                sersic.append(1.6)
            else:
                sersic.append(galaxy.sersic)
            #color.append(galaxy.Imag-galaxy.Hmag)
            color.append(galaxy.ICD_IH)
            mass.append(galaxy.Mass)
            label.append(galaxy.ID)

    # Sort the arrays by ICD
    mass = pyl.asarray(mass)
    color = pyl.asarray(color)
    sersic = pyl.asarray(sersic)

    IH_array = pyl.column_stack((mass,color,sersic,label))

    IH_array = colsort(IH_array,3)

    '''
    for label,x,y in zip(IH_array[:,3],IH_array[:,0], IH_array[:,1]):
        pyl.annotate(label,xy=(x,y),
            xytext=(x,y),textcoords='data',ha='right',va='bottom',
            bbox=dict(boxstyle='round,pad=0.5',fc='yellow',alpha=0.5),
            arrowprops=dict(arrowstyle='->'))
    '''

    sc1 = f1s1.scatter(IH_array[:,0], IH_array[:,1], c=IH_array[:,2], s=50,
    cmap='spectral')


    ############
    # FIGURE 1 #
    ############
    pyl.figure('CM_ICD_IH')

    bar = pyl.colorbar(sc1)
    bar.set_label("Sersic Index, n")

    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    #f1s1.set_ylim(-0.1,3.5)
    f1s1.set_ylim(-0.01,0.25)
    f1s1.set_xlabel(r"Mass $[M_{\odot}]$")
    f1s1.set_ylabel("$(I-H)_{Observed}$")

    pyl.subplots_adjust(left=0.15, bottom=0.15, right=.75)
   # pyl.savefig('color_vs_mass_vs_icd_IH.eps',bbox='tight')

    pyl.show()


if __name__=='__main__':
    plot_color_vs_mass_vs_icd()
