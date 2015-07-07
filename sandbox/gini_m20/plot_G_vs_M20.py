#File: gini_plot.py
#Created: Mon 12 Mar 2012 03:00:01 PM CDT
#Last Change: Wed 03 Oct 2012 04:08:38 PM CDT
#Author: Steven Boada

import numpy as np
import pylab as pyl
import sys
sys.path.append('../')
from mk_galaxy_struc import mk_galaxy_struc

galaxies = mk_galaxy_struc()

f1 = pyl.figure(1,figsize=(8,8))
f1s1 = f1.add_subplot(221)
f1s2 = f1.add_subplot(222)
f1s3 = f1.add_subplot(223)
f1s4 = f1.add_subplot(224)

for galaxy in galaxies:
    if galaxy.ston_I >30. and galaxy.sersic != None:
        if galaxy.sersic < 1.:
            col1 = f1s1.scatter(galaxy.Gini,galaxy.M20, s=50, c='r',
                    edgecolor='w', zorder=1)
        if  1. < galaxy.sersic and galaxy.sersic < 2.:
            col2 = f1s1.scatter(galaxy.Gini,galaxy.M20, s=50, c='g',
                    edgecolor='w', zorder=1)
        if 2. < galaxy.sersic and galaxy.sersic < 3.:
            col3 = f1s1.scatter(galaxy.Gini,galaxy.M20, s=50, c='b',
                    edgecolor='w', zorder=1)
        if 3. < galaxy.sersic:
            col4 = f1s1.scatter(galaxy.Gini,galaxy.M20, s=50, c='k',
                    edgecolor='w', zorder=1)

m1 = np.arange(-3.0,0.0,0.1)
m2 = np.arange(-3.0,-1.68,0.1)

pyl.figure(1)
f1s1.plot(m1,-0.14*m1+0.33,'--',color='g',lw=2)
f1s1.plot(m2,0.14*m2+0.80,'.',color='r',lw=2)
f1s2.plot(m1,-0.14*m1+0.33,'--',color='g',lw=2)
f1s2.plot(m2,0.14*m2+0.80,'.',color='r',lw=2)
f1s3.plot(m1,-0.14*m1+0.33,'--',color='g',lw=2)
f1s3.plot(m2,0.14*m2+0.80,'.',color='r',lw=2)
f1s4.plot(m1,-0.14*m1+0.33,'--',color='g',lw=2)
f1s4.plot(m2,0.14*m2+0.80,'.',color='r',lw=2)

pyl.subplots_adjust(bottom=0.15)
f1s1.set_xlim(-3,0)
f1s1.set_ylim(0.3,0.8)
ax = pyl.gca()
ax.set_xlim(ax.get_xlim()[::-1])
f1s1.set_xlabel(r"$M_{20}$")
f1s1.set_ylabel("G")

f1l1 = pyl.figtext(0.45,0.7,'Merger')
f1l2 = pyl.figtext(0.7,0.5,'E/S0/Sa')
f1l3 = pyl.figtext(0.6,0.25,'Sb-Ir')

pyl.show()
