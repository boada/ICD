#!/usr/bin/env python
# File: plot_color_vs_mass.py
# Created on: Mon 12 Mar 2012 12:03:42 PM CDT
# Last Change: Mon Jun 24 13:57:07 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
#from mk_galaxy_struc import mk_galaxy_struc
import cPickle as pickle

def plot_color_vs_mass_hist():
    #galaxies = mk_galaxy_struc()
    galaxies = pickle.load(open('galaxies.pickle','rb'))
    galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)


    # Definitions for the axes
    left, width = 0.12, 0.83
    bottom, height = 0.12, 0.5
    bottom_h = left+height+0.05

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.25]

    # Add the figures
    # Mass vs color plot I-H
    f1 = pyl.figure(1,figsize=(6,5))
    f1s1 = f1.add_axes(rect_scatter)
    f1s2 = f1.add_axes(rect_histx)
    #f1s3 = f1.add_axes(rect_histy)

    # Plot redshift data
    for galaxy in galaxies:
        f1s1.scatter(galaxy.z, galaxy.ICD_IH *100., c='r', s=50)

    # make histogram data
    all_rs = [galaxy.z for galaxy in galaxies if galaxy.ICD_IH < 1]
    highicd_rs = [galaxy.z for galaxy in galaxies
            if 0.04 < galaxy.ICD_IH < 1]
    # Now make the bins
    bin1_high = float(len([z for z in highicd_rs if 1.5 < z < 2.0 ]))
    bin1_all = float(len([z for z in all_rs if 1.5 < z < 2.0 ]))

    bin2_high = float(len([z for z in highicd_rs if 2.0 < z < 2.5 ]))
    bin2_all = float(len([z for z in all_rs if 2.0 < z < 2.5 ]))

    bin3_high = float(len([z for z in highicd_rs if 2.5 < z < 3.0 ]))
    bin3_all = float(len([z for z in all_rs if 2.5 < z < 3.0 ]))

    bin4_high = float(len([z for z in highicd_rs if 3.0 < z < 3.5 ]))
    bin4_all = float(len([z for z in all_rs if 3.0 < z < 3.5 ]))

    f1s2.bar(1.5, bin1_high/bin1_all*100., width=0.5, ec='k', fc='r')
    f1s2.bar(2.0, bin2_high/bin2_all*100., width=0.5, ec='k', fc='r')
    f1s2.bar(2.5, bin3_high/bin3_all*100., width=0.5, ec='k', fc='r')
    f1s2.bar(3.0, bin4_high/bin4_all*100., width=0.5, ec='k', fc='r')

    print bin1_high/bin1_all*100.
    print bin2_high/bin2_all*100.
    print bin3_high/bin3_all*100.
    print bin4_high/bin4_all*100.

    #Add the VJ data
    all_rs = [galaxy.z for galaxy in galaxies if galaxy.ICD_VJ < 1]
    highicd_rs = [galaxy.z for galaxy in galaxies
            if 0.04 < galaxy.ICD_VJ < 1]
    # Now make the bins
    bin1_high = float(len([z for z in highicd_rs if 1.5 < z < 2.0 ]))
    bin1_all = float(len([z for z in all_rs if 1.5 < z < 2.0 ]))

    bin2_high = float(len([z for z in highicd_rs if 2.0 < z < 2.5 ]))
    bin2_all = float(len([z for z in all_rs if 2.0 < z < 2.5 ]))

    bin3_high = float(len([z for z in highicd_rs if 2.5 < z < 3.0 ]))
    bin3_all = float(len([z for z in all_rs if 2.5 < z < 3.0 ]))

    bin4_high = float(len([z for z in highicd_rs if 3.0 < z < 3.5 ]))
    bin4_all = float(len([z for z in all_rs if 3.0 < z < 3.5 ]))

    f1s2.bar(1.5, bin1_high/bin1_all*100., width=0.5, ec='k', fc='none',
        linestyle='dashed', lw=2)
    f1s2.bar(2.0, bin2_high/bin2_all*100., width=0.5, ec='k', fc='none',
        linestyle='dashed', lw=2)
    f1s2.bar(2.5, bin3_high/bin3_all*100., width=0.5, ec='k', fc='none',
        linestyle='dashed', lw=2)
    f1s2.bar(3.0, bin4_high/bin4_all*100., width=0.5, ec='k', fc='none',
        linestyle='dashed', lw=2, label=r'$\xi[V_{606}, J_{125}]$')

    ############
    # FIGURE 1 #
    ############

    f1s1.set_xlim(1.5,3.5)
    f1s1.set_ylim(-1,25)
    f1s1.set_xlabel("Redshift")
    f1s1.set_ylabel(r"$\xi[i_{775}, H_{160}]$ (%)")

    #f1s1.text(1.1,13,'NEW DATA',rotation='vertical',
    #    verticalalignment='center', fontsize=20, color='k', zorder=1,
    #    backgroundcolor='w')
    #f1s1.axvspan(0.7, 1.5, facecolor='w', ec='k', hatch='/',zorder=0)


    #f1s2.text(1.1,17.5,'NEW DATA',rotation='vertical',
    #    verticalalignment='center', fontsize=20, color='k', zorder=1,
    #    backgroundcolor='w')
    #f1s2.axvspan(0.7, 1.5, facecolor='w', ec='k', hatch='/',zorder=0)
    f1s2.set_xlim( f1s1.get_xlim() )
    f1s2.tick_params(labelbottom='off')
    f1s2.set_yticks([10, 20, 30, 40, 50])
    f1s2.set_ylabel(r"$N_{bin} > 4\% (\%)$")
    f1s2.legend()

    pyl.show()

if __name__ ==  '__main__':
    plot_color_vs_mass_hist()
