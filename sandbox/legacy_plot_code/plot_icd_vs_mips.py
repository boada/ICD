#!/usr/bin/env python
# File: plot_icd_vs_mips.py
# Created on: Fri 15 Jun 2012 11:19:08 AM CDT
# Last Change: Fri 15 Jun 2012 11:50:20 AM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_icd_vs_mips():
    galaxies = mk_galaxy_struc()

    f1 = pyl.figure(1,figsize=(6,4))
    f1s1 = f1.add_subplot(111)

    # Upper and Lower limit arrow verts
    arrowup_verts = [[0.,0.], [-1., -1], [0.,0.], [0.,-2.],[0.,0.], [1,-1]]
    arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.], [0.,2.],[0.,0.], [1,1]]

    for i in range(len(galaxies)):
        if galaxies[i].ston_I > 30.:
            if not galaxies[i].Mips == -1:
                f1s1.scatter(galaxies[i].Mips, galaxies[i].ICD_IH, c='#F28500',
                marker='o')
                if galaxies[i].ICD_IH > 0.25:
                    f1s1.scatter(galaxies[i].Mips,0.25,s=100,marker=None,
                    verts=arrowup_verts)
                if galaxies[i].ICD_IH < -0.05:
                    f1s1.scatter(galaxies[i].Mips,-0.05,s=100,marker=None,
                    verts=arrowdown_verts)

    pyl.subplots_adjust(left=0.17,bottom=0.18)
    f1s1.tick_params(axis='both',pad=7)#,labelsize=15)
    f1s1.set_ylim(-0.05,0.25)
    f1s1.set_xlabel(r"$F_{24\mu m}$",fontsize=18)
    f1s1.set_ylabel(r"$\xi[I,H]$",fontsize=18)
    pyl.show()
if __name__=='__main__':
    plot_icd_vs_mips()
