#!/usr/bin/env python
# File: plot_color_vs_mass.py
# Created on: Mon 12 Mar 2012 12:03:42 PM CDT
# Last Change: Thu Sep 13 12:19:33 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_color_vs_mass():
    galaxies = mk_galaxy_struc()

    # Add the figures

    # Mass vs color plot I-H
    f1 = pyl.figure('CM_IH',figsize=(8,8))
    f1s1 = f1.add_subplot(111)

    # Mass vs color plot J-H
    f2 = pyl.figure('CM_ZH',figsize=(8,8))
    f2s1 = f2.add_subplot(111)

    # Mass vs color plot Z-H
    f3 = pyl.figure('CM_JH',figsize=(8,8))
    f3s1 = f3.add_subplot(111)

    for i in range(len(galaxies)):
        if 20.0 < galaxies[i].ston_I and galaxies[i].ston_I < 30.0 :
            f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
            c='0.8', marker='s', alpha=0.4,zorder=0)
        elif galaxies[i].ston_I < 20.0:
            f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
            c='0.8', marker='.', alpha=0.4)

        if 20.0 < galaxies[i].ston_Z and galaxies[i].ston_Z < 30.0 :
            f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
            c='0.8', marker='s', alpha=0.4)
        elif galaxies[i].ston_Z < 20.0:
            f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
            c='0.8', marker='.', alpha=0.4)

        if 20.0 < galaxies[i].ston_J and galaxies[i].ston_J < 30.0 :
            f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
            c='0.8', marker='s', alpha=0.4)
        elif galaxies[i].ston_J < 20.0:
            f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
            c='0.8', marker='.', alpha=0.4)

    for i in range(len(galaxies)):
        # Color vs Mass Plots
        if galaxies[i].ston_I >30.0:
            if galaxies[i].Mips >=10.0:
                f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
                c='#FFAB19', marker='o', markersize=9)
            if galaxies[i].ICD_IH > 0.1:
                f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
                c='None', marker='s', markersize=10)
            else:
                f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
                c='#196DFF', marker='*')

        if galaxies[i].ston_Z >30.0:
            if galaxies[i].Mips >=10.0:
                f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
                c='#FFAB19', marker='o', markersize=9)
            if galaxies[i].ICD_ZH > 0.05:
                f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
                c='None', marker='s', markersize=10)
            else:
                f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
                c='#196DFF', marker='*')

        if galaxies[i].ston_J >30.0:
            if galaxies[i].Mips >=10.0:
                f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
                c='#FFAB19', marker='o', markersize=9)
            if galaxies[i].ICD_JH > 0.03:
                f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
                c='None', marker='s', markersize=10)
            else:
                f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
                c='#196DFF', marker='*')

    ############
    # FIGURE 4 #
    ############
    pyl.figure('CM_IH')

    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(0,4.5)
    f1s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
    f1s1.set_ylabel("$(I-H)_{Observed}$",fontsize=20)
    f1s1.tick_params(axis='both',pad=7)
    pyl.savefig('color_vs_mass_IH.eps')

    ############
    # FIGURE 5 #
    ############
    pyl.figure('CM_ZH')

    f2s1.set_xscale('log')
    f2s1.set_xlim(3e7,1e12)
    f2s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
    f2s1.set_ylabel("$(Z-H)_{Observed}$",fontsize=20)
    f2s1.tick_params(axis='both',pad=7)
    pyl.savefig('color_vs_mass_ZH.eps')

    ############
    # FIGURE 6 #
    ############
    pyl.figure('CM_JH')

    f3s1.set_xscale('log')
    f3s1.set_xlim(3e7,1e12)
    f3s1.set_ylim(-0.5,2)
    f3s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
    f3s1.set_ylabel("$(J-H)_{Observed}$",fontsize=20)
    f3s1.tick_params(axis='both',pad=7)
    pyl.savefig('color_vs_mass_JH.eps')

    pyl.show()

if __name__ ==  '__main__':
    plot_color_vs_mass()
