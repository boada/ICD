#!/usr/bin/env python
# File: plot_icd_vs_colorgrad.py
# Created on: Tue 08 May 2012 11:03:26 AM CDT
# Last Change: Wed Jul 17 16:06:22 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
#from mk_galaxy_struc import mk_galaxy_struc
import cPickle as pickle

#galaxies = mk_galaxy_struc()
galaxies = pickle.load(open('galaxies.pickle','rb'))

f1 = pyl.figure(1,figsize=(5,3.09))
f1s1 = f1.add_subplot(111)

#Upper and Lower limit arrow verts
arrowup_verts = [[0.,0.], [-1., -1], [0.,0.], [0.,-2.],[0.,0.], [1,-1]]
arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.], [0.,2.],[0.,0.], [1, 1]]

for galaxy in galaxies:
    if galaxy.ston_I >= 30. and galaxy.Color_grad != None:
        pyl.scatter(galaxy.ICD_IH*100., galaxy.Color_grad, s=50, c='lime')
        #if galaxy.ICD_IH < 0.05:
        #    f1s1.scatter(-0.05*100., galaxy.Color_grad,s=100,marker=None,
        #        verts=arrowdown_verts)
        #if galaxy.ICD_IH > 0.25:
        #    f1s1.scatter(0.25*100., galaxy.Color_grad,s=100,marker=None,
        #        verts=arrowup_verts)


f1s1.axvline(4, lw=2, zorder=0)
f1s1.axvline(0, ls=':', lw=2, zorder=0)
f1s1.axhline(0, lw=2, zorder=0)

pyl.text(68, 0.8, "Blue Core, Red Edge", size=12, ha="right", va="top",
        bbox = dict(boxstyle="round", ec=(1., 0.5, 0.5),
        fc=(1., 0.8, 0.8)), zorder=0)

pyl.text(65, -2.5, "Red Core, Blue Edge", size=12, ha="right", va="top",
        bbox = dict(boxstyle="round", ec=(1., 0.5, 0.5),
        fc=(1., 0.8, 0.8)))

# Finish Plot
#f1s1.set_xlim(-5,25)
f1s1.set_ylim(-3.,1)

#f1s1.set_xticks([-5, 0, 5, 10, 15, 20])
f1s1.set_yticks([-3, -2, -1, 0, 1])

f1s1.set_xlabel(r'$\xi[i_{775},H_{160}]$ (%)')
f1s1.set_ylabel('Color Gradient')

#pyl.subplots_adjust(left=0.165,bottom=0.165)
pyl.tight_layout()
pyl.savefig('icd_vs_color_grad.eps',bbox='tight')

pyl.show()
