import pylab as pyl
from mpl_toolkits.axes_grid.inset_locator import inset_axes
import cPickle as pickle
galaxies_all = pickle.load(open('galaxies.pickle', 'rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies_all)

m_all = [galaxy.Mass for galaxy in galaxies_all]
m = [galaxy.Mass for galaxy in galaxies]
color_all = [galaxy.Imag - galaxy.Hmag for galaxy in galaxies_all]
color = [galaxy.Imag - galaxy.Hmag for galaxy in galaxies]

color_hist_all = [galaxy.Imag- galaxy.Hmag for galaxy in galaxies_all if
        galaxy.Mass > 11 and  galaxy.ston_I < 30.]
color_hist = [galaxy.Imag- galaxy.Hmag for galaxy in galaxies if galaxy.Mass >
        11]


f = pyl.figure(1, (6,4))
f1 = f.add_subplot(111)
inset = inset_axes(f1, width="35%", height="40%", loc=2)

f1.scatter(m_all, color_all, c='k', s=10)
f1.scatter(m, color, c='#a60628', edgecolor='#a60628', s=35)

inset.hist(color_hist, normed=False, histtype='step', edgecolor='#a60628', lw=2)
inset.hist(color_hist_all, normed=False, histtype='step', edgecolor='k', lw=2)

# adjust plots
inset.set_xlim(-1,4)
inset.set_xlabel('$i_{775} - H_{160}$')
inset.yaxis.tick_right()

f1.set_xlabel('Log Mass $(M_\odot)$')
f1.set_ylabel('$i_{775} - H_{160}$')

pyl.show()

