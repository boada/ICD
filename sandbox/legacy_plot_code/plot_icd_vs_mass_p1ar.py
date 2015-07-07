#!/usr/bin/env python
# File: plot_icd_vs_mass.py
# Created on: Mon 12 Mar 2012 11:50:09 AM CDT
# Last Change: Thu Feb 28 17:11:01 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_icd_vs_mass():
    galaxies = mk_galaxy_struc()
    galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)

    # Mass vs ICD plot I-H
    f1 = pyl.figure(1,figsize=(6,4))
    f1s1 = f1.add_subplot(111)

    #Upper and Lower limit arrow verts
    arrowup_verts = [[0.,0.], [-1., -1], [0.,0.], [0.,-2.],[0.,0.], [1, -1]]
    arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.], [0.,2.],[0.,0.], [1, 1]]

    for galaxy in galaxies:
        f1s1.scatter(galaxy.Mass, galaxy.ICD_IH*100., c='r', s=50)


        #if galaxies[i].ICD_IH > 0.25:
        #    f1s1.scatter(galaxies[i].Mass,0.25*100.,s=100,marker=None,
        #    verts=arrowup_verts)
        #if galaxies[i].ICD_IH < -0.05:
        #    f1s1.scatter(galaxies[i].Mass,-0.05*100.,s=100,marker=None,
        #    verts=arrowdown_verts)

    ############
    # FIGURE 1 #
    ############
    pyl.figure(1)

    #f1s1.axvspan(3e7,1e9,facecolor='#FFFDD0',ec='None',zorder=0)
    #f1s1.axvspan(1e11,1e12,facecolor='#FFFDD0',ec='None',zorder=0)
    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(-5,25)
    f1s1.hlines(0.0,3e7,1e12)

    #f1s2.set_xscale('log')
    #f1s2.set_xlim(3e7,1e12)
    #f1s2.set_ylim(-0.1,0.4)
    #f1s2.hlines(0.0,3e7,1e12)
    f1s1.set_xlabel(r"Mass ($M_{\odot})$")
    f1s1.set_ylabel("ICD[F775W, F160W] (%)")
    pyl.tight_layout()


    pyl.show()

if __name__=='__main__':
    plot_icd_vs_mass()
