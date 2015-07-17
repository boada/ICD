import pylab as pyl
import cPickle as pickle
from mpl_toolkits.axes_grid1 import AxesGrid
from colsort import colsort

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ICD_IH is not None, galaxies)

f1 = pyl.figure(1, figsize=(5,5))
f1s1 = f1.add_subplot(111)

low_mass = []
low_color = []
low_icd = []
high_mass = []
high_color = []
high_icd = []

for galaxy in galaxies:
    if galaxy.ston_I >30:
        high_mass.append(galaxy.Mass)
        high_color.append(galaxy.Imag - galaxy.Hmag)
        if galaxy.ICD_IH*100 > 33.5:
            high_icd.append(33.5)
        else:
            high_icd.append(galaxy.ICD_IH*100)
    else:
        low_mass.append(galaxy.Mass)
        low_color.append(galaxy.Imag - galaxy.Hmag)
        low_icd.append(galaxy.ICD_IH*100)

low_mass = pyl.asarray(low_mass)
low_color = pyl.asarray(low_color)
low_icd = pyl.asarray(low_icd)
high_mass = pyl.asarray(high_mass)
high_color = pyl.asarray(high_color)
high_icd = pyl.asarray(high_icd)

low = pyl.column_stack((low_mass, low_color, low_icd))
high = pyl.column_stack((high_mass, high_color, high_icd))

#sort
high_sort = colsort(high, 3)

#plot
sc2 = f1s1.scatter(low[:,0], low[:,1], c='0.8', edgecolor='0.8', s=25)
#sc1 = f1s1.scatter(high_sort[:,0], high_sort[:,1], c=high_sort[:,2], s=50,
#        cmap='spectral')
sc1 = f1s1.scatter(high_sort[:,0], high_sort[:,1], c='#9370DB', s=50)

#bar = pyl.colorbar(sc1)
#bar.set_label(r'$\xi[i_{775}, H_{160}]$ (%)')

f1s1.set_xlabel(r'Log Mass $(M_\odot)$')
f1s1.set_ylabel(r'$(i_{775} - H_{160})_{Observed}$')
f1s1.set_xticks([8,9,10,11,12])

import matplotlib.font_manager
prop = matplotlib.font_manager.FontProperties(size='small')
line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', linewidth=0)
line2 = pyl.Line2D([], [], marker='o', mfc='#9370DB', linewidth=0)
f1s1.legend((line1, line2), ('$i_{775}$ S/N < 30', '$i_{775}$ S/N > 30'),
    'upper left', prop=prop, ncol=1)

pyl.show()


