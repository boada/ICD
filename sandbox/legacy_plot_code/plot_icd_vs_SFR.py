#!/usr/bin/env python
# File: plot_icd_vs_SFR.py
# Created on: Thu 14 Jun 2012 11:59:06 AM CDT
# Last Change: Thu 14 Jun 2012 12:53:27 PM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pyfits as pyf
import pylab as pyl

hdulist =\
pyf.open('/home/steven/Projects/image_fields/CANDELS/GOODS_S/catalogs/results_gsd_fit_zsol_chab_cb07.fits')
tbdata=hdulist[1].data

icd = pyl.loadtxt('gini_m20/icd_1.5_3.5_gsd_full_ston.txt')

f1 = pyl.figure(1,figsize=(6,4))
f1s1 = f1.add_subplot(111)

icd1 = []
sfr = []
appendicd1 = icd1.append
appendsfr = sfr.append

for i in range(len(icd)):
    if icd[i][11] > 30.0:
        for j in range(len(tbdata.field('ID'))):
            if icd[i][0] == tbdata.field('ID')[j]:
                print icd[i][0], tbdata.field('ID')[j]
                appendicd1(icd[i][9])
                appendsfr(tbdata.field('SFR')[j])

icd1 = pyl.asarray(icd1)
sfr = pyl.asarray(sfr)

plt_matrix=pyl.column_stack((sfr,icd1))

f1s1.scatter(pyl.log10(plt_matrix[:,0]),plt_matrix[:,1],s=50)

pyl.show()
