#!/usr/bin/env python
# File: plot_uvj_vs_icd.py
# Created on: Wed 07 Nov 2012 09:20:44 AM CST
# Last Change: Thu Jan 17 12:08:36 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mpl_toolkits.axes_grid1 import AxesGrid
from mk_galaxy_struc import mk_galaxy_struc
from colsort import colsort

def plot_uvj_vs_icd():
    galaxies=mk_galaxy_struc()
    #Take out the UDF data
    galaxies = filter(lambda galaxy: galaxy.field == 1, galaxies)
    galaxies = filter(lambda galaxy: -0.05 < galaxy.ICD_IH < 0.25, galaxies)

    #f,(ax1, ax2) = pyl.subplots(1,2,sharex=True, sharey=True,figsize=(6.25,4.5))

    F = pyl.figure(1,figsize=(6,3.1))
    grid = AxesGrid(F, 111,
                        nrows_ncols=(1,2),
                        axes_pad = 0.1,
                        add_all=True,
                        label_mode = 'L',
                        share_all=True,
                        cbar_location = 'top',
                        cbar_mode = 'single')
    ax1 = grid[0]
    ax2 = grid[1]

    uv =[]
    vj =[]
    icd = []
    uv_all =[]
    vj_all =[]
    icd_all = []

    appenduv = uv.append
    appendvj = vj.append
    appendicd = icd.append
    appenduv_all = uv_all.append
    appendvj_all = vj_all.append
    appendicd_all = icd_all.append

    #Build Arrays
    for galaxy in galaxies:
        if galaxy.ston_I >30. and galaxy.ston_H > 30.:
            appenduv(-2.5*pyl.log10(galaxy.Uflux_rest/galaxy.Vflux_rest))
            appendvj(-2.5*pyl.log10(galaxy.Vflux_rest/galaxy.Jflux_rest))
            appendicd(pyl.log10(galaxy.Mass))
        appenduv_all(-2.5*pyl.log10(galaxy.Uflux_rest/galaxy.Vflux_rest))
        appendvj_all(-2.5*pyl.log10(galaxy.Vflux_rest/galaxy.Jflux_rest))
        appendicd_all(pyl.log10(galaxy.Mass))


    #Convert to Numpy Array
    uv = pyl.asarray(uv)
    vj = pyl.asarray(vj)
    icd = pyl.asarray(icd)
    uv_all = pyl.asarray(uv_all)
    vj_all = pyl.asarray(vj_all)
    icd_all = pyl.asarray(icd_all)

    #Build Plotting Matrices
    cut = pyl.column_stack((uv,vj,icd))
    total = pyl.column_stack((uv_all,vj_all,icd_all))

    cut = colsort(cut,3)
    total = colsort(total,3)

    #plot!
    sc1 = ax1.scatter(total[:,1], total[:,0], c=total[:,2], s=50,
            cmap='spectral')
    sc2 = ax2.scatter(cut[:,1], cut[:,0], c=cut[:,2], s=50,
            cmap='spectral')

    #Add Lines
    ax1.set_ylim(-0.5,2.5)
    ax1.set_xlim(-1.5,2.5)

    limits = ax1.axis()
    ax1.axis
    x = [limits[0], 0.69, 1.4,1.4]
    y = [1.2, 1.2, 1.82, limits[3]]

    ax1.plot(x,y,lw=2,c='k')
    ax2.plot(x,y,lw=2,c='k')

    #Add the color bar and labels and stuff
    grid.cbar_axes[0].colorbar(sc2)
    ax = grid.cbar_axes[0]
    ax.axis["top"].toggle(ticks=True, ticklabels=True, label=True)
    ax.set_xlabel('Log Mass $[M_{\odot}]$')

    grid.axes_llc.set_xticks([-1,0,1,2])
    grid.axes_llc.set_yticks([0,1,2])

    ax1.set_ylabel('$U-V_{Rest}$')
    ax1.set_xlabel('$V-J_{Rest}$')
    ax2.set_xlabel('$V-J_{Rest}$')

    #pyl.savefig('UVJ_vs_mass.eps',bbox='tight')
    pyl.show()

if __name__ =='__main__':
    plot_uvj_vs_icd()
