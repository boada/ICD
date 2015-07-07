import pylab as pyl
import cPickle as pickle

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.sfrir != None and galaxy.ston_I >30.,
        galaxies)

f = pyl.figure(1)
f1 = f.add_subplot(311)
f2 = f.add_subplot(312)
f3 = f.add_subplot(313)

for galaxy in galaxies:
    f1.scatter(galaxy.ICD_IH*100, galaxy.sfrtotal/galaxy.sfr2800, c='0.8',
            edgecolor='0.8', s=50)

# now add the medians
x = pyl.asarray([galaxy.ICD_IH*100 for galaxy in galaxies])
y = pyl.asarray([galaxy.sfrtotal/galaxy.sfr2800 for galaxy in galaxies])
bins = pyl.linspace(0,55, 11)
idx = pyl.digitize(x, bins)
delta = bins[1]-bins[0]
running = [pyl.median(y[idx==k]) for k in range(11)]
f1.plot(bins-delta/2,running, 'r--', lw=4)

galaxies = filter(lambda galaxy: 10<galaxy.Mass< 11, galaxies)

for galaxy in galaxies:
    f2.scatter(galaxy.ICD_IH*100, galaxy.sfrtotal/galaxy.sfr2800, c='0.8',
            edgecolor='0.8', s=50)

# now add the medians
x = pyl.asarray([galaxy.ICD_IH*100 for galaxy in galaxies])
y = pyl.asarray([galaxy.sfrtotal/galaxy.sfr2800 for galaxy in galaxies])
bins = pyl.linspace(0,55, 11)
idx = pyl.digitize(x, bins)
delta = bins[1]-bins[0]
running = [pyl.median(y[idx==k]) for k in range(11)]
f2.plot(bins-delta/2,running, 'r--', lw=4)

pyl.show()


