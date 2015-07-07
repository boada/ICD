import pylab as pyl
import cPickle as pickle
galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)

f1 = pyl.figure(1,figsize=(5,5))
f1s1 = f1.add_subplot(111)

#Upper and Lower limit arrow verts
arrowup_verts = [[0.,0.], [-1., -1], [0.,0.],
                [0.,-2.], [0.,0.], [1,-1], [0,0]]

for galaxy in galaxies:
    if galaxy.ICD_IH > 0.5:
        f1s1.scatter(galaxy.Imag-galaxy.Hmag, 50, s=100, marker=None,
                verts=arrowup_verts)
    else:
        f1s1.scatter(galaxy.Imag-galaxy.Hmag, galaxy.ICD_IH*100, c='0.8', s=50)

f1s1.set_xlabel(r'$i_{775} - H_{160}$')
f1s1.set_ylabel(r'$\xi[i_{775}, H_{160}]$ (%)')

pyl.show()
