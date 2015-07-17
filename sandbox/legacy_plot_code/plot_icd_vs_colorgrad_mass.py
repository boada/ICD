#!/usr/bin/env python
# File: plot_icd_vs_colorgrad.py
# Created on: Tue 08 May 2012 11:03:26 AM CDT
# Last Change: Mon Aug 12 14:25:59 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
import cPickle as pickle

galaxies = pickle.load(open('galaxies.pickle','rb'))

#f1 = pyl.figure(1,figsize=(5,3.09))
f1 = pyl.figure(1,figsize=(4,6))
f1s1 = f1.add_subplot(311)
f1s2 = f1.add_subplot(312)
f1s3 = f1.add_subplot(313)

galaxies = filter(lambda galaxy: galaxy.ston_I > 30. and galaxy.Color_grad !=
        None, galaxies)

#Low mass bin
y = [galaxy.Color_grad for galaxy in galaxies if 8 < galaxy.Mass < 10]
x = [galaxy.ICD_IH*100 for galaxy in galaxies if 8 < galaxy.Mass < 10]

f1s1.scatter(x, y, s=25, c='0.8')
f1s1.axvline(3.64, c='r', ls=':', lw=2, zorder=0)
f1s1.axhline(-0.06, c='r', ls=':', lw=2, zorder=0)

#Medium mass bin
y = [galaxy.Color_grad for galaxy in galaxies if 10 < galaxy.Mass < 11]
x = [galaxy.ICD_IH*100 for galaxy in galaxies if 10 < galaxy.Mass < 11]

f1s2.scatter(x, y, s=25, c='0.8')
f1s2.axvline(6.71, c='r', ls=':', lw=2, zorder=0)
f1s2.axhline(-0.12, c='r', ls=':', lw=2, zorder=0)

#High mass bin
y = [galaxy.Color_grad for galaxy in galaxies if 11 < galaxy.Mass < 12]
x = [galaxy.ICD_IH*100 for galaxy in galaxies if 11 < galaxy.Mass < 12]


arrow_left = [[0,0],[-1,1],[0,0],[-2,0],[0,0],[-1,-1],[0,0]]

f1s3.scatter(x, y, s=25, c='0.8')
f1s3.scatter(50, -1.5, s=100, marker=None, verts=arrow_left)
f1s3.axvline(4.35, c='r', ls=':', lw=2, zorder=0)
f1s3.axhline(-0.38, c='r', ls=':', lw=2, zorder=0)

f1s1.axvline(0, lw=2, zorder=0)
f1s2.axvline(0, lw=2, zorder=0)
f1s3.axvline(0, lw=2, zorder=0)

f1s1.axhline(0, lw=2, zorder=0)
f1s2.axhline(0, lw=2, zorder=0)
f1s3.axhline(0, lw=2, zorder=0)

# Finish Plot
f1s1.set_xlim(-5,50)
f1s2.set_xlim(-5,50)
f1s3.set_xlim(-5,50)
f1s1.set_ylim(-3.,1)
f1s2.set_ylim(-3.,1)
f1s3.set_ylim(-3.,1)

#f1s1.set_xticks([-5, 0, 5, 10, 15, 20])
f1s1.set_yticks([-3, -2, -1, 0, 1])
f1s2.set_yticks([-3, -2, -1, 0, 1])
f1s3.set_yticks([-3, -2, -1, 0, 1])


f1s1.text(-5, 0.5, 'a', color='k' )
f1s2.text(-5, 0.5, 'b', color='k' )
f1s3.text(-5, 0.5, 'c', color='k' )
f1s2.set_ylabel(r'$\Delta(i_{775} - H_{160})$')
f1s3.set_xlabel(r'$\xi[i_{775},H_{160}]$ (%)')

#pyl.subplots_adjust(left=0.165,bottom=0.165)
pyl.tight_layout()
#pyl.savefig('icd_vs_color_grad.eps',bbox='tight')

import matplotlib.font_manager
line1 = pyl.Line2D([], [], marker='o', mfc='0.8', markersize=8,
    linewidth=0)
#line2 = pyl.Line2D([], [], marker='s', mec='blue', mfc='None',
#    markersize=10, linewidth=0, markeredgewidth=2)
line3 = pyl.Line2D([], [], color='r', linewidth=2, linestyle=':')
prop = matplotlib.font_manager.FontProperties(size='small')
f1s3.legend((line1, line3), ('Data', 'Medians'), 'lower center',
    prop=prop, ncol=2)



pyl.show()
