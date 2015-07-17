#!/usr/bin/env python
# File: plot_icd_visual.py
# Created on: Wed Dec  5 10:01:35 2012
# Last Change: Wed Dec  5 13:16:45 2012
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
import matplotlib.image as mpimg

fig, ax = pyl.subplots(1, 4, figsize=(6,3))

img =\
mpimg.imread('/Users/steven/Projects/galaxy_icd/images/GSD_IJH_20kpc/GSD_5107_RGB.png')
ax[0].imshow(img)
ax[0].set_title(r'$\xi[I,H] = 0$')

img =\
mpimg.imread('/Users/steven/Projects/galaxy_icd/images/GSD_IJH_20kpc/GSD_6179_RGB.png')
ax[1].imshow(img)
ax[1].set_title(r'$\xi[I,H] = 6$')

img =\
mpimg.imread('/Users/steven/Projects/galaxy_icd/images/GSD_IJH_20kpc/GSD_6574_RGB.png')
ax[2].imshow(img)
ax[2].set_title(r'$\xi[I,H] = 12$')

img =\
mpimg.imread('/Users/steven/Projects/galaxy_icd/images/GSD_IJH_20kpc/GSD_11318_RGB.png')
ax[3].imshow(img)
ax[3].set_title(r'$\xi[I,H] = 17$')

for i in range(4):
    ax[i].get_xaxis().set_visible(False)
    ax[i].get_yaxis().set_visible(False)



pyl.show()
