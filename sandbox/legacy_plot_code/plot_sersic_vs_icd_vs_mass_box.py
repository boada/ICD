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
    arrowup_verts = [[0.,0.], [-1., -1], [0.,0.],
        [0.,-2.], [0.,0.], [1,-1]]
    #arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.],
    #    [0.,2.], [0.,0.], [1, 1]]

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
            col1 =ax1.scatter(galaxy.Mass, galaxy.ICD_IH * 100.,
                s=25, c='0.8', edgecolor='0.8')
        if 1. < galaxy.sersic < 2.:
                col2 =ax2.scatter(galaxy.Mass, galaxy.ICD_IH * 100.,
                    s=25, c='0.8', edgecolor='0.8')
        if 2. < galaxy.sersic < 3.:
                col3 =ax3.scatter(galaxy.Mass, galaxy.ICD_IH * 100.,
                    s=25, c='0.8', edgecolor='0.8')
        if 3. <  galaxy.sersic:
            if galaxy.ICD_IH*100 < 50:
                col4 =ax4.scatter(galaxy.Mass, galaxy.ICD_IH * 100.,
                    s=25, c='0.8', edgecolor='0.8')
            else:
                col4 = ax4.scatter(galaxy.Mass, 50, marker=None, s=100,
                        verts=arrowup_verts)

    # Add the box and whiskers
    galaxies1 = filter(lambda galaxy: galaxy.ston_I > 30. and \
        galaxy.sersic < 1, galaxies)
    galaxies1 = pyl.asarray(galaxies1)
    galaxies2 = filter(lambda galaxy: galaxy.ston_I > 30. and \
        1 < galaxy.sersic < 2, galaxies)
    galaxies2 = pyl.asarray(galaxies2)
    galaxies3 = filter(lambda galaxy: galaxy.ston_I > 30. and \
        2 < galaxy.sersic < 3, galaxies)
    galaxies3 = pyl.asarray(galaxies3)
    galaxies4 = filter(lambda galaxy: galaxy.ston_I > 30. and \
        3 < galaxy.sersic, galaxies)
    galaxies4 = pyl.asarray(galaxies4)

    x1 = [galaxy.Mass for galaxy in galaxies1]
    x2 = [galaxy.Mass for galaxy in galaxies2]
    x3 = [galaxy.Mass for galaxy in galaxies3]
    x4 = [galaxy.Mass for galaxy in galaxies4]

    ll = 8.5
    ul= 12
    bins_x =pyl.arange(8.5, 12.5, 0.5)
    grid1 = []
    grid2 = []
    grid3 = []
    grid4 = []

    for i in range(bins_x.size-1):
        xmin = bins_x[i]
        xmax = bins_x[i+1]
        cond=[cond1 and cond2 for cond1, cond2 in zip(x1>=xmin, x1<xmax)]
        grid1.append(galaxies1.compress(cond))
        cond=[cond1 and cond2 for cond1, cond2 in zip(x2>=xmin, x2<xmax)]
        grid2.append(galaxies2.compress(cond))
        cond=[cond1 and cond2 for cond1, cond2 in zip(x3>=xmin, x3<xmax)]
        grid3.append(galaxies3.compress(cond))
        cond=[cond1 and cond2 for cond1, cond2 in zip(x4>=xmin, x4<xmax)]
        grid4.append(galaxies4.compress(cond))

    icd1 = []
    icd2 = []
    icd3 = []
    icd4 = []

    for i in range(len(grid1)):
        icd1.append([galaxy.ICD_IH*100 for galaxy in grid1[i]])
        icd2.append([galaxy.ICD_IH*100 for galaxy in grid2[i]])
        icd3.append([galaxy.ICD_IH*100 for galaxy in grid3[i]])
        icd4.append([galaxy.ICD_IH*100 for galaxy in grid4[i]])

    from boxplot_percentile import percentile_box_plot as pbp

    bp1 = pbp(ax1, icd1, indexer=list(pyl.delete(bins_x,-1)+0.25))
    bp2 = pbp(ax2, icd2, indexer=list(pyl.delete(bins_x,-1)+0.25))
    bp3 = pbp(ax3, icd3, indexer=list(pyl.delete(bins_x,-1)+0.25))
    bp4 = pbp(ax4, icd4, indexer=list(pyl.delete(bins_x,-1)+0.25))

    ax1.set_xticks([8, 9, 10, 11])
    ax2.set_xticks([8, 9, 10, 11])
    ax3.set_xticks([8, 9, 10, 11])
    ax4.set_xticks([8, 9, 10, 11])

    ax1.set_ylim(0, 50)
    ax2.set_ylim(0, 50)
    ax3.set_ylim(0, 50)
    ax4.set_ylim(0, 50)

    ax1.set_ylabel(r'$\xi[i_{775},H_{160}]$ (%)')
    ax1.set_title('n < 1')
    ax2.set_title('1 < n < 2')
    ax3.set_title('2 < n < 3')
    ax4.set_title('3 < n')

    pyl.figtext(.5, .05, r'Log Mass $(M_{\odot})$',fontsize=18,
        horizontalalignment='center')
    ax1.axhline(0, lw=2, zorder=0)
    ax2.axhline(0, lw=2, zorder=0)
    ax3.axhline(0, lw=2, zorder=0)
    ax4.axhline(0, lw=2, zorder=0)

    import matplotlib.font_manager
    line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', markersize=8,
            linewidth=0)
    line2 = pyl.Line2D([], [], marker='s', mec='blue', mfc='None',
            markersize=10, linewidth=0, markeredgewidth=2)
    line3 = pyl.Line2D([], [], color='r', linewidth=2)
    prop = matplotlib.font_manager.FontProperties(size='small')
    ax3.legend((line1, line2, line3), ('Data', 'Quartiles',
        'Medians'), 'upper center', prop=prop, ncol=1)

    pyl.tight_layout()
    pyl.subplots_adjust(bottom=0.21, left=0.11)
    pyl.show()

if __name__ =='__main__':
    plot_uvj_vs_icd()
