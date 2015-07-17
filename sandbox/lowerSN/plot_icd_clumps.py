import pylab as pyl
import cPickle as pickle
from astLib import astStats

galaxies = pickle.load(open('galaxies.pickle', 'rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I >10. and galaxy.clumps != None,
        galaxies)

f = pyl.figure(1, figsize=(6,4))
f1s1 = f.add_subplot(111)

d = [[galaxy.clumps, galaxy.ICD_IH*100] for galaxy in galaxies]
d = pyl.asarray(d)

f1s1.scatter(d[:,0], d[:,1], s=50, c='0.8', edgecolor='0.8')

bins = pyl.arange(0, 50, 5)
index = pyl.digitize(d[:,1], bins) - 1
delta = bins[1] - bins[2]
avgs = [pyl.mean(d[:,0][index==k]) for k in range(len(bins))]
#avgs = [astStats.biweightLocation(d[:,0][index==k], 6.0) for k in range(len(bins))]

#avgs = astStats.runningStatistic(d[:,1], d[:,0])
#bins = pyl.linspace(d[:,1].min(), d[:,1].max(), 10)
#delta = bins[1] - bins[0]

#f1s1.hlines(bins - delta/2., [0], avgs, lw=2, color='#A60628')
f1s1.plot(avgs, bins - delta/2.,  lw=2, color='#A60628')

avg=[]
for i in range(9):
    d = [galaxy.ICD_IH*100 for galaxy in galaxies if galaxy.clumps ==i]
    avg.append(astStats.biweightLocation(d, 6.0))

    #f1s1.vlines(i, [0],pyl.mean(d), linestyle='dashed', lw=2, color='blue')
    #f1s1.vlines(i, [0],astStats.biweightLocation(d,6.0), linestyle='dashed',
    #        lw=2, color='#348ABD')
f1s1.plot(range(9), avg, linestyle='dashed',
    lw=2, color='#348ABD')


f1s1.set_xlim(-0.5, 10)
f1s1.set_ylim(0, 50)
f1s1.set_xlabel('Clump Number')
f1s1.set_ylabel(r'$\xi(i_{775}, H_{160})$ (%)')

line1 = pyl.Line2D([], [], marker='o', mfc='0.8', mec='0.8', lw=0)
line2 =  pyl.Line2D([], [], color='#A60628', lw=2)
line3 = pyl.Line2D([], [], color='#348ABD',linestyle='dashed', lw=2)

pyl.legend((line1, line2, line3), ('Data', 'Mean Clump', 'Mean ICD'),
        loc='upper right', ncol=1)

pyl.show()

