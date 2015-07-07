#!/usr/bin/env python
# File: plot_icd_mass.py
# Created on: Tue Jun  4 11:31:32 2013
# Last Change: Mon Jul 15 16:35:14 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
import cPickle as pickle

def plot_icd_vs_mass():
    galaxies = pickle.load(open('galaxies.pickle','rb'))
    #galaxies = filter(lambda galaxy:
    #    galaxy.ston_I > 30. and galaxy.ICD_IH != None, galaxies)

    # Make figure
    f1 = pyl.figure(1, figsize=(6,4))
    f1s1 = f1.add_subplot(121)
    f1s2 = f1.add_subplot(122)

    #Upper and Lower limit arrow verts
    arrowup_verts = [[0.,0.], [-1., -1], [0.,0.],
        [0.,-2.], [0.,0.], [1,-1]]
    arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.],
        [0.,2.], [0.,0.], [1, 1]]

    for galaxy in galaxies:
        if galaxy.ston_I > 30. and galaxy.ICD_IH != None:
            # Add arrows first
            if galaxy.ICD_IH > 0.65:
                f1s1.scatter(galaxy.Mass, 0.5*100, s=100, marker=None,
                    verts=arrowup_verts)
            elif galaxy.ICD_IH < -0.05:
                f1s1.scatter(galaxy.Mass, -0.05*100, s=100, marker=None,
                    verts=arrowdown_verts)
            else:
                f1s1.scatter(galaxy.Mass, galaxy.ICD_IH * 100, c='lime',
                    marker='o', zorder=2, s=50)

        if galaxy.ston_J > 30. and galaxy.ICD_JH != None:
            # Add arrows first
            if galaxy.ICD_JH > 0.5:
                f1s2.scatter(galaxy.Mass, 0.2*100, s=100, marker=None,
                    verts=arrowup_verts)
            elif galaxy.ICD_JH < -0.05:
                f1s2.scatter(galaxy.Mass, -0.05*100, s=100, marker=None,
                    verts=arrowdown_verts)
            else:
                f1s2.scatter(galaxy.Mass, galaxy.ICD_JH * 100, c='lime',
                    marker='o', zorder=2, s=50)

    # Finish Plot
    f1s1.axvspan(7.477, 9, facecolor='#FFFDD0', ec='None', zorder=0)
    f1s1.axvspan(11, 12, facecolor='#FFFDD0', ec='None', zorder=0)
    f1s2.axvspan(7.477, 9, facecolor='#FFFDD0', ec='None', zorder=0)
    f1s2.axvspan(11, 12, facecolor='#FFFDD0', ec='None', zorder=0)

    f1s1.set_xlim(8,12)
    f1s2.set_xlim(8,12)

    f1s1.set_xticks([8,9,10,11,12])
    f1s2.set_xticks([8,9,10,11,12])

    f1s1.axhline(0.0, lw=2, c='b', zorder=0)
    f1s2.axhline(0.0, lw=2, c='b', zorder=0)

    f1s1.set_xlabel(r"Log Mass ($M_{\odot})$")
    f1s1.set_ylabel(r"$\xi[i_{775},H_{160}]$ (%)")
    f1s2.set_xlabel(r"Log Mass ($M_{\odot})$")
    f1s2.set_ylabel(r"$\xi[J_{125},H_{160}]$ (%)")

    pyl.show()

if __name__=='__main__':
        plot_icd_vs_mass()
