import cPickle as pickle
galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)

for galaxy in galaxies:
    print int(galaxy.ID), galaxy.RA, galaxy.DEC

