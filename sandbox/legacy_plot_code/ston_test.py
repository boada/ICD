import pyfits as pyf
import pylab as pyl

full = pyf.getdata('./data/gs_all_tf_h_130511b_multi.fits')
sample = pyf.getdata('../samples/sample_1.5_3.5_gs_all.fits')

f = pyl.figure(1)
f1 = f.add_subplot(111)

for i in range(len(sample)):
    ID = sample['ID'][i]
    H_flux = full['WFC3_F160W_FLUX'][i-1]
    H_flux_err = full['WFC3_F160W_FLUXERR'][i-1]
    H_flux_weight = full['WFC3_F160W_WEIGHT'][i-1]
    H_mag = sample['Hmag'][i]

    f1.scatter(H_mag,H_flux/H_flux_err)

pyl.show()

