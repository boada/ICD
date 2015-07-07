#!/usr/bin/env python
import pylab as pyl
import cPickle as pickle
from astLib import astCalc

def plot_icd_vs_mass():
    galaxies = pickle.load(open('galaxies.pickle','rb'))
#    galaxies = filter(lambda galaxy: 0.06 * galaxy.halflight *\
#           astCalc.da(galaxy.z)*1000/206265. > 2, galaxies)

    # Make figure
    f1 = pyl.figure(1, figsize=(6,4))
    f1s1 = f1.add_subplot(121)
    f1s2 = f1.add_subplot(122)
#    f1s3 = f1.add_subplot(223)
#    f1s4 = f1.add_subplot(224)

    #Upper and Lower limit arrow verts
    arrowup_verts = [[0.,0.], [-1., -1], [0.,0.],
        [0.,-2.], [0.,0.], [1,-1], [0,0]]
    #arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.],
    #    [0.,2.], [0.,0.], [1, 1]]

    for galaxy in galaxies:
        if galaxy.ston_I > 10. and galaxy.ICD_IH != None:
            # Add arrows first
            if galaxy.ICD_IH > 0.5:
                f1s1.scatter(galaxy.Mass, 0.5*100, s=100, marker=None,
                    verts=arrowup_verts)
            else:
                f1s1.scatter(galaxy.Mass, galaxy.ICD_IH * 100, c='0.8',
                    marker='o', s=25, edgecolor='0.8')
                f1s2.scatter(galaxy.Mass, galaxy.ICD_IH * 100, c='0.8',
                    marker='o', s=25, edgecolor='0.8')

    # Add the box and whiskers
    galaxies2 = filter(lambda galaxy: galaxy.ston_I > 10., galaxies)
    galaxies2 = pyl.asarray(galaxies2)
    x = [galaxy.Mass for galaxy in galaxies2]
    ll = 8.5
    ul= 12
    bins_x =pyl.array([8.5, 9., 9.5, 10., 10.5, 11., 12.])
    grid = []

    for i in range(bins_x.size-1):
        xmin = bins_x[i]
        xmax = bins_x[i+1]
        cond=[cond1 and cond2 for cond1, cond2 in zip(x>=xmin, x<xmax)]

        grid.append(galaxies2.compress(cond))
    icd = []
    for i in range(len(grid)):
        icd.append([galaxy.ICD_IH*100 for galaxy in grid[i]])

    from boxplot_percentile_width import percentile_box_plot as pbp
    #bp1 = f1s1.boxplot(icd, positions=pyl.delete(bins_x,-1)+0.25, sym='')
    width = pyl.diff(bins_x)
    index = pyl.delete(bins_x,-1) + 0.25
    index[-1] = index[-1] + 0.25
    pbp(f1s1, icd, indexer=list(index), width=width)
    pbp(f1s2, icd, indexer=list(index), width=width)

    f1s1.set_xlim(8,12)
    f1s2.set_xlim(8,12)

    f1s1.set_ylim(-10,50)
    f1s2.set_ylim(0,15)

    f1s1.set_xticks([8,9,10,11,12])
    f1s2.set_xticks([8,9,10,11,12])


    f1s1.set_ylabel(r"$\xi[i_{775},H_{160}]$ (%)")
    f1s1.set_xlabel(r"Log Mass ($M_{\odot})$")
    f1s2.set_xlabel(r"Log Mass ($M_{\odot})$")

    import matplotlib.font_manager
    line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', markersize=8,
        linewidth=0)
    line2 = pyl.Line2D([], [], marker='s', mec='#348ABD', mfc='None',
        markersize=10, linewidth=0, markeredgewidth=2)
    line3 = pyl.Line2D([], [], color='#A60628', linewidth=2)
    prop = matplotlib.font_manager.FontProperties(size='small')
    pyl.figlegend((line1, line2, line3), ('Data', 'Quartiles',
        'Medians'), 'lower center', prop=prop, ncol=3)

    from matplotlib.patches import ConnectionPatch
    xy = (12, 15)
    xy2 = (8, 15)
    con = ConnectionPatch(xyA=xy, xyB=xy2, coordsA='data', coordsB='data',
        axesA=f1s1, axesB=f1s2)
    xy = (12, 0)
    xy2 = (8, 0)
    con2 = ConnectionPatch(xyA=xy, xyB=xy2, coordsA='data', coordsB='data',
        axesA=f1s1, axesB=f1s2)
    f1s1.add_artist(con)
    f1s1.add_artist(con2)

    xy = (12, 3)
    xy2 = (8, 3)
    xy = (12, -1)
    xy2 = (8, -1)

    pyl.draw()
    pyl.show()

if __name__=='__main__':
        plot_icd_vs_mass()
