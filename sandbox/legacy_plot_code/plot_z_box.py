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
    f1 = pyl.figure(1, figsize=(6,6))
    f1s1 = f1.add_subplot(221)
    f1s2 = f1.add_subplot(222)
    f1s3 = f1.add_subplot(223)
    f1s4 = f1.add_subplot(224)

    for galaxy in galaxies:
        if galaxy.ston_I > 30. and galaxy.ICD_IH != None:
            if galaxy.ICD_IH*100 < 50:
                f1s1.scatter(galaxy.z, galaxy.ICD_IH * 100, c='0.8',
                    marker='o', s=25, edgecolor='0.8')
            else:
                f1s1.scatter(galaxy.z, 50, s=100, marker=None, verts=arrow_up)

            f1s2.scatter(galaxy.z, galaxy.ICD_IH * 100, c='0.8',
                marker='o', s=25, edgecolor='0.8')

        if galaxy.ston_V > 30. and galaxy.ICD_VJ != None:
            f1s3.scatter(galaxy.z, galaxy.ICD_VJ * 100, c='0.8',
                marker='o', s=25, edgecolor='0.8')
            f1s4.scatter(galaxy.z, galaxy.ICD_VJ * 100, c='0.8',
                marker='o', s=25, edgecolor='0.8')

    # Add the box and whiskers
    galaxies2 = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)
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
    pbp(f1s1, icd, indexer=list(pyl.delete(bins_x,-1)+0.25))
    pbp(f1s2, icd, indexer=list(pyl.delete(bins_x,-1)+0.25))

    # Add the box and whiskers
    galaxies = pickle.load(open('galaxies.pickle','rb'))
    galaxies2 = filter(lambda galaxy: galaxy.ston_V > 30., galaxies)
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
    pbp(f1s3, icd, indexer=list(pyl.delete(bins_x,-1)+0.25))
    pbp(f1s4, icd, indexer=list(pyl.delete(bins_x,-1)+0.25))

    f1s1.set_xlim(1.5, 3.5)
    f1s2.set_xlim(1.5, 3.5)
    f1s3.set_xlim(1.5, 3.5)
    f1s4.set_xlim(1.5, 3.5)

    f1s1.set_ylim(-5, 50)
    f1s2.set_ylim(-1, 10)
    f1s3.set_ylim(-5, 50)
    f1s4.set_ylim(-1, 10)

    f1s1.set_xticks([1.5,2,2.5,3,3.5])
    f1s2.set_xticks([1.5,2,2.5,3,3.5])
    f1s1.set_xticklabels([])
    f1s2.set_xticklabels([])
    f1s3.set_xticks([1.5,2,2.5,3,3.5])
    f1s4.set_xticks([1.5,2,2.5,3,3.5])

    f1s3.set_xlabel("Redshift")
    f1s1.set_ylabel(r"$\xi[i_{775},H_{160}]$ (%)")
    f1s4.set_xlabel("Redshift")
    f1s3.set_ylabel(r"$\xi[V_{606},J_{125}]$ (%)")

    import matplotlib.font_manager
    line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', markersize=8,
        linewidth=0)
    line2 = pyl.Line2D([], [], marker='s', mec='blue', mfc='None',
        markersize=10, linewidth=0, markeredgewidth=2)
    line3 = pyl.Line2D([], [], color='r', linewidth=2)
    prop = matplotlib.font_manager.FontProperties(size='small')
    pyl.figlegend((line1, line2, line3), ('Data', 'Quartiles',
        'Medians'), 'lower center', prop=prop, ncol=3)

    from matplotlib.patches import ConnectionPatch
    xy = (3.5, 10)
    xy2 = (1.5, 10)
    con = ConnectionPatch(xyA=xy, xyB=xy2, coordsA='data', coordsB='data',
            axesA=f1s1, axesB=f1s2)
    xy = (3.5, -1)
    xy2 = (1.5, -1)
    con2 = ConnectionPatch(xyA=xy, xyB=xy2, coordsA='data', coordsB='data',
            axesA=f1s1, axesB=f1s2)
    f1s1.add_artist(con)
    f1s1.add_artist(con2)

    xy = (3.5, 10)
    xy2 = (1.5, 10)
    con = ConnectionPatch(xyA=xy, xyB=xy2, coordsA='data', coordsB='data',
            axesA=f1s3, axesB=f1s4)
    xy = (3.5, -1)
    xy2 = (1.5, -1)
    con2 = ConnectionPatch(xyA=xy, xyB=xy2, coordsA='data', coordsB='data',
            axesA=f1s3, axesB=f1s4)
    f1s3.add_artist(con)
    f1s3.add_artist(con2)

    pyl.draw()
    pyl.show()

if __name__=='__main__':
        plot_icd_vs_mass()
