import os
import numpy as np
import pyfits as pyf
try:
    import cPickle as pickle
except ImportError:
    import pickle

class galaxy:
    __module__ = os.path.splitext(os.path.basename(__file__))[0]
    def __init__(self,
        ID=None,
        RA=None,
        DEC=None,
        Imag=None,
        Zmag=None,
        Jmag=None,
        Hmag=None,
        z=None,
        Mass=None,
        mass_candels=None,
        ICD_IH=None,
        ICD_IH_ERR=None,
        ICD_IH_cored=None,
        ston_I=None,
        ICD_JH=None,
        ICD_JH_ERR=None,
        ston_J=None,
        PR_H=None,
        ICD_VJ=None,
        ICD_VJ_ERR=None,
        ston_V=None,
        mips24 = None,
        Mips=None,
        AV=None,
        sfr2800 = None,
        sfrir = None,
        sfrtotal = None,
        lsfr = None,
        lssfr = None,
        Gini=None,
        M20=None,
        Spiral=False,
        Elliptical=False,
        Merger=False,
        sersic=None,
        axis_ratio=None,
        Color_grad=None,
        Uflux_rest = None,
        Vflux_rest = None,
        Jflux_rest = None,
        clumps = None,
        halflight=None,
        stellarity=None):

        self.ID = ID
        self.RA = RA
        self.DEC = DEC
        self.Imag = Imag
        self.Zmag = Zmag
        self.Jmag = Jmag
        self.Hmag = Hmag
        self.z = z
        self.Mass = Mass
        self.mass_candels = mass_candels
        self.ICD_IH = ICD_IH
        self.ICD_IH_ERR = ICD_IH_ERR
        self.ICD_IH_cored = ICD_IH_cored
        self.ston_I = ston_I
        self.ICD_JH = ICD_JH
        self.ICD_JH_ERR = ICD_JH_ERR
        self.ston_J = ston_J
        self.PR_H = PR_H
        self.ICD_VJ = ICD_VJ
        self.ICD_VJ_ERR = ICD_VJ_ERR
        self.ston_V = ston_V
        self.mips24 = mips24
        self.Mips = Mips
        self.AV = AV
        self.sfr2800 = sfr2800
        self.sfrir = sfrir
        self.sfrtotal = sfrtotal
        self.lsfr = lsfr
        self.lssfr = lssfr
        self.Gini = Gini
        self.M20 = M20
        self.Spiral = Spiral
        self.Elliptical = Elliptical
        self.Merger = Merger
        self.sersic = sersic
        self.axis_ratio = axis_ratio
        self.Color_grad = Color_grad
        self.Uflux_rest = Uflux_rest
        self.Vflux_rest = Vflux_rest
        self.Jflux_rest = Jflux_rest
        self.clumps = clumps
        self.halflight = halflight
        self.stellarity = stellarity

