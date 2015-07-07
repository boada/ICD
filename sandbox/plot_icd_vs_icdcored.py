import pylab as pyl
import cPickle as pickle

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >30., galaxies)

f1 = pyl.figure(1, figsize=(6,4))
f1s1 = f1.add_subplot(111)

icd = pyl.asarray([galaxy.ICD_IH*100 for galaxy in galaxies])
icdc = pyl.asarray([galaxy.ICD_IH_cored*100 for galaxy in galaxies])
y = (icd-icdc)/icd

f1s1.scatter(icd, y, c='0.8', edgecolor='0.8', s=25, label='Data')

f1s1.axhline(0.0, c='k', lw=1)

bins = pyl.linspace(icd.min(),icd.max(), 10)
delta = bins[1]-bins[0]
idx  = pyl.digitize(icd,bins)
running_median = [pyl.median(y[idx==k]) for k in range(10)]
pyl.plot(bins-delta/2, running_median, c='#A60628', lw=4, label='Median')

f1s1.set_xlim(-5,50)
f1s1.set_ylim(-1, 1)

f1s1.set_xlabel(r"$\xi[i_{775},H_{160}]$ (%)")
#f1s1.set_ylabel(r'$(\xi[i_{775},H_{160}]_{out} -\xi[i_{775},H_{160}])\xi[i_{775},H_{160}]$')

f1s1.set_ylabel('Fractional Change')

pyl.legend(loc='upper right')

pyl.tight_layout()
pyl.show()

