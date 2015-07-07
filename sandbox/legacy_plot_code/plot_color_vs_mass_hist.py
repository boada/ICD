#!/usr/bin/env python
# File: plot_color_vs_mass.py
# Created on: Mon 12 Mar 2012 12:03:42 PM CDT
# Last Change: Mon 19 Mar 2012 03:27:41 PM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mk_galaxy_struc import mk_galaxy_struc

def plot_color_vs_mass_hist():
    galaxies = mk_galaxy_struc()

    # Definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left+width+0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    # Add the figures
    # Mass vs color plot I-H
    f1 = pyl.figure(1,figsize=(8,8))
    f1s1 = f1.add_axes(rect_scatter)
    f1s2 = f1.add_axes(rect_histx)
    f1s3 = f1.add_axes(rect_histy)

    # Mass vs color plot J-H
    f2 = pyl.figure(2,figsize=(8,8))
    f2s1 = f2.add_axes(rect_scatter)
    f2s2 = f2.add_axes(rect_histx)
    f2s3 = f2.add_axes(rect_histy)
    #f2s1 = f2.add_subplot(111)

    # Mass vs color plot Z-H
    f3 = pyl.figure(3,figsize=(8,8))
    f3s1 = f3.add_axes(rect_scatter)
    f3s2 = f3.add_axes(rect_histx)
    f3s3 = f3.add_axes(rect_histy)
    #f3s1 = f3.add_subplot(111)

    mass1 = []
    color1 = []
    mass2 = []
    color2 = []
    mass3 = []
    color3 = []
    for i in range(len(galaxies)):
        # Color vs Mass Plots
        if galaxies[i].ston_I >30.0:
            if galaxies[i].Mips >=10.0:
                f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
                c='#FFAB19', marker='o', markersize=9)
                mass1.append(galaxies[i].Mass) # Get the right mass
                color1.append(galaxies[i].Imag-galaxies[i].Hmag) # Get the color
            if galaxies[i].ICD_IH > 0.1:
                f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
                c='None', marker='s', markersize=10)
            else:
                f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
                c='#196DFF', marker='*')
        elif 20.0 < galaxies[i].ston_I and galaxies[i].ston_I < 30.0 :
            f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
            c='0.8', marker='s', alpha=0.4)
        else:
            f1s1.plot(galaxies[i].Mass,galaxies[i].Imag-galaxies[i].Hmag,
            c='0.8', marker='.', alpha=0.4)

        if galaxies[i].ston_Z >30.0:
            if galaxies[i].Mips >=10.0:
                f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
                c='#FFAB19', marker='o', markersize=9)
                mass2.append(galaxies[i].Mass) # Get the right mass
                color2.append(galaxies[i].Zmag-galaxies[i].Hmag) # Get the color
            if galaxies[i].ICD_ZH > 0.05:
                f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
                c='None', marker='s', markersize=10)
            else:
                f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
                c='#196DFF', marker='*')
        elif 20.0 < galaxies[i].ston_Z and galaxies[i].ston_Z < 30.0 :
            f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
            c='0.8', marker='s', alpha=0.4)
        else:
            f2s1.plot(galaxies[i].Mass,galaxies[i].Zmag-galaxies[i].Hmag,
            c='0.8', marker='.', alpha=0.4)

        if galaxies[i].ston_J >30.0:
            if galaxies[i].Mips >=10.0:
                f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
                c='#FFAB19', marker='o', markersize=9)
                mass3.append(galaxies[i].Mass) # Get the right mass
                color3.append(galaxies[i].Jmag-galaxies[i].Hmag) # Get the color
            if galaxies[i].ICD_JH > 0.03:
                f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
                c='None', marker='s', markersize=10)
            else:
                f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
                c='#196DFF', marker='*')
        elif 20.0 < galaxies[i].ston_J and galaxies[i].ston_J < 30.0 :
            f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
            c='0.8', marker='s', alpha=0.4)
        else:
            f3s1.plot(galaxies[i].Mass,galaxies[i].Jmag-galaxies[i].Hmag,
            c='0.8', marker='.', alpha=0.4)

    ############
    # FIGURE 1 #
    ############
    pyl.figure(1)

    f1s1.set_xscale('log')
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_ylim(0,4.5)
    f1s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
    f1s1.set_ylabel("$(I-H)_{Observed}$",fontsize=20)
    f1s1.tick_params(axis='both',pad=7)

    binsx = pyl.logspace(7, 12)
    binsy = pyl.linspace(f1s1.get_ylim()[0], f1s1.get_ylim()[1] + 0.25)
    f1s2.hist(mass1, bins=binsx)
    f1s2.set_xlim( f1s1.get_xlim() )
    f1s2.tick_params(labelbottom='off')
    f1s2.set_xscale('log')

    f1s3.hist(color1, bins=binsy, orientation='horizontal')
    f1s3.set_ylim( f1s1.get_ylim() )
    f1s3.tick_params(labelleft='off')

    pyl.savefig('color_vs_mass_hist_IH.eps')

    ############
    # FIGURE 2 #
    ############
    pyl.figure(2)

    f2s1.set_xscale('log')
    f2s1.set_xlim(3e7,1e12)
    f2s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
    f2s1.set_ylabel("$(Z-H)_{Observed}$",fontsize=20)
    f2s1.tick_params(axis='both',pad=7)

    binsx = pyl.logspace(7, 12)
    binsy = pyl.linspace(f2s1.get_ylim()[0], f2s1.get_ylim()[1] + 0.25)
    f2s2.hist(mass2, bins=binsx)
    f2s2.set_xlim( f2s1.get_xlim() )
    f2s2.tick_params(labelbottom='off')
    f2s2.set_xscale('log')

    f2s3.hist(color2, bins=binsy, orientation='horizontal')
    f2s3.set_ylim( f2s1.get_ylim() )
    f2s3.tick_params(labelleft='off')
    pyl.savefig('color_vs_mass_hist_ZH.eps')

    ############
    # FIGURE 3 #
    ############
    pyl.figure(3)

    f3s1.set_xscale('log')
    f3s1.set_xlim(3e7,1e12)
    f3s1.set_ylim(-0.5,2)
    f3s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
    f3s1.set_ylabel("$(J-H)_{Observed}$",fontsize=20)
    f3s1.tick_params(axis='both',pad=7)

    binsx = pyl.logspace(7, 12)
    binsy = pyl.linspace(f3s1.get_ylim()[0], f3s1.get_ylim()[1] + 0.25)
    f3s2.hist(mass3, bins=binsx)
    f3s2.set_xlim( f3s1.get_xlim() )
    f3s2.tick_params(labelbottom='off')
    f3s2.set_xscale('log')

    f3s3.hist(color3, bins=binsy, orientation='horizontal')
    f3s3.set_ylim( f3s1.get_ylim() )
    f3s3.tick_params(labelleft='off')
    pyl.savefig('color_vs_mass_hist_JH.eps')

    pyl.show()

if __name__ ==  '__main__':
    plot_color_vs_mass_hist()
