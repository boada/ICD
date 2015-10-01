import img_scale
import pyfits as pyf
import pylab as pyl
from mpl_toolkits.axes_grid1 import axes_grid
import cPickle as pickle
import os
from scipy.stats import scoreatpercentile

def mk_image(galaxy):
    base = './../../images_v5/GS_2.5as_matched/gs_all_'

    i_img = pyf.getdata(base+str(galaxy)+'_I.fits')
    j_img = pyf.getdata(base+str(galaxy)+'_J.fits')
    h_img = pyf.getdata(base+str(galaxy)+'_H.fits')

    #include 90% of pixels
    x = pyl.hstack(i_img)
    i_lim = scoreatpercentile(x,99)
    x = pyl.hstack(j_img)
    j_lim = scoreatpercentile(x,99)
    x = pyl.hstack(h_img)
    h_lim = scoreatpercentile(x,99)

    print galaxy, i_lim, j_lim, h_lim

    img = pyl.zeros((h_img.shape[0], h_img.shape[1], 3), dtype=float)
    img[:,:,0] = img_scale.asinh(h_img, scale_min=-0.1*h_lim, scale_max=h_lim,
            non_linear=0.5)
    img[:,:,1] = img_scale.asinh(j_img, scale_min=-0.1*j_lim, scale_max=j_lim,
            non_linear=0.5)
    img[:,:,2] = img_scale.asinh(i_img, scale_min=-0.1*i_lim, scale_max=i_lim,
            non_linear=0.5)

    return img

F = pyl.figure(1, figsize=(2, 3))
grid1 = axes_grid.ImageGrid(F, 111, nrows_ncols=(3,1), axes_pad=0.05,
        add_all=True, share_all=True, aspect=True, direction='column')


ids = [9601, 4181, 1841]

base = './../../images_v5/GS_2.5as/gs_all_'
for i, ID in enumerate(ids):
    if not os.path.isfile(base+str(ID)+'_I.fits'):
        print('choose again', ID)
    else:
        grid1[i].spines['bottom'].set_color('0.8')
        grid1[i].spines['top'].set_color('0.8')
        grid1[i].spines['right'].set_color('0.8')
        grid1[i].spines['left'].set_color('0.8')
        grid1[i].set_axis_bgcolor('None')

        img = mk_image(ID)
        grid1[i].text(0.5, 0.5, str(ID), color='white' )
        grid1[i].set_xticks([])
        grid1[i].set_yticks([])
        grid1[i].imshow(img, origin='lower')

# Label everything
#grid1[4].set_xlabel('8.75', fontsize=16)
#grid1[9].set_xlabel('9.25', fontsize=16)
#grid1[14].set_xlabel('9.75', fontsize=16)
#grid1[19].set_xlabel('10.25\nLog Mass $(M_\odot)$', fontsize=16)
#grid1[24].set_xlabel('10.75', fontsize=16)
#grid1[29].set_xlabel('11.25', fontsize=16)
#grid1[34].set_xlabel('11.75', fontsize=16)

#grid1[0].set_ylabel('45%', fontsize=16)
#grid1[1].set_ylabel('35%', fontsize=16)
#grid1[2].set_ylabel(r'$\xi[i_{775}, H_{160}]$ (%)'+'\n25%', fontsize=16,
#        multialignment='center')
#grid1[3].set_ylabel('15%', fontsize=16)
#grid1[4].set_ylabel('5%', fontsize=16)

pyl.show()
