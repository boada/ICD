#!/usr/bin/env python
# File: montage.py
# Created on: Mon Mar 18 10:08:05 2013
# Last Change: Tue Aug 20 14:17:48 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import img_scale
import pyfits as pyf
import pylab as pyl
from mpl_toolkits.axes_grid1 import axes_grid
#from mk_galaxy_struc import mk_galaxy_struc
import cPickle as pickle
import os
from random import choice

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
def mk_grid(llx, ulx, nx, lly, uly, ny):
    # Get the Galaxy info
    #galaxies = mk_galaxy_struc()
    galaxies = pickle.load(open('galaxies.pickle','rb'))
    galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)
    galaxies = pyl.asarray(filter(lambda galaxy: galaxy.ICD_IH < 0.5, galaxies))

    # Make the low mass grid first
    x = [galaxy.Mass for galaxy in galaxies]
    y = [galaxy.ICD_IH *100 for galaxy in galaxies]
    bins_x =pyl.linspace(llx, ulx, nx)
    bins_y = pyl.linspace(uly, lly, ny)

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

    return grid

def populate_grid(ax, images, picked):
    base = './../../images_v5/GS_2.5as/gs_all_'
    for i in range(len(images)):

        if len(images[i]) >= 1:
            notpicked = list(set([int(galaxy.ID) for galaxy in images[i]]) -
                    set(picked))
            if len(notpicked) > 0:
                ID = choice(notpicked)
            else:
                ID = -1
                #ax[i].axis('off')
                ax[i].spines['bottom'].set_color('0.8')
                ax[i].spines['top'].set_color('0.8')
                ax[i].spines['right'].set_color('0.8')
                ax[i].spines['left'].set_color('0.8')
                ax[i].set_axis_bgcolor('None')
        else:
            #ax[i].axis('off')
            ax[i].spines['bottom'].set_color('0.8')
            ax[i].spines['top'].set_color('0.8')
            ax[i].spines['right'].set_color('0.8')
            ax[i].spines['left'].set_color('0.8')
            ax[i].set_axis_bgcolor('None')

        if len(images[i]) != 0 and ID !=-1:
            img = mk_image(ID)
            ax[i].imshow(img, origin='lower')
            ax[i].text(0.5, 0.5, str(ID), color='white' )
            ax[i].set_xticks([])
            ax[i].set_yticks([])
            print len(picked), ID
            picked.append(ID)
        else:
            pass

    return picked

# Put the grid together
F = pyl.figure(1, figsize=(6, 4))
F2 = pyl.figure(2, figsize=(6, 4))
grid1 = axes_grid.ImageGrid(F, 111, nrows_ncols=(5,7), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column',
        label_mode='all')

grid2 = axes_grid.ImageGrid(F2, 234, nrows_ncols=(4,5), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column',
        label_mode='all')

grid3 = axes_grid.ImageGrid(F2, 235, nrows_ncols=(4,5), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column')

grid4 = axes_grid.ImageGrid(F2, 236, nrows_ncols=(4,5), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column')

grid5 = axes_grid.ImageGrid(F2, 231, nrows_ncols=(4,5), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column',
        label_mode='all')

grid6 = axes_grid.ImageGrid(F2, 232, nrows_ncols=(4,5), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column')

picked = []
grid = mk_grid(8.5, 12, 8, 0, 50, 6)
populate_grid(grid1, grid, picked)

picked=[]
grid = mk_grid(10, 11, 6, 10, 50, 5)
p1 = populate_grid(grid2, grid, picked)
p2 = populate_grid(grid3, grid, p1)
p3 = populate_grid(grid4, grid, p2)
p4 = populate_grid(grid5, grid, p3)
p5 = populate_grid(grid6, grid, p4)

# Label everything
grid1[4].set_xlabel('8.75', fontsize=16)
grid1[9].set_xlabel('9.25', fontsize=16)
grid1[14].set_xlabel('9.75', fontsize=16)
grid1[19].set_xlabel('10.25', fontsize=16)
grid1[24].set_xlabel('10.75', fontsize=16)
grid1[29].set_xlabel('11.25', fontsize=16)
grid1[34].set_xlabel('11.75', fontsize=16)

grid1[0].set_ylabel('45%', fontsize=16)
grid1[1].set_ylabel('35%', fontsize=16)
grid1[2].set_ylabel('25%', fontsize=16)
grid1[3].set_ylabel('15%', fontsize=16)
grid1[4].set_ylabel('5%', fontsize=16)

grid2[0].set_ylabel('45%', fontsize=16)
grid2[1].set_ylabel('35%', fontsize=16)
grid2[2].set_ylabel('25%', fontsize=16)
grid2[3].set_ylabel('15%', fontsize=16)

grid2[3].set_xlabel('10.1', fontsize=16)
grid2[7].set_xlabel('10.3', fontsize=16)
grid2[11].set_xlabel('10.5', fontsize=16)
grid2[15].set_xlabel('10.7', fontsize=16)
grid2[19].set_xlabel('10.9', fontsize=16)

grid3[3].set_xlabel('10.1', fontsize=16)
grid3[7].set_xlabel('10.3', fontsize=16)
grid3[11].set_xlabel('10.5', fontsize=16)
grid3[15].set_xlabel('10.7', fontsize=16)
grid3[19].set_xlabel('10.9', fontsize=16)

grid4[3].set_xlabel('10.1', fontsize=16)
grid4[7].set_xlabel('10.3', fontsize=16)
grid4[11].set_xlabel('10.5', fontsize=16)
grid4[15].set_xlabel('10.7', fontsize=16)
grid4[19].set_xlabel('10.9', fontsize=16)

grid5[0].set_ylabel('45%', fontsize=16)
grid5[1].set_ylabel('35%', fontsize=16)
grid5[2].set_ylabel('25%', fontsize=16)
grid5[3].set_ylabel('15%', fontsize=16)


pyl.show()
