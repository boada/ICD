#!/usr/bin/env python
import pylab as pyl
from mpl_toolkits.axes_grid1 import AxesGrid
import cPickle as pickle
from colsort import colsort

def plot_uvj_vs_icd():
    galaxies = pickle.load(open('galaxies.pickle','rb'))
    galaxies = filter(lambda galaxy: galaxy.ICD_IH != None, galaxies)
    galaxies = filter(lambda galaxy: galaxy.sersic != None and \
            galaxy.ston_I > 30, galaxies)

    #Upper and Lower limit arrow verts
    arrow_left = [[0,0],[-1,1],[0,0],[-2,0],[0,0],[-1,-1],[0,0]]

    F = pyl.figure(1,figsize=(8,3))
    grid = AxesGrid(F, 111,
            nrows_ncols=(1,4),
            axes_pad = 0.1,
            add_all=True,
            aspect=False,
            share_all = True)

    ax1 = grid[0]
    ax2 = grid[1]
    ax3 = grid[2]
    ax4 = grid[3]

    for galaxy in galaxies:
        if galaxy.sersic < 1.:
            col1 =ax1.scatter(galaxy.ICD_IH * 100., pyl.log10(galaxy.ssfr),
                s=25, c='0.8', edgecolor='0.8')
        if 1. < galaxy.sersic < 2.:
            col2 =ax2.scatter(galaxy.ICD_IH * 100., pyl.log10(galaxy.ssfr),
                    s=25, c='0.8', edgecolor='0.8')
        if 2. < galaxy.sersic < 3.:
            col3 =ax3.scatter(galaxy.ICD_IH * 100., pyl.log10(galaxy.ssfr),
                    s=25, c='0.8', edgecolor='0.8')
        if 3. <  galaxy.sersic:
            if galaxy.ICD_IH*100 < 50:
                col4 =ax4.scatter(galaxy.ICD_IH * 100., pyl.log10(galaxy.ssfr),
                    s=25, c='0.8', edgecolor='0.8')
            else:
                col4 = ax4.scatter(50, pyl.log10(galaxy.ssfr), marker=None,
                        s=100, verts=arrow_left)

    ax1.set_ylabel('Log sSFR')
    ax1.set_title('n < 1')
    ax2.set_title('1 < n < 2')
    ax3.set_title('2 < n < 3')
    ax4.set_title('3 < n')

    pyl.figtext(.5, .05, r'$\xi[i_{775},H_{160}]$ (%)',fontsize=18,
        horizontalalignment='center')

    ax1.set_xlim(-5,45)
    ax2.set_xlim(-5,45)
    ax3.set_xlim(-5,45)
    ax4.set_xlim(-5,45)
    ax1.set_ylim(-11, -6)
    ax2.set_ylim(-11, -6)
    ax3.set_ylim(-11, -6)
    ax4.set_ylim(-11, -6)


    import matplotlib.font_manager
#    line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', markersize=8,
#            linewidth=0)
#    line2 = pyl.Line2D([], [], marker='s', mec='blue', mfc='None',
#            markersize=10, linewidth=0, markeredgewidth=2)
#    line3 = pyl.Line2D([], [], color='r', linewidth=2)
#    prop = matplotlib.font_manager.FontProperties(size='small')
#    ax3.legend((line1, line2, line3), ('Data', 'Quartiles',
#        'Medians'), 'upper center', prop=prop, ncol=1)

    pyl.tight_layout()
    pyl.subplots_adjust(bottom=0.21, left=0.11)
    pyl.show()

if __name__ =='__main__':
    plot_uvj_vs_icd()
