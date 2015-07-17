import pylab as pyl
import cPickle as pickle

galaxies = pickle.load(open('./galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I > 30., galaxies)

mergers = pyl.asarray([galaxy.Merger for galaxy in galaxies])
icd = pyl.asarray([galaxy.ICD_IH*100 for galaxy in galaxies])

stack = pyl.column_stack((mergers, icd))

result =[]
for i in range(10000):
    # shuffle the icd values
    pyl.shuffle(stack[:,1])

    #get the high ICD ones
    gt = pyl.where(stack[:,1] > 20)

    # are they mergers?
    y = stack[:,0][gt]

    #how many mergers?
    m = len(y.nonzero()[0])

    #what percentage?
    per = m/float(len(gt[0]))

    # save that percentage
    result.append(per)


print len(result)
