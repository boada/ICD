import img_scale
import pyfits as pyf
import pylab as pyl
from mpl_toolkits.axes_grid1 import axes_grid
from scipy.stats import scoreatpercentile

F = pyl.figure(1, figsize=(6,4))
grid = axes_grid.ImageGrid(F, 111, nrows_ncols=(3,4), axes_pad=0.05,
        add_all=True, share_all=True, direction='column', label_mode='all')

galaxies =[397, 1073, 1589, 3736, 8030,
        8740, 10832, 14447, 15769, 16934, 21852, 18801]
    #949, 1961, 3608, 4956, 10426]

def mk_image(galaxy):
    base = './../../images_v5/GS_2.5as_matched/gs_all_'

    i_img = pyf.getdata(base+str(galaxy)+'_I.fits')
    j_img = pyf.getdata(base+str(galaxy)+'_J.fits')
    h_img = pyf.getdata(base+str(galaxy)+'_H.fits')

    x = pyl.hstack(i_img)
    i_lim = scoreatpercentile(x,99)
    x = pyl.hstack(j_img)
    j_lim = scoreatpercentile(x,99)
    x = pyl.hstack(h_img)
    h_lim = scoreatpercentile(x,99)

    img = pyl.zeros((h_img.shape[0], h_img.shape[1], 3), dtype=float)
    img[:,:,0] = img_scale.asinh(h_img, scale_max=h_lim, non_linear=0.5)
    img[:,:,1] = img_scale.asinh(j_img, scale_max=j_lim, non_linear=0.5)
    img[:,:,2] = img_scale.asinh(i_img, scale_max=i_lim, non_linear=0.5)

    img = pyl.zeros((h_img.shape[0], h_img.shape[1], 3), dtype=float)
    img[:,:,0] = img_scale.asinh(h_img, scale_min=-0.1*h_lim, scale_max=h_lim,
                                non_linear=0.5)
    img[:,:,1] = img_scale.asinh(j_img, scale_min=-0.1*j_lim, scale_max=j_lim,
                                non_linear=0.5)
    img[:,:,2] = img_scale.asinh(i_img, scale_min=-0.1*i_lim, scale_max=i_lim,
                                non_linear=0.5)

    return img

label =0
for ax, galaxy in zip(grid, galaxies):
    img = mk_image(galaxy)
    ax.imshow(img, origin='lower')
    ax.set_xticks([])
    ax.set_yticks([])
    #ax.text(0.5, 35, str(chr(ord('a')+label)), color='white' )
    ax.text(0.5, 1, str(int(galaxy)), color='white' )
    label += 1

#grid[-1].axis('off')

pyl.tight_layout()

pyl.show()
