#!/usr/bin/env python
# File: script.py
# Created on: Fri Jun 21 10:42:19 2013
# Last Change: Fri Jun 21 11:08:42 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada
import math as m
import pyfits as pyf
data = pyf.open('icd_oldold_old_new.fits')
data = data[1].data


for ID1, ID2, ICD1, ICD2, ston1, ston2 in zip(
    data['ID_1'], data['ID_2a'], data['ICD_IH_1'],
        data['ICD_IH'], data['ston_I_1'], data['ston_I']):

    if ston1 >30 and ston2 > 30:
        if abs(ICD1-ICD2)*100 > 5:
            print ID1, ID2, (ICD1-ICD2)*100

