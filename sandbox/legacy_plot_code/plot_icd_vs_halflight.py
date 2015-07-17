import pylab as pyl
import cPickle as pickle
from astLib import astCalc
from scipy.stats import scoreatpercentile
import matplotlib.ticker


galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >30., galaxies)

f1 = pyl.figure(1, figsize=(6,4))
f1s1 = f1.add_subplot(111)

#x = [0.06 * galaxy.halflight * astCalc.da(galaxy.z) * 1000./206265
#    for galaxy in galaxies]

galaxies = pyl.asarray(galaxies)

for galaxy in galaxies:
    re = 0.06* galaxy.halflight * astCalc.da(galaxy.z)*1000/206265.
    f1s1.scatter(re, galaxy.ICD_IH*100, c='0.8', edgecolor='0.8', s=20)

bins_x = pyl.arange(1, 20, 2)
grid = []

for i in range(bins_x.size-1):
    xmin = bins_x[i]
    xmax = bins_x[i+1]
    cond=[cond1 and cond2 for cond1, cond2 in zip(x>=xmin, x<xmax)]
    bunch = galaxies.compress(cond)

    icds = [galaxy.ICD_IH*100 for galaxy in bunch]
    if len(icds) >= 1:
        med = pyl.median(icds)
        f1s1.scatter((xmax-xmin)/2. + xmin, med, s=50, c='r')
    print xmin, (xmax-xmin)/2., xmax, med

f1s1.set_xlabel(r'$R_e$ (kpc)')
f1s1.set_ylabel(r'$\xi[i_{775}, H_{160}]$ (%)')
f1s1.set_ylim(0.1, 50)
f1s1.set_xlim(1,20)

f1s1.set_xscale('log')
f1s1.set_xticks([1,2,5,10,15])
f1s1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
pyl.show()

