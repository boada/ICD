#!/usr/bin/env python
# File: plot_halflight_vs_icd.py
# Created on: Mon 02 Apr 2012 09:43:14 PM CDT
# Last Change: Fri 05 Oct 2012 02:51:28 PM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from colsort import colsort
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png
from astLib import astCalc

def plot_halflight_vs_icd():

    gini = pyl.loadtxt('gdss_e4_f160_m25.morph')
    icd = pyl.loadtxt('icd_1.5_3.5_gsd_full_ston.txt')

    f1 = pyl.figure('Half Light vs ICD',figsize=(8,4))
    f1s1 = f1.add_subplot(111)

    mass = []
    half = []
    icd1 = []
    id_num = []
    appendmass =mass.append
    appendhalf =half.append
    appendicd1 =icd1.append
    appendid_num =id_num.append
    for i in range(len(icd)):
        for j in range(len(gini)):
            if icd[i][0] == gini[j][0]: # match the ID's
                if icd[i][11]>30.0: # Ston in I
                    appendid_num(icd[i][0])
                    appendmass(icd[i][8])
                    #mass.append(icd[i][11])
# Add the half light and convert to Kpc
                    appendhalf(gini[j][6]*astCalc.da(icd[i][7])*1000./206265.)
                   # print icd[i][0],gini[j][0],gini[j][6]*astCalc.da(icd[i][7])*1000./206265
                    #half.append(icd[i][12])
                    appendicd1(icd[i][9])


    # Sort the arrays by mass
    mass = pyl.asarray(mass)
    half = pyl.asarray(half)
    icd1 = pyl.asarray(icd1)
    id_num = pyl.asarray(id_num)

    plt_matrix = pyl.column_stack((mass,half,icd1,id_num))
    plt_matrix = colsort(plt_matrix,1)

    sc1 = f1s1.scatter(plt_matrix[:,1], plt_matrix[:,2],
                    c='#6495ED', s=50, edgecolor='w')#, cmap='spectral')
            #        c=pyl.log10(plt_matrix[:,0]), s=50)#, cmap='spectral')
    '''
    galaxylist =[1297, 5428, 3323, 6659, 1236, 12038, 6566,
        6574, 4730, 605, 1164, 11318, 5591, 14243]
    x_coor =[4.95, 5.7, 6.7, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 6.7,
            5.7, 5., 0.5, 0.5]
    y_coor =[-0.08, -0.08, -0.08, -0.05, 0.0, 0.05, 0.10, 0.15,
            0.2, 0.23, 0.23, 0.23, 0.12, 0.07]
    for label, x, y in zip(plt_matrix[:,3], plt_matrix[:,1], plt_matrix[:,2]):
        for galaxy, x1, y1 in zip(galaxylist, x_coor, y_coor):
            if galaxy == label:
                #print galaxy,label,x,y
                image =\
                read_png('/home/steven/Projects/galaxy_icd/images/pngs_contours_halflight/'
                    +'GSD_'+str(galaxy)+'_RGB_contours.png')
                imagebox = OffsetImage(image, zoom=0.17)
                xy = [x1, y1] # Coordinates of the image
                ab = AnnotationBbox(imagebox, xy, pad=0.0)
                art=f1s1.add_artist(ab)
                pyl.annotate(' ', xy=(x,y), xytext=(x1,y1),textcoords='data',
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    for label, x, y in zip(plt_matrix[:,3], plt_matrix[:,1], plt_matrix[:,2]):
        if 1. <x and x < 2.:
            pyl.annotate(label, xy=(x,y), xytext=(x,y), textcoords='data',
                ha='right', va='bottom',bbox=dict(boxstyle='round,pad=0.5',
                fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle='->'))
    '''

    #for ID, icd, light in zip(plt_matrix[:,3],plt_matrix[:,2],plt_matrix[:,1]):
    #    print ID,icd,light
    ############
    # FIGURE 1 #
    ############
    pyl.figure('Half Light vs ICD')
    pyl.subplots_adjust(bottom=0.15,hspace=0.0)

    #bar = pyl.colorbar(sc1)
    #bar.set_label(r"$Log_{10}(M/M_{\odot})$",fontsize=18)

    f1s1.set_xlim(0,7.)
    f1s1.set_ylim(-0.05,0.25)
    f1s1.set_xlabel(r"$R_{1/2} [kpc]$")
    f1s1.set_ylabel(r"$\xi[I,H]$")
    #f1s1.tick_params(axis='both',pad=7)
    pyl.savefig('halflight_vs_icd_vs_mass_IH.eps')

    pyl.show()

if __name__=='__main__':
    plot_halflight_vs_icd()
