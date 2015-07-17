import pylab as pyl
import cPickle as pickle

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >30. and galaxy.Color_grad !=
        None, galaxies)

f1 = pyl.figure(1, figsize=(6,4))
f1s1 = f1.add_subplot(111)

icd = pyl.asarray([galaxy.ICD_IH*100 for galaxy in galaxies])
colorgrad = pyl.asarray([galaxy.Color_grad for galaxy in galaxies])

f1s1.scatter(icd, colorgrad, c='0.8', edgecolor='0.8', s=25, label='Data')

f1s1.axhline(0.0, c='k', lw=1)

bins = pyl.linspace(icd.min(),icd.max(), 10)
delta = bins[1]-bins[0]
idx  = pyl.digitize(icd,bins)
running_median = [pyl.median(colorgrad[idx==k]) for k in range(10)]
pyl.plot(bins-delta/2, running_median, c='#A60628', lw=4, label='Median')

f1s1.set_xlim(-5,50)
f1s1.set_ylim(-2, 1.5)

f1s1.set_xlabel(r"$\xi[i_{775},H_{160}]$ (%)")
f1s1.set_ylabel(r'$\Delta(i_{775} - H_{160})$')

pyl.legend(loc='upper right')

pyl.tight_layout()
pyl.show()

