#!/usr/bin/env python
# File: plot_uvj_vs_icd.py
# Created on: Wed 07 Nov 2012 09:20:44 AM CST
# Last Change: Wed Jul 17 16:16:34 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mpl_toolkits.axes_grid1 import AxesGrid
#from mk_galaxy_struc import mk_galaxy_struc
import cPickle as pickle
from colsort import colsort

def plot_uvj_vs_icd():
    #galaxies=mk_galaxy_struc()
    galaxies = pickle.load(open('galaxies.pickle','rb'))
    #Take out the UDF data
    #galaxies = filter(lambda galaxy: galaxy.field == 1, galaxies)
    #galaxies = filter(lambda galaxy: -0.05 < galaxy.ICD_IH < 0.25, galaxies)
    galaxies = filter(lambda galaxy: galaxy.ICD_IH != None, galaxies)

    #f,(ax1, ax2) = pyl.subplots(1,2,sharex=True, sharey=True,figsize=(6.25,4.5))

    F = pyl.figure(1,figsize=(8,4))
    grid = AxesGrid(F, 111,
                        nrows_ncols=(1,3),
                        axes_pad = 0.1,
                        add_all=True,
                        label_mode = 'L',
                        share_all=True,
                        cbar_location = 'top',
                        cbar_mode = 'each')
    ax1 = grid[0]
    ax2 = grid[1]
    ax3 = grid[2]

    uv =[]
    vj =[]
    icd = []
    mass= []

    appenduv = uv.append
    appendvj = vj.append
    appendicd = icd.append
    appendmass = mass.append

    #Build Arrays
    for galaxy in galaxies:
        if galaxy.ston_I > 30.:
            appenduv(-2.5*pyl.log10(galaxy.Uflux_rest/galaxy.Vflux_rest))
            appendvj(-2.5*pyl.log10(galaxy.Vflux_rest/galaxy.Jflux_rest))
            if galaxy.ICD_IH > 0.5:
                appendicd(0.5)
            else:
                appendicd(galaxy.ICD_IH)
            appendmass(galaxy.Mass)

    x = [g for g in galaxies if g.ston_I > 30. and g.Mips != None]
    uv2 =[]
    vj2 =[]
    mips =[]
    appenduv2 = uv2.append
    appendvj2 = vj2.append
    appendmips = mips.append

    for galaxy in x:
        appenduv2(-2.5*pyl.log10(galaxy.Uflux_rest/galaxy.Vflux_rest))
        appendvj2(-2.5*pyl.log10(galaxy.Vflux_rest/galaxy.Jflux_rest))
        if galaxy.Mips > 45:
            appendmips(45.)
        else:
            appendmips(galaxy.Mips)

    #Convert to Numpy Array
    uv = pyl.asarray(uv)
    vj = pyl.asarray(vj)
    uv2 = pyl.asarray(uv2)
    vj2 = pyl.asarray(vj2)
    icd = pyl.asarray(icd)
    mass = pyl.asarray(mass)
    mips = pyl.asarray(mips)

    #Build Plotting Matrices
    cut = pyl.column_stack((uv, vj, icd*100., mass))
    cut3 = pyl.column_stack((uv2, vj2, mips))

    cut = colsort(cut,3)
    cut2 = colsort(cut,4)
    cut3 = colsort(cut3,3) 

    #plot!
    sc1 = ax1.scatter(cut[:,1], cut[:,0], c=cut[:,2], s=50, cmap='Spectral')
    sc2 = ax2.scatter(cut2[:,1], cut2[:,0], c=cut2[:,3], s=50, cmap='Spectral')
    sc3 = ax3.scatter(cut3[:,1], cut3[:,0], c=cut3[:,2], s=50, cmap='Spectral')

    #Add Lines
    ax1.set_ylim(-0.5,2.5)
    ax1.set_xlim(-1.5,2.5)

    limits = ax1.axis()
    ax1.axis
    #x = [limits[0], 0.69, 1.4,1.4]
    #y = [1.2, 1.2, 1.82, limits[3]]
    x = [limits[0], 0.92, 1.6,1.6]
    y = [1.3, 1.3, 1.89, limits[3]]

    ax1.plot(x,y,lw=2,c='k')
    ax2.plot(x,y,lw=2,c='k')
    ax3.plot(x,y,lw=2,c='k')

    #Add the color bar and labels and stuff
    grid.cbar_axes[0].colorbar(sc1)
    grid.cbar_axes[1].colorbar(sc2)
    grid.cbar_axes[2].colorbar(sc3)

    ax = grid.cbar_axes[0]
    ax.axis["top"].toggle(ticks=True, ticklabels=True, label=True)
    ax.set_xlabel(r'$\xi[i_{775},H_{160}]$ (%)', fontsize=16)
    ax = grid.cbar_axes[1]
    ax.set_xlabel(r'Log Mass $(M_\odot)$', fontsize=16)
    ax = grid.cbar_axes[2]
    ax.set_xlabel(r'24$\mu$m ($\mu$Jy)', fontsize=16)

    grid.axes_llc.set_xticks([-1,0,1,2])
    grid.axes_llc.set_yticks([0,1,2])

    ax1.set_ylabel('$(U-V)_{Rest}$')
    ax1.set_xlabel('$(V-J)_{Rest}$')
    ax2.set_xlabel('$(V-J)_{Rest}$')
    ax3.set_xlabel('$(V-J)_{Rest}$')

    pyl.tight_layout()
    pyl.savefig('UVJ_vs_icd_mass.eps',bbox='tight')
    pyl.show()

if __name__ =='__main__':
    plot_uvj_vs_icd()
