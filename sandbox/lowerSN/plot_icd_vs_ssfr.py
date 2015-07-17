import pylab as pyl
import cPickle as pickle
from scipy.stats import scoreatpercentile

galaxies = pickle.load(open('galaxies.pickle', 'rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I > 10., galaxies)

f1 = pyl.figure(1, figsize=(6,4))
f1s1 = f1.add_subplot(111)

# for the clipped points
arrow_right = [[0,0],[-1,1],[0,0],[-2,0],[0,0],[-1,-1],[0,0]]
arrow_down = [[0.,0.], [-1., 1], [0.,0.],[0.,2.], [0.,0.], [1, 1]]

icd = pyl.asarray([galaxy.ICD_IH*100 for galaxy in galaxies])
sfr = pyl.asarray([pyl.log10(galaxy.ssfr) for galaxy in galaxies])

# plot the data
f1s1.scatter(icd, sfr, c='0.8',edgecolor='0.8', s=25, label='Data')

#plot the outliers
for i,s in zip(icd, sfr):
    if s < -10:
        pyl.scatter(i, -10, s=100, marker=None, verts = arrow_down)
    if i > 50:
        pyl.scatter(50, s, s=100, marker=None, verts = arrow_right)

bins = pyl.linspace(icd.min(),50, 10)
delta = bins[1]-bins[0]
idx  = pyl.digitize(icd,bins)
running_median = [pyl.median(sfr[idx==k]) for k in range(10)]
#upper = [scoreatpercentile(sfr[idx==k], 75) for k in range(1,7)]
#lower = [scoreatpercentile(sfr[idx==k], 25) for k in range(1,7)]

pyl.plot(bins-delta/2, running_median, '#A60628', lw=4, label='Median')
#pyl.plot(bins-delta/2, upper, '#348ABD', '--', lw=4, label='Quartile')
#pyl.plot(bins-delta/2, lower, '#348ABD', '--', lw=4)


# add the speagle relation
from astLib.astCalc import tz

t = tz(2.25)
m = 10
sfr = (0.84 - 0.026*t)*m - (6.51-0.11*t)

f1s1.axhspan(sfr-m - 0.2, sfr-m + 0.2, color='#AAF0D1', label='speagle+14',
        zorder=0)
#f1s1.axhline(sfr-m, lw=2, c='purple', label='speagle+14')
#f1s1.axhline(sfr-m - 0.2, lw=2, c='purple')
#f1s1.axhline(sfr-m + 0.2, lw=2, c='purple')


f1s1.set_xlim(-5,50)
f1s1.set_ylim(-10,-6.5)

f1s1.set_xlabel(r"$\xi[i_{775},H_{160}]$ (%)")
f1s1.set_ylabel(r'Log sSFR ($yr^{-1}$)')

pyl.legend(loc='upper right', fancybox=True, frameon=True)

pyl.tight_layout()
pyl.show()
