#!/usr/bin/env python
# File: plot_color_vs_mass_vs_icd.py
# Created on: Mon 19 Mar 2012 12:01:47 PM CDT
# Last Change: Tue Jun 25 14:14:47 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
#from mk_galaxy_struc import mk_galaxy_struc
import cPickle as pickle
from mpl_toolkits.axes_grid1 import AxesGrid
from colsort import colsort


def plot_color_vs_mass_vs_icd():
    #galaxies=mk_galaxy_struc()
    galaxies = pickle.load(open('galaxies.pickle','rb'))

    F = pyl.figure(1, figsize=(6,3.5))
    grid = AxesGrid(F, 111, nrows_ncols=(1,1), add_all=True, label_mode='L',
        cbar_location='right', cbar_mode='each', aspect=False)

    color1 = []
    mass1 = []
    icd1 = []
    color2 = []
    mass2 = []
    icd2 = []

    for galaxy in galaxies:
        if galaxy.ston_I > 30. and galaxy.ICD_IH != None:
            mass1.append(galaxy.Mass)
            color1.append(galaxy.Imag-galaxy.Hmag)
            icd1.append(pyl.log10(galaxy.ICD_IH*100))
            '''
            if galaxy.ICD_IH < -0.05:
                mass1.append(galaxy.Mass)
                color1.append(galaxy.Imag-galaxy.Hmag)
                icd1.append(-0.05*100)
            elif -0.05 < galaxy.ICD_IH < 0.25:
                mass1.append(galaxy.Mass)
                color1.append(galaxy.Imag-galaxy.Hmag)
                icd1.append(galaxy.ICD_IH*100.)
            else:
                mass1.append(galaxy.Mass)
                color1.append(galaxy.Imag-galaxy.Hmag)
                icd1.append(0.25*100.)
            '''
        elif galaxy.ICD_IH != None:
            mass2.append(galaxy.Mass)
            color2.append(galaxy.Imag-galaxy.Hmag)
            icd2.append(galaxy.ICD_IH*100)

    # Sort the arrays by ICD
    mass1 = pyl.asarray(mass1)
    color1 = pyl.asarray(color1)
    icd1 = pyl.asarray(icd1)

    IH_array = pyl.column_stack((mass1,color1,icd1))
    IH_array = colsort(IH_array,3)

    #sc2 = grid[0].scatter(mass2, icd2, c='0.8', s=20)
    sc1 = grid[0].scatter(IH_array[:,0], IH_array[:,1], c=IH_array[:,2], s=50,
    cmap='spectral')

    grid.cbar_axes[0].colorbar(sc1)
    grid.cbar_axes[0].set_ylabel(r'Log $\xi[i_{775},H_{160}]$ (%)')

    #grid[0].set_xscale('log')
    #grid[0].set_xlim(3e7,1e12)
    #grid[0].set_ylim(0.0,3.5)
    grid[0].set_xlabel(r"Log Mass $(M_{\odot})$")
    grid[0].set_ylabel("$(i_{775}-H_{160})_{Observed}$")
    grid[0].set_yticks([0,1,2,3])
    grid[0].set_xticks([8,9,10,11,12])

    #pyl.tight_layout()
    #pyl.savefig('color_vs_mass_vs_icd_IH.eps',bbox='tight')

    pyl.show()


if __name__=='__main__':
    plot_color_vs_mass_vs_icd()
