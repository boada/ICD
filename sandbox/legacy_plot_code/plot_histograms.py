#!/usr/bin/env python
# File: plot_histograms.py
# Created on: Mon 25 Jun 2012 12:58:05 PM CDT
# Last Change: Tue Jun 25 15:07:50 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
import numpy as np
#from mk_galaxy_struc import mk_galaxy_struc
import cPickle as pickle

def plot_histograms():
    #galaxies = mk_galaxy_struc()
    galaxies = pickle.load(open('galaxies.pickle','rb'))

    f1 = pyl.figure(1,figsize=(6,4))
    f1s1 = f1.add_subplot(111)

    # Histogram Data
    z =[]
    appendz = z.append
    z2 =[]
    appendz2 = z2.append

    for galaxy in galaxies:
        if galaxy.z < 3.5:
            appendz(galaxy.z)
        if galaxy.ston_I >30.:
            appendz2(galaxy.z)

    # Make Histogram plots
    h, binedg = np.histogram(z,10)
    wid = binedg[1:] - binedg[:-1]
    f1s1.bar(binedg[:-1], (h/float(len(z)))*100, width=wid, fill=False, ec='b',
        hatch='/', label='all', lw=2)

    h, binedg = np.histogram(z2,10)
    wid = binedg[1:] - binedg[:-1]
    f1s1.bar(binedg[:-1], (h/float(len(z2)))*100, width=wid, fill=False,
        ec='r', hatch='\ ', label='selected', lw=2 )

    #pyl.subplots_adjust(left=0.19,bottom=0.19)

    f1s1.set_xlabel("Redshift")
    f1s1.set_ylabel("Fraction of Total (%)")
    f1s1.set_yticks([5, 10, 15, 20, 25])
    f1s1.set_ylim(0,26)
    pyl.legend()
    pyl.tight_layout()
    #pyl.savefig('redshift_histogram.eps',bbox='tight')
    pyl.show()

if __name__ == '__main__':
    plot_histograms()

