#!/usr/bin/env python
# File: plot_uvj_vs_icd.py
# Created on: Wed 07 Nov 2012 09:20:44 AM CST
# Last Change: Tue Jun 25 15:09:28 2013
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
    galaxies = filter(lambda galaxy: galaxy.ICD_IH != None, galaxies)

    F = pyl.figure(1,figsize=(8,3))
    grid = AxesGrid(F, 111,
            nrows_ncols=(1,4),
            axes_pad = 0.1,
            add_all=True,
            aspect=False,
            share_all = True)

    ax1 = grid[0]
    ax2 = grid[1]
    ax3 = grid[2]
    ax4 = grid[3]

    for galaxy in galaxies:
            if galaxy.ston_I >30. and galaxy.sersic != None:
                if galaxy.sersic < 1.:
                    col1 =ax1.scatter(galaxy.Mass, galaxy.ICD_IH * 100.,
                        s=50, c='k', edgecolor='w')
                if 1. < galaxy.sersic < 2.:
                        col2 =ax2.scatter(galaxy.Mass, galaxy.ICD_IH * 100.,
                            s=50, c='k', edgecolor='w')
                if 2. < galaxy.sersic < 3.:
                        col3 =ax3.scatter(galaxy.Mass, galaxy.ICD_IH * 100.,
                            s=50, c='k', edgecolor='w')
                if 3. <  galaxy.sersic:
                        col4 =ax4.scatter(galaxy.Mass, galaxy.ICD_IH * 100.,
                            s=50, c='k', edgecolor='w')

    #ax1.semilogx()
    #ax2.semilogx()
    #ax3.semilogx()
    #ax4.semilogx()

    #ax1.set_ylim(-5, 25)
    #ax1.set_xlim(3e7,1e12)

    ax1.set_xticks([8, 9, 10, 11])
    ax2.set_xticks([8, 9, 10, 11])
    ax3.set_xticks([8, 9, 10, 11])
    ax4.set_xticks([8, 9, 10, 11])

    ax1.set_ylabel(r'$\xi[i_{775},H_{160}]$ (%)')
    ax1.set_title('n < 1')
    ax2.set_title('1 < n < 2')
    ax3.set_title('2 < n < 3')
    ax4.set_title('3 < n')

    pyl.figtext(.5, .05, r'Mass $(M_{\odot})$',fontsize=18,
        horizontalalignment='center')
    pyl.subplots_adjust(bottom=0.21, left=0.1)
    ax1.axhline(0, lw=2, zorder=0)
    ax2.axhline(0, lw=2, zorder=0)
    ax3.axhline(0, lw=2, zorder=0)
    ax4.axhline(0, lw=2, zorder=0)

    #pyl.tight_layout()
    pyl.show()

if __name__ =='__main__':
    plot_uvj_vs_icd()
