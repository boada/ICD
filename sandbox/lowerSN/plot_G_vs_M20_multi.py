import pylab as pyl
import cPickle as pickle

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.Gini != None and galaxy.ston_I >
        10., galaxies)

f1 = pyl.figure(1,figsize=(5,5))
f1s1 = f1.add_subplot(221)
f1s2 = f1.add_subplot(222)
f1s3 = f1.add_subplot(223)
f1s4 = f1.add_subplot(224)

for galaxy in galaxies:
    if galaxy.ICD_IH <0.05:
        f1s1.scatter(galaxy.M20, galaxy.Gini, s=50, c='0.8')
    elif 0.04 <galaxy.ICD_IH <0.1:
        f1s2.scatter(galaxy.M20, galaxy.Gini, s=50, c='0.8')
    elif 0.1 <galaxy.ICD_IH <0.2:
        f1s3.scatter(galaxy.M20, galaxy.Gini, s=50, c='0.8')
    elif 0.2 <galaxy.ICD_IH:
        f1s4.scatter(galaxy.M20, galaxy.Gini, s=50, c='0.8')

m1 = pyl.arange(-3.0,0.0,0.1)
m2 = pyl.arange(-3.0,-1.68,0.1)

for ax in f1.get_axes():
    ax.plot(m1,-0.14*m1+0.33, '--', color='g',lw=2)
    ax.plot(m2,0.14*m2+0.80, ':', color='b',lw=2)
    ax.set_xlim(0,-3)
    ax.set_ylim(0.3,0.8)
    ax.set_xticks([-3, -2, -1, 0])
    ax.set_yticks([0.3, 0.4, 0.5, 0.6, 0.7])

f1s1.set_xticklabels([])
f1s2.set_xticklabels([])
f1s2.set_yticklabels([])
f1s4.set_yticklabels([])

#ax = pyl.gca()
#ax.set_xlim(ax.get_xlim()[::-1])
f1s3.set_xlabel(r"$M_{20}$")
f1s4.set_xlabel(r"$M_{20}$")
f1s1.set_ylabel("G")
f1s3.set_ylabel("G")


f1s4.annotate('Merger',(-1,0.65), ha='center')
f1s4.annotate('E/S0/Sa', (-2.3,0.57), ha='center')
f1s4.annotate('Sb-Ir', (-2.1, 0.35), ha='center')

f1s1.set_title(r'$\xi[i_{775}, H_{160}]<$5%')
f1s2.set_title(r'5%$<\xi[i_{775}, H_{160}]<$10%')
f1s3.set_title(r'10%$<\xi[i_{775}, H_{160}]<$20%')
f1s4.set_title(r'$\xi[i_{775}, H_{160}]>$20%')


#f1l1 = pyl.figtext(0.45,0.7,'Merger')
#f1l2 = pyl.figtext(0.7,0.5,'E/S0/Sa')
#f1l3 = pyl.figtext(0.6,0.25,'Sb-Ir')

pyl.show()
