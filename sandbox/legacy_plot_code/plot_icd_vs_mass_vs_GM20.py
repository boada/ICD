#!/usr/bin/env python
# File: plot_icd_vs_mass.py
# Created on: Mon 12 Mar 2012 11:50:09 AM CDT
# Last Change: Mon Oct 29 11:08:34 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_icd_vs_mass():
    galaxies = mk_galaxy_struc()

    # Add the figures

    # Mass vs ICD plot I-H
    f1 = pyl.figure(1,figsize=(5,3.09))
    f1s1 = f1.add_subplot(111)

    #Upper and Lower limit arrow verts
    arrowup_verts = [[0.,0.], [-1., -1], [0.,0.], [0.,-2.],[0.,0.], [1, -1]]
    arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.], [0.,2.],[0.,0.], [1, 1]]


    for galaxy in galaxies:
        if galaxy.ston_I > 30.:
            if galaxy.ICD_IH > 0.25:
                f1s1.scatter(galaxy.z, 0.25, s=100, marker=None,
                verts=arrowup_verts)
            elif galaxy.ICD_IH < -0.05:
                f1s1.scatter(galaxy.z, -0.05, s=100, marker=None,
                verts=arrowdown_verts)
            elif galaxy.Spiral ==1:
                col1 = f1s1.text(galaxy.Mass, galaxy.ICD_IH, 's',color='r')
            elif galaxy.Elliptical ==1:
                col2 = f1s1.text(galaxy.Mass, galaxy.ICD_IH, 'e',color='g')
            elif galaxy.Uncertain ==1:
                col3 = f1s1.text(galaxy.Mass, galaxy.ICD_IH, 'u',color='b')
            else:
                print 'wtf?'

    ############
    # FIGURE 1 #
    ############
    f1s1.axvspan(3e7,1e9,facecolor='#FFFDD0',ec='None',zorder=0)
    f1s1.axvspan(1e11,1e12,facecolor='#FFFDD0',ec='None',zorder=0)
    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(-0.05,0.25)
    f1s1.hlines(0.0,3e7,1e12)

    # remove extra ticks
    #f1s1.xaxis.set_major_formatter(pyl.NullFormatter())

    #f1s2.set_xscale('log')
    #f1s2.set_xlim(3e7,1e12)
    #f1s2.set_ylim(-0.1,0.4)
    #f1s2.hlines(0.0,3e7,1e12)
    #f1s2.tick_params(axis='both',pad=7)

    # labels
    #f1xl=pyl.figtext(0.5,0.025,r"$Log_{10}(M_{\odot})$",fontsize=30,ha='center')
    #f1yl=pyl.figtext(0.025,0.5,r"$\xi[I,H]$",fontsize=30,ha='center',rotation='vertical')
    f1s1.set_xlabel(r"Mass [$M_{\odot}]$")
    f1s1.set_ylabel(r"$\xi[I,H]$")
    #pyl.savefig('icd_vs_mass_vs_GM20_IH.eps',bbox='tight')

    pyl.show()

if __name__=='__main__':
    plot_icd_vs_mass()
