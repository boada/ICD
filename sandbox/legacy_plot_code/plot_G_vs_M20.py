#File: gini_plot.py
#Created: Mon 12 Mar 2012 03:00:01 PM CDT
#Last Change: Wed 03 Oct 2012 04:08:38 PM CDT
#Author: Steven Boada

import pylab as pyl
import cPickle as pickle

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.Gini is not None, galaxies)

f1 = pyl.figure(1,figsize=(4,6))
f1s1 = f1.add_subplot(211)
f1s2 = f1.add_subplot(212)

for galaxy in galaxies:
    if galaxy.ICD_IH > 0.2:
        f1s1.scatter(galaxy.M20, galaxy.Gini, s=50, c='0.8')
    else:
        f1s2.scatter(galaxy.M20, galaxy.Gini, s=50, c='0.8')

m1 = pyl.arange(-3.0,0.0,0.1)
m2 = pyl.arange(-3.0,-1.68,0.1)

f1s1.plot(m1,-0.14*m1+0.33, color='g',lw=2)
f1s1.plot(m2,0.14*m2+0.80, color='b',lw=2)
f1s2.plot(m1,-0.14*m1+0.33, color='g',lw=2)
f1s2.plot(m2,0.14*m2+0.80, color='b',lw=2)

f1s1.set_xlim(0,-3)
f1s1.set_ylim(0.3,0.8)
f1s2.set_xlim(0,-3)
f1s2.set_ylim(0.3,0.8)

f1s1.set_xticks([-3, -2, -1, 0])
f1s2.set_xticks([-3, -2, -1, 0])


#ax = pyl.gca()
#ax.set_xlim(ax.get_xlim()[::-1])
f1s2.set_xlabel(r"$M_{20}$")
f1s1.set_ylabel("G")
f1s2.set_ylabel("G")

f1s1.set_title(r'$\xi[i_{775}, H_{160}] >$ 4%')
f1s2.set_title(r'$\xi[i_{775}, H_{160}] <$ 4%')


#f1l1 = pyl.figtext(0.45,0.7,'Merger')
#f1l2 = pyl.figtext(0.7,0.5,'E/S0/Sa')
#f1l3 = pyl.figtext(0.6,0.25,'Sb-Ir')

pyl.show()
