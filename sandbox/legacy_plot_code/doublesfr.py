import pylab as pyl
import cPickle as pickle
from scipy.stats import scoreatpercentile


galaxies = pickle.load(open('galaxies.pickle', 'rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >30., galaxies)


f1 = pyl.figure(1)
f1s1 = f1.add_subplot(111)

x = [round(galaxy.sersic) for galaxy in galaxies]
y1 = [pyl.log10(galaxy.ssfr) for galaxy in galaxies]
y2 = [galaxy.ICD_IH*100 for galaxy in galaxies]

x_, y1_median = zip(*sorted((xVal, pyl.median([yVal for a, yVal in zip(x, y1)
    if xVal==a])) for xVal in set(x)))
x_, y2_median = zip(*sorted((xVal, pyl.median([yVal for a, yVal in zip(x, y2)
    if xVal==a])) for xVal in set(x)))

# upper and lower quartiles
x_, y1_upper = zip(*sorted((xVal, scoreatpercentile([yVal for a, yVal in zip(x,
    y1) if xVal==a], 75)) for xVal in set(x)))
x_, y1_lower = zip(*sorted((xVal, scoreatpercentile([yVal for a, yVal in zip(x,
    y1) if xVal==a], 25)) for xVal in set(x)))
x_, y2_upper = zip(*sorted((xVal, scoreatpercentile([yVal for a, yVal in zip(x,
    y2) if xVal==a], 75)) for xVal in set(x)))
x_, y2_lower = zip(*sorted((xVal, scoreatpercentile([yVal for a, yVal in zip(x,
    y2) if xVal==a], 25)) for xVal in set(x)))


f1s1.plot(x_, y1_median, lw=2, c='green', label='sSFR 50%')
f1s1.plot(x_, y1_upper, '--', lw=2, c='green', label='sSFR 75%')
f1s1.plot(x_, y1_lower, '--', lw=2, c='green', label='sSFR 25%')

pyl.legend(loc='upper center')

ax2 = f1s1.twinx()

ax2.plot(x_, y2_median, lw=2, c='orange', label='ICD 50%')
ax2.plot(x_, y2_upper, '--', lw=2, c='orange', label='ICD 75%')
ax2.plot(x_, y2_lower, '--', lw=2, c='orange', label='ICD 25%')
pyl.show()

