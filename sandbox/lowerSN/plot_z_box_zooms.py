#!/usr/bin/env python
# File: plot_icd_mass.py
# Created on: Tue Jun  4 11:31:32 2013
# Last Change: Mon Aug 12 14:09:04 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
import cPickle as pickle

def plot_icd_vs_mass():
    galaxies = pickle.load(open('galaxies.pickle','rb'))

    arrow_up = [[0,0], [-1,-1], [0,0], [0,-2], [0,0], [1,-1], [0,0]]

    # Make figure
    f1 = pyl.figure(1, figsize=(4,6))
    f1s1 = f1.add_subplot(211)
    f1s2 = f1.add_subplot(212)

    for galaxy in galaxies:
        if galaxy.ston_I > 10. and galaxy.ICD_IH != None:
            f1s1.scatter(galaxy.z, galaxy.ICD_IH * 100, c='0.8',
                marker='o', s=25, edgecolor='0.8')

        if galaxy.ston_V > 10. and galaxy.ICD_VJ != None:
            f1s2.scatter(galaxy.z, galaxy.ICD_VJ * 100, c='0.8',
                marker='o', s=25, edgecolor='0.8')

    # Add the box and whiskers
    galaxies2 = filter(lambda galaxy: galaxy.ston_I > 10., galaxies)
    galaxies2 = pyl.asarray(galaxies2)
    x = [galaxy.z for galaxy in galaxies2]
    ll = 1.5
    ul= 4
    bins_x =pyl.arange(ll, ul, 0.5)
    grid = []

    for i in range(bins_x.size-1):
        xmin = bins_x[i]
        xmax = bins_x[i+1]
        cond=[cond1 and cond2 for cond1, cond2 in zip(x>=xmin, x<xmax)]

        grid.append(galaxies2.compress(cond))
    icd = []
    for i in range(len(grid)):
        icd.append([galaxy.ICD_IH*100 for galaxy in grid[i]])
    from boxplot_percentile import percentile_box_plot as pbp
    pbp(f1s1, icd, indexer=list(pyl.delete(bins_x,-1)+0.25), whisker_top=None,
            whisker_bottom=None)

    # Add the box and whiskers
    galaxies = pickle.load(open('galaxies.pickle','rb'))
    galaxies2 = filter(lambda galaxy: galaxy.ston_V > 10., galaxies)
    galaxies2 = pyl.asarray(galaxies2)
    x = [galaxy.z for galaxy in galaxies2]
    ll = 1.5
    ul= 4
    bins_x =pyl.arange(ll, ul, 0.5)
    grid = []

    for i in range(bins_x.size-1):
        xmin = bins_x[i]
        xmax = bins_x[i+1]
        cond=[cond1 and cond2 for cond1, cond2 in zip(x>=xmin, x<xmax)]

        grid.append(galaxies2.compress(cond))
    icd = []
    for i in range(len(grid)):
        icd.append([galaxy.ICD_VJ*100 for galaxy in grid[i]])
    pbp(f1s2, icd, indexer=list(pyl.delete(bins_x,-1)+0.25), whisker_top=None,
            whisker_bottom=None)

    f1s1.set_xlim(1.5, 3.5)
    f1s2.set_xlim(1.5, 3.5)

    f1s1.set_ylim(-1, 15)
    f1s2.set_ylim(-1, 15)

    f1s1.set_xticklabels([])
    f1s2.set_xticks([1.5,2,2.5,3,3.5])

    f1s1.set_yticks([2,4,6,8,10,12,14])
    f1s2.set_yticks([2,4,6,8,10,12,14])

    f1s1.set_ylabel(r"$\xi[i_{775},H_{160}]$ (%)")
    f1s2.set_xlabel("Redshift")
    f1s2.set_ylabel(r"$\xi[V_{606},J_{125}]$ (%)")

    import matplotlib.font_manager
    line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', markersize=8,
        linewidth=0)
    line2 = pyl.Line2D([], [], marker='s', mec='#348ABD', mfc='None',
        markersize=10, linewidth=0, markeredgewidth=2)
    line3 = pyl.Line2D([], [], color='#A60628', linewidth=2)
    prop = matplotlib.font_manager.FontProperties(size='small')
    pyl.figlegend((line1, line2, line3), ('Data', 'Quartiles',
        'Medians'), 'lower center', prop=prop, ncol=3)

    pyl.show()

if __name__=='__main__':
        plot_icd_vs_mass()
