#!/usr/bin/env python
# File: plot_icd_vs_mass.py
# Created on: Mon 12 Mar 2012 11:50:09 AM CDT
# Last Change: Thu Oct  4 15:47:52 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_icd_vs_mass():
    galaxies = mk_galaxy_struc()

    # Add the figures

    # Mass vs ICD plot I-H
    f1 = pyl.figure(1,figsize=(8,8))
    f1s1 = f1.add_subplot(221)
    f1s2 = f1.add_subplot(222)
    f1s3 = f1.add_subplot(223)
    f1s4 = f1.add_subplot(224)

    #Upper and Lower limit arrow verts
    arrowup_verts = [[0.,0.], [-1., -1], [0.,0.], [0.,-2.],[0.,0.], [1, -1]]
    arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.], [0.,2.],[0.,0.], [1, 1]]


    for galaxy in galaxies:
        if galaxy.ston_I > 30. and galaxy.sersic != None:
            if 1.5 < galaxy.z and galaxy.z < 2.:
                if galaxy.ICD_IH > 0.25:
                    f1s1.scatter(galaxy.Mass,0.25,s=100,marker=None,
                    verts=arrowup_verts)
                elif galaxy.ICD_IH < -0.05:
                    f1s1.scatter(galaxy.Mass,-0.05,s=100,marker=None,
                    verts=arrowdown_verts)
                else:
                    col1 = f1s1.scatter((galaxy.Mass),galaxy.ICD_IH,
                    s=50, c='r', edgecolor='w')
            if 2. < galaxy.z and galaxy.z < 2.5:
                if galaxy.ICD_IH > 0.25:
                    f1s2.scatter(galaxy.Mass,0.25,s=100,marker=None,
                    verts=arrowup_verts)
                elif galaxy.ICD_IH < -0.05:
                    f1s2.scatter(galaxy.Mass,-0.05,s=100,marker=None,
                    verts=arrowdown_verts)
                else:
                    col2 = f1s2.scatter((galaxy.Mass),galaxy.ICD_IH,
                    s=50, c='g', edgecolor='w')
            if 2.5 < galaxy.z and galaxy.z < 3.:
                if galaxy.ICD_IH > 0.25:
                    f1s3.scatter(galaxy.Mass,0.25,s=100,marker=None,
                    verts=arrowup_verts)
                elif galaxy.ICD_IH < -0.05:
                    f1s3.scatter(galaxy.Mass,-0.05,s=100,marker=None,
                    verts=arrowdown_verts)
                else:
                    col3 = f1s3.scatter((galaxy.Mass),galaxy.ICD_IH,
                    s=50, c='b', edgecolor='w')
            if 3. < galaxy.z and galaxy.z < 3.5:
                if galaxy.ICD_IH > 0.25:
                    f1s4.scatter(galaxy.Mass,0.25,s=100,marker=None,
                    verts=arrowup_verts)
                elif galaxy.ICD_IH < -0.05:
                    f1s4.scatter(galaxy.Mass,-0.05,s=100,marker=None,
                    verts=arrowdown_verts)
                else:
                    col4 = f1s4.scatter((galaxy.Mass),galaxy.ICD_IH,
                    s=50, c='k', edgecolor='w')


    f1s1.legend([col1],['1.5 < z < 2'],scatterpoints=1)
    f1s2.legend([col2],['2 < z < 2.5'],scatterpoints=1)
    f1s3.legend([col3],['2.5 < z < 3'],scatterpoints=1)
    f1s4.legend([col4],['3 < z < 3.5'],scatterpoints=1)

    #pyl.subplots_adjust(left=0.18,right=0.9,top=0.9,bottom=0.15,hspace=0.0)
    #pyl.subplots_adjust(left=0.17,bottom=0.18)

    #f1s1.axvspan(3e7,1e9,facecolor='#FFFDD0',ec='None',zorder=0)
    #f1s1.axvspan(1e11,1e12,facecolor='#FFFDD0',ec='None',zorder=0)
    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(-0.05,0.25)
    f1s1.hlines(0.0,3e7,1e12)

    f1s2.set_xscale('log')
    f1s2.set_xlim(3e7,1e12)
    f1s2.set_ylim(-0.05,0.25)
    f1s2.hlines(0.0,3e7,1e12)

    f1s3.set_xscale('log')
    f1s3.set_xlim(3e7,1e12)
    f1s3.set_ylim(-0.05,0.25)
    f1s3.hlines(0.0,3e7,1e12)

    f1s4.set_xscale('log')
    f1s4.set_xlim(3e7,1e12)
    f1s4.set_ylim(-0.05,0.25)
    f1s4.hlines(0.0,3e7,1e12)

    # remove extra ticks
    #f1s1.xaxis.set_major_formatter(pyl.NullFormatter())

    # labels
    #f1xl=pyl.figtext(0.5,0.025,r"$Log_{10}(M_{\odot})$",fontsize=30,ha='center')
    #f1yl=pyl.figtext(0.025,0.5,r"$\xi[I,H]$",fontsize=30,ha='center',rotation='vertical')
    f1s1.set_xlabel(r"$M/M_{\odot}$")
    f1s1.set_ylabel(r"$\xi[I,H]$")
    #f1s1l =pyl.figtext(0.25,0.8,"$1.5 \leq z \leq 2.5$",fontsize=16,ha='center')
    #f1s2l =pyl.figtext(0.25,0.4,"$2.5 \leq z \leq 3.5$",fontsize=16,ha='center')
    #pyl.savefig('icd_vs_mass_IH.eps')

    pyl.show()

if __name__=='__main__':
    plot_icd_vs_mass()
