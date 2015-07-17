import pylab as pyl
import cPickle as pickle
from astLib import astCalc
from astLib import astStats
from scipy.stats import scoreatpercentile
galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >30., galaxies)
#galaxies = filter(lambda galaxy: 10<galaxy.Mass <11 , galaxies)

#Upper and Lower limit arrow verts
arrowup_verts = [[0., 0.], [-1., -1], [0., 0.],
    [0., -2.], [0., 0.], [1, -1]]
#arrowdown_verts = [[0.,0.], [-1., 1], [0.,0.],
#    [0.,2.], [0.,0.], [1, 1]]

f1 = pyl.figure(1, figsize=(6, 4))
f1s1 = f1.add_subplot(111)

for galaxy in galaxies:
    re = 0.06* galaxy.halflight * astCalc.da(galaxy.z)*1000/206265.
    if galaxy.ICD_IH*100 < 50:
        f1s1.scatter(re, galaxy.ICD_IH*100, c='0.8', edgecolor='0.8', s=20)
    else:
        f1s1.scatter(re, 50, s=100, marker=None, verts=arrowup_verts)

x = [round(0.06 * galaxy.halflight * astCalc.da(galaxy.z)*1000/206265.) for
        galaxy in galaxies]
y = [galaxy.ICD_IH*100. for galaxy in galaxies]

x_, y_median = zip(*sorted((xVal, pyl.median([yVal for a, yVal in zip(x, y) if
    xVal==a])) for xVal in set(x)))

x_, y_upper = zip(*sorted((xVal, scoreatpercentile([yVal for a, yVal in zip(x,
    y) if xVal==a], 75)) for xVal in set(x)))
x_, y_low = zip(*sorted((xVal, scoreatpercentile([yVal for a, yVal in zip(x,
    y) if xVal==a], 25)) for xVal in set(x)))


y_median = pyl.asarray(y_median)[:-3]
y_upper = pyl.asarray(y_upper)[:-3]
y_low = pyl.asarray(y_low)[:-3]
x_ = x_[:-3]

#print x_, y_median, y_mad

f1s1.plot(x_, y_median, lw=2, c='#A60628')
f1s1.plot(x_, y_median + y_upper, '--', lw=2, c='#348ABD')
f1s1.plot(x_, y_median - y_low, '--', lw=2, c='#348ABD')

f1s1.set_xlabel(r'$R_e$ (kpc)')
f1s1.set_ylabel(r'$\xi[i_{775}, H_{160}]$ (%)')
f1s1.set_ylim(0.1, 50)
f1s1.set_xlim(1, 20)

f1s1.set_xscale('log')
f1s1.set_xticks([1, 2, 5, 10, 15])
import matplotlib.ticker
f1s1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

import matplotlib.font_manager
line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', markersize=8,
        linewidth=0)
line2 = pyl.Line2D([], [], color='#A60628', linewidth=2)
line3 = pyl.Line2D([], [], ls='--', color='#348ABD', linewidth=2)

#prop = matplotlib.font_manager.FontProperties()
#pyl.figlegend((line1, line2, line3), ('Data', 'Medians', 'MAD'),
#    'lower center', prop=prop, ncol=3)
pyl.legend((line1, line2, line3), ('Data', 'Medians', 'Quartile'),
    'upper right', ncol=1)
pyl.tight_layout()
pyl.show()