def mk_galaxy_struc():
    from mk_galaxy_struc import galaxy
    galaxies = []

    # Add Sample
    data = pyf.getdata('../samples/sample_1.5_3.5_gs_all.fits')
    for i in range(len(data)):
        galaxies.append(galaxy(data['ID'][i],
            data['RA'][i],
            data['DEC'][i],
            data['Imag'][i],
            data['Zmag'][i],
            data['Jmag'][i],
            data['Hmag'][i],
            data['z'][i])
            )

    # Add ICD info
    data = pyf.getdata('../results/icd_IH.fits')
    #data = pyf.getdata('../results/IH_icd_20140806.fits')
    for i in range(len(data)):
        look = data['ID'][i]
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.ICD_IH = data['ICD_IH'][i]
                galaxy.ICD_IH_ERR = data['ICD_IH_ERR'][i]
                galaxy.ston_I = data['ston_I'][i]

    data = pyf.getdata('../results/icd_JH.fits')
    #data = pyf.getdata('../results/JH_icd_20140806.fits')
    for i in range(len(data)):
        look = data['ID'][i]
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.ICD_JH = data['ICD_JH'][i]
                galaxy.ICD_JH_ERR = data['ICD_JH_ERR'][i]
                galaxy.ston_J = data['ston_J'][i]

    data = pyf.getdata('../results/icd_VJ.fits')
    #data = pyf.getdata('../results/VJ_icd_20140806.fits')
    for i in range(len(data)):
        look = data['ID'][i]
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.ICD_VJ = data['ICD_VJ'][i]
                galaxy.ICD_VJ_ERR = data['ICD_VJ_ERR'][i]
                galaxy.ston_V = data['ston_V'][i]


    # Add FAST results
    data = pyf.getdata('./data/FAST_result_GS_1.5_3.5.fits')
    for i in range(len(data)):
        look = data['id'][i] # note the difference
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.Mass = data['lmass'][i]
                galaxy.AV = data['Av'][i]
                galaxy.lsfr = data['lsfr'][i]
                galaxy.lssfr = data['lssfr'][i]

    # Add EAZY results
    u = np.loadtxt('./data/photz.153.rf')
    v = np.loadtxt('./data/photz.155.rf')
    j = np.loadtxt('./data/photz.161.rf')
    for ID, u1,v1,j1 in zip(u[:,0],u[:,5],v[:,5],j[:,5]):
        look = int(ID)
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.Uflux_rest = u1
                galaxy.Vflux_rest = v1
                galaxy.Jflux_rest = j1

    # Add GalFit data
    data = pyf.getdata('./data/gs_all_candels_ers_udf_f160w_v0.5_galfit.fits')
    for i in range(len(data)):
        look = data['id'][i]
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.sersic = data['n'][i]
                galaxy.axis_ratio = data['q'][i]
                galaxy.halflight = data['re'][i]

    # Add Color Gradient for GSD
    hdulist =\
    pyf.open('./data/GOODS-S_May2013_colourGradients_diff_all_no-pegs_2013-06-20.fits')
    tbdata = hdulist[1].data
    for i in range(len(tbdata.field('ID'))):
        look = tbdata.field('ID')[i]
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.Color_grad = tbdata.field('grad_i-H_obs')[i]
                #galaxy.Color_grad = tbdata.field('grad_z-H_obs')[i]

    # MIPS
    hdulist =\
    pyf.open('./data/Sample_MIPS_matched.fits')
    tbdata = hdulist[1].data
    for i in range(len(tbdata.field('ID_GSD'))):
        look = tbdata.field('ID_GSD')[i]
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.Mips = tbdata.field('F24')[i]

    # Add the morphology data.
    data1 = np.genfromtxt('./gini_m20/gdss-match.txt', names=True)
    for i in range(len(data1)):
        look = data1[i]['ID_1'] # ID
        for galaxy in galaxies:
                if look == galaxy.ID:
                    G = galaxy.Gini = data1[i]['G']
                    M = galaxy.M20 = data1[i]['M20']
                    if G <= (-0.14*M+0.33) and G > (0.14*M+0.80): # E/S0/Sa
                        galaxy.Elliptical = True
                    elif G <= (-0.14*M+0.33) and G <= (0.14*M+0.80): #Sb-Ir
                        galaxy.Spiral = True
                    elif G > (-0.14*M+0.33): # Mergers
                        galaxy.Merger = True

    # Add extra stuff
    data = pyf.getdata('./data/gs_all_tf_h_130511b_multi.fits')
    for galaxy in galaxies:
        galaxy.stellarity = data['CLASS_STAR'][galaxy.ID-1]
        galaxy.halflight = data['FLUX_RADIUS_2'][galaxy.ID-1]

    data = np.genfromtxt('./data/centers_removed.dat', names=True)
    for i in range(len(data)):
        look = data['ID'][i]
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.ICD_IH_cored = data['ICD'][i]

    data = np.genfromtxt('./data/clumpylist_4steven.dat')
    for i in range(len(data)):
        look = data[i][0]
        for galaxy in galaxies:
            if look == galaxy.ID:
                # Number of blobs with UV Luminosity L_blob/L_galaxy>0.08
                #galaxy.clumps = data[i][5]
                # Number of blobs with UV Luminosity L_blob/L_galaxy>0.05
                #galaxy.clumps = data[i][4]
                # Number of blobs with UV Luminosity L_blob/L_galaxy>0.01
                galaxy.clumps = data[i][3]

    data = np.genfromtxt('./data/sfrs.txt', names=True)
    for i in data:
        look = i['UserID']
        for galaxy in galaxies:
            if look == galaxy.ID:
                if i['SFR_Wuyts'] < 0.0:
                    a2800 = 1.79289 * i['FAST_ma05_Av']
                    #a2800 = 1.79289 * galaxy.AV
                    correction = 10.0**(a2800/2.5)
                    galaxy.sfr2800 = i['SFR_2800']
                    galaxy.sfrtotal = i['SFR_2800'] * correction
                else:
                    a2800 = 1.79289 * i['FAST_ma05_Av']
                    #a2800 = 1.79289 * galaxy.AV
                    correction = 10.0**(a2800/2.5)
                    galaxy.sfr2800 = i['SFR_2800']
                    galaxy.sfrir = (i['SFR_Wuyts']+i['SFR_2800'])/10**0.2178
                    galaxy.sfrtotal = (i['SFR_Wuyts']+i['SFR_2800'])/10**0.2178

                #galaxy.Mass = i['FAST_ma05_lmass']
                galaxy.ssfr = galaxy.sfrtotal/10**galaxy.Mass
                galaxy.mips24 = i['mips24_cryo']

    data = np.genfromtxt('./data/masses_from_CANDELS.txt', names=True)
    for i in data:
        look = i['UserID']
        for galaxy in galaxies:
            if look == galaxy.ID:
                galaxy.mass_candels = i['FAST_ma05_lmass']

    x = [galaxy.ID for galaxy in galaxies if galaxy.stellarity > 0.78]

    # Bad galaxy removal
    bad = [1073.0, 3736.0, 8030.0, 10832.0, 15769.0, 949.0, 1961.0, 3608.0,
        4956.0, 10426.0, 18801.0]+x
    galaxies = filter(lambda galaxy: galaxy.ID not in bad, galaxies)

    pickle.dump(galaxies, open('galaxies.pickle', 'wb'))


    '''
    # Add AGN info
    hdulist =\
    pyf.open('gsd_agn_matched.fits')
    tbdata = hdulist[1].data
    for i in range(len(tbdata.field('ID'))):
        look = tbdata.field('ID')[i]
        for galaxy in galaxies:
            if galaxy.field == 1:
                if look == galaxy.ID and tbdata.field('AGNflag')[i]==100:
                    galaxy.AGN = True
                    galaxy.AGN_z = tbdata.field('zbest')[i]

    '''

    #return galaxies
if __name__=='__main__':
    mk_galaxy_struc()
