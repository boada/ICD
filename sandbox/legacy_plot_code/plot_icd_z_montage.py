#!/usr/bin/env python
# File: montage.py
# Created on: Mon Mar 18 10:08:05 2013
# Last Change: Tue Aug 13 14:06:18 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import img_scale
import pyfits as pyf
import pylab as pyl
from mpl_toolkits.axes_grid1 import axes_grid
#from mk_galaxy_struc import mk_galaxy_struc
import cPickle as pickle
import os

def mk_image(galaxy):
    base = './../../images_v5/GS_2.5as_matched/gs_all_'

    i_img = pyf.getdata(base+str(galaxy)+'_I.fits')
    j_img = pyf.getdata(base+str(galaxy)+'_J.fits')
    h_img = pyf.getdata(base+str(galaxy)+'_H.fits')

    img = pyl.zeros((h_img.shape[0], h_img.shape[1], 3), dtype=float)
    img[:,:,0] = img_scale.asinh(h_img)
    img[:,:,1] = img_scale.asinh(j_img)
    img[:,:,2] = img_scale.asinh(i_img)

    return img

# Get the Galaxy info
#galaxies = mk_galaxy_struc()
galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)
galaxies = pyl.asarray(filter(lambda galaxy: galaxy.ICD_IH < 0.5, galaxies))

# Make the low mass grid first
x = [galaxy.z for galaxy in galaxies]
y = [galaxy.ICD_IH *100 for galaxy in galaxies]
ll = 1.5
ul= 3.5
bins_x =pyl.linspace(ll, ul, 16)
bins_y = pyl.linspace(50, -5, 7)

grid = []

for i in range(bins_x.size-1):
    xmin = bins_x[i]
    xmax = bins_x[i+1]
    for j in  range(bins_y.size-1):
        ymax = bins_y[j]
        ymin = bins_y[j+1]

        cond=[cond1 and cond2 and cond3 and cond4 for cond1, cond2, cond3,
            cond4 in zip(x>=xmin, x<xmax, y>=ymin, y<ymax)]

        grid.append(galaxies.compress(cond))

# Put the grid together
F = pyl.figure(1, figsize=(6, 4))
grid1 = axes_grid.ImageGrid(F, 211, nrows_ncols=(6,15), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column')
grid2 = axes_grid.ImageGrid(F, 212, nrows_ncols=(6,15), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column')

from random import choice

base = './../../images_v5/GS_2.5as/gs_all_'
for i in range(len(grid)):
    print len(grid[i])
    if len(grid[i]) > 1:
        galaxy = choice(grid[i])
        ID = int(galaxy.ID)
        while os.path.isfile(base+str(galaxy)+'_I.fits'):
            print 'choose again', ID
            galaxy = choice(grid[i])
    elif len(grid[i]) == 1:
        galaxy = grid[i][0]
    else:
        pass

    grid1[i].axis('off')

    if len(grid[i]) != 0:
        ID = int(galaxy.ID)
        img = mk_image(ID)
        grid1[i].imshow(img, origin='lower')
        grid1[i].text(0.5, 0.5, str(galaxy.z), color='white' )
        grid1[i].text(0.5, 35, str(ID), color='white' )
        grid1[i].set_xticks([])
        grid1[i].set_yticks([])
    else:
        pass

pyl.show()
