#!/usr/bin/env python
# File: plot_grad_vs_mass.py
# Created on: Thu 14 Jun 2012 11:12:28 AM CDT
# Last Change: Mon 01 Oct 2012 09:59:51 AM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import pylab as pyl
from mpl_toolkits.mplot3d import Axes3D
from plotfix import plotfix

def plot_grad_vs_mass():
    grad = pyl.loadtxt('asymm_color_grads/colourGradients_U-V.txt')
    icd = pyl.loadtxt('gini_m20/icd_1.5_3.5_gsd_full_ston.txt')

    f1 = pyl.figure('Grad vs Mass',figsize=(6,4))
    f1s1 = f1.add_subplot(111)
    f2 = pyl.figure(2)
    f2s1 = f2.add_subplot(111)#,projection='3d')
    f2s1 = plotfix(f2s1)

    mass = []
    gradient = []
    icd1 = []
    id_num = []
    appendid_num = id_num.append
    appendmass = mass.append
    appendgradient = gradient.append
    appendicd1 = icd1.append
    for i in range(len(icd)):
        for j in range(len(grad)):
            if icd[i][0] == grad[j][0]:
                if icd[i][11] > 30.0:
                    appendmass(icd[i][8])
                    appendgradient(grad[j][2])
                    appendicd1(icd[i][9])
                    appendid_num(icd[i][0])

    mass = pyl.asarray(mass)
    gradient = pyl.asarray(gradient)
    icd1 = pyl.asarray(icd1)
    id_num = pyl.asarray(id_num)
    plt_matrix = pyl.column_stack((mass,gradient,icd1,id_num))

    pyl.figure(1)
    f1s1.scatter(plt_matrix[:,0],plt_matrix[:,1],s=50)
    f1s1.set_xscale('log')
    f1s1.hlines(0.0,3e7,1e12)
    f1s1.axvspan(3e7,1e9,facecolor='#FFFDD0',ec='None',zorder=0)
    f1s1.axvspan(1e11,1e12,facecolor='#FFFDD0',ec='None',zorder=0)
    f1s1.set_xlim(3e7,1e12)
    f1s1.set_xlabel(r"$M/M_{\odot}$",fontsize=18)

    pyl.subplots_adjust(left=0.17,bottom=0.18)

    pyl.figure(2)

    for label,x,y in zip(plt_matrix[:,3],plt_matrix[:,1], plt_matrix[:,2]):
        pyl.annotate(label,xy=(x,y),
                xytext=(x,y),textcoords='data',ha='right',va='bottom',
                bbox=dict(boxstyle='round,pad=0.5',fc='yellow',alpha=0.5),
                arrowprops=dict(arrowstyle='->'))

    f2s1.scatter(plt_matrix[:,1],plt_matrix[:,2],s=50)
    #f2s1.set_xscale('log')
    f2s1.set_ylim(-0.05,0.25)
    
    #f2s1.set_xlabel(r"$M/M_{\odot}$",fontsize=18)
    f2s1.set_xlabel("Color Gradient",fontsize=18)
    f2s1.set_ylabel(r"$\xi[I,H]$",fontsize=18)


    pyl.show()

if __name__=='__main__':
    plot_grad_vs_mass()
