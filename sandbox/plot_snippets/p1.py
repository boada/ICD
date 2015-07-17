#!/usr/bin/env python
# File: plot_icd_vs_mass.py
# Created on: Mon 12 Mar 2012 11:50:09 AM CDT
# Last Change: Fri Sep 28 15:47:02 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_icd_vs_mass():
    galaxies = mk_galaxy_struc()

    # Add the figures

    # Mass vs ICD plot I-H
    f1 = pyl.figure(1,figsize=(6,4))
    f1s1 = f1.add_subplot(211)

    #Upper and Lower limit arrow verts
    arrowup_verts = [[0.,0.], [-1., -1], [0.,0.], [0.,-2.],[0.,0.], [1, -1]]
    arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.], [0.,2.],[0.,0.], [1, 1]]


    for i in range(len(galaxies)):
        if galaxies[i].ston_I > 30.0:
            f1s1.scatter(galaxies[i].Mass, galaxies[i].ICD_IH,
            c='#F28500', s=50, zorder=2)
            #Add upper limit arrows
            if galaxies[i].ICD_IH > 0.25:
                f1s1.scatter(galaxies[i].Mass,0.25,s=100,marker=None,
                verts=arrowup_verts)
            if galaxies[i].ICD_IH < -0.05:
                f1s1.scatter(galaxies[i].Mass,-0.05,s=100,marker=None,
                verts=arrowdown_verts)

    ############
    # FIGURE 1 #
    ############
    pyl.figure(1)

    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(-0.05,0.25)
    f1s1.hlines(0.0,3e7,1e12)

    # labels
    f1s1.set_xlabel(r"Mass [$M_{\odot}]$")
    f1s1.set_ylabel(r"$\xi[I,H]$")

#    pyl.show()

    return f1s1

if __name__=='__main__':
    plot_icd_vs_mass()
