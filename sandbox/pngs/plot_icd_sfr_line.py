import pylab as pyl
import cPickle as pickle
from astLib import astCalc
from astLib import astStats

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >30., galaxies)
galaxies = filter(lambda galaxy: galaxy.ICD_IH*100 < 25., galaxies)

#Upper and Lower limit arrow verts
arrow_left = [[0,0],[-1,1],[0,0],[-2,0],[0,0],[-1,-1],[0,0]]

f1 = pyl.figure(1, figsize=(6,4))
f1s1 = f1.add_subplot(111)

for galaxy in galaxies:
    if galaxy.ICD_IH*100 < 50:
        f1s1.scatter(galaxy.ICD_IH*100, pyl.log10(galaxy.ssfr), c='0.8',
                edgecolor='0.8', s=20)
    else:
        f1s1.scatter(45, pyl.log10(galaxy.ssfr), s=100, marker=None,
                verts=arrow_left)

x = pyl.asarray([galaxy.ICD_IH*100. for galaxy in galaxies])
y = pyl.asarray([pyl.log10(galaxy.ssfr) for galaxy in galaxies])

total_bins = 20

bins = pyl.linspace(x.min(), x.max(), total_bins)
delta = bins[1]-bins[0]

idx = pyl.digitize(x, bins)

running_median = pyl.asarray([pyl.median(y[idx==k]) for k in
    range(total_bins)])
running_mad = pyl.asarray([astStats.MAD(y[idx==k]) for k in range(total_bins)])

f1s1.plot(bins-delta/2,running_median, c='r',lw=2)
f1s1.plot(bins-delta/2,running_median+running_mad, 'b--',lw=2)
f1s1.plot(bins-delta/2,running_median-running_mad, 'b--',lw=2)

f1s1.set_xlabel(r'$\xi[i_{775}, H_{160}]$ (%)')
f1s1.set_ylabel('Log sSFR')
f1s1.set_xlim(-2, 45)

import matplotlib.ticker
f1s1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

import matplotlib.font_manager
line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', markersize=8,
        linewidth=0)
line2 = pyl.Line2D([], [], color='r', linewidth=2)
line3 = pyl.Line2D([], [], ls='--', color='b', linewidth=2)

prop = matplotlib.font_manager.FontProperties(size='small')
pyl.legend((line1, line2, line3), ('Data', 'Medians', 'MAD'),
    'center right', prop=prop, ncol=1)

pyl.show()

