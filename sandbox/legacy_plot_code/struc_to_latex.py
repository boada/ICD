#!/usr/bin/env python
# File: struc_to_latex.py
# Created on: Thu Aug  8 15:38:23 2013
# Last Change: Thu Aug  8 16:22:31 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import cPickle as pickle
galaxies = pickle.load(open('galaxies_fortable.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >30., galaxies)

for galaxy in galaxies:

    print int(galaxy.ID), '&',
    #print int(galaxy.ID), '&', galaxy.RA, '&', galaxy.DEC, '&',
    print '{0:.2f} & {1:.2f} & {2:.2f} &'.format(galaxy.ston_I, galaxy.ston_J,
        galaxy.ston_V),
    print '{0:.2f} & {1:.2f} & {2:.2f} &'.format(100*galaxy.ICD_IH,
            100*galaxy.ICD_JH, 100*galaxy.ICD_VJ),
    print '{0:.2f}'.format(galaxy.Mass),
    #print '{0:.2f} & {1:.2f} & {2:.2f} &'.format(galaxy.Mass, galaxy.sersic,
    #    galaxy.Color_grad),
    #print '{0:.2f} & {1:.2f} & {2:.2f} &'.format(galaxy.z, galaxy.Uflux_rest,
    #    galaxy.Vflux_rest),
    #print '{0:.2f}'.format(galaxy.Jflux_rest), r'\\'

    print r'\\'
