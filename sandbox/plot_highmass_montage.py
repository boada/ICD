import pylab as pyl
import pyfits as pyf
import cPickle as pickle
from mpl_toolkits.axes_grid1 import axes_grid
from colsort import colsort
import img_scale

F = pyl.figure(1, figsize=(4,6))
grid = axes_grid.ImageGrid(F, 121, nrows_ncols=(5,3), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='row')

grid2 = axes_grid.ImageGrid(F, 122, nrows_ncols=(5,3), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='row')

base = './../../images_v5/GS_2.5as_matched/gs_all_'

galaxies = pickle.load(open('galaxies.pickle','rb'))
galaxies = filter(lambda galaxy: galaxy.ston_I > 30, galaxies)

d = [[galaxy.ICD_IH*100, galaxy.Mass, galaxy.ID] for galaxy in galaxies if\
        galaxy.Mass > 11]
d = pyl.asarray(d)

d = colsort(d)

d1 = d[:5]
d2 = d[5:]

for i, (icd, mass, ID) in enumerate(zip(d1[:,0], d1[:,1], d1[:,2])):
    print icd, mass, ID
    H = pyf.getdata(base+str(int(ID))+'_H.fits')
    I = pyf.getdata(base+str(int(ID))+'_I.fits')

    H = img_scale.asinh(H, non_linear=0.5)
    I = img_scale.asinh(I, non_linear=0.5)

    grid[i*3].imshow(I, origin='lower', cmap='PuBu_r')
    grid[i*3+1].imshow(H, origin='lower', cmap='PuBu_r')
    grid[i*3+2].imshow(I-H, origin='lower', cmap='PuBu_r')

    grid[i*3].set_xticks([])
    grid[i*3].set_yticks([])
    grid[i*3+1].set_xticks([])
    grid[i*3+1].set_yticks([])
    grid[i*3+2].set_xticks([])
    grid[i*3+2].set_yticks([])

    grid[i*3].text(1, 0, str(int(ID)), color='white', fontsize=10)
    grid[i*3].text(1, 35, 'I', color='white', fontsize=10)
    grid[i*3+1].text(1, 35, 'H', color='white', fontsize=10)
    grid[i*3+1].text(39, 0, '{0:.2f}%'.format(icd), color='white', fontsize=10,
            ha='right')

    grid[i*3+2].text(1, 35, 'I-H', color='black', fontsize=10)


for i, (icd, mass, ID) in enumerate(zip(d2[:,0], d2[:,1], d2[:,2])):
    print icd, mass, ID
    H = pyf.getdata(base+str(int(ID))+'_H.fits')
    I = pyf.getdata(base+str(int(ID))+'_I.fits')

    H = img_scale.asinh(H, non_linear=0.5)
    I = img_scale.asinh(I, non_linear=0.5)

    grid2[i*3].imshow(I, origin='lower', cmap='PuBu_r')
    grid2[i*3+1].imshow(H, origin='lower', cmap='PuBu_r')
    grid2[i*3+2].imshow(I-H, origin='lower', cmap='PuBu_r')

    grid2[i*3].set_xticks([])
    grid2[i*3].set_yticks([])
    grid2[i*3+1].set_xticks([])
    grid2[i*3+1].set_yticks([])
    grid2[i*3+2].set_xticks([])
    grid2[i*3+2].set_yticks([])

    grid2[i*3].text(1, 0, str(int(ID)), color='white', fontsize=10)
    grid2[i*3].text(1, 35, 'I', color='white', fontsize=10)
    grid2[i*3+1].text(1, 35, 'H', color='white', fontsize=10)
    grid2[i*3+1].text(39, 0, '{0:.2f}%'.format(icd), color='white', fontsize=10,
            ha='right')

    grid2[i*3+2].text(1, 35, 'I-H', color='black', fontsize=10)

pyl.show()



