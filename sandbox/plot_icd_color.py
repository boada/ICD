import pylab as pyl
from astLib import astStats
import cPickle as pickle
from scipy import stats

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >30., galaxies)

f = pyl.figure(1, figsize=(6,4))
f1s1 = f.add_subplot(111)

icd = pyl.asarray([galaxy.ICD_IH*100 for galaxy in galaxies])
color = pyl.asarray([galaxy.Imag - galaxy.Hmag for galaxy in galaxies])
av = pyl.asarray([galaxy.AV for galaxy in galaxies])

d = stats.binned_statistic_2d(icd, color, av, bins=20,
        range=((0,50),(-0.5,3.5)))
extent = [d[2][0], d[2][-1], d[1][0], d[1][-1]]
im = f1s1.imshow(d[0], cmap='YlOrRd', extent=extent, interpolation='nearest',
        origin='lower')

cb = pyl.colorbar(im)
cb.set_ticks([0, 0.5, 1, 1.5, 2])
cb.set_label(r'$<A_v>$ (mag)')
pyl.xlabel(r'$i_{775} - H_{160}$ (mag)')
pyl.ylabel(r'$\xi[i_{775}, H_{160}]$ (%)')

pyl.xticks([0, 1, 2, 3])

pyl.show()



