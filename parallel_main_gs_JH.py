#!/usr/bin/python

import sys
from ctypes import *
from functions import *
from math import sqrt
import numpy as np
import multiprocessing
import pyfits
import signal

# Load the library for the CFitsio routines
overseer = CDLL("/home/steven/Projects/galaxy_icd/libraries/liboverseer.so.0")

def main(sample):
    naxes = (c_long*2)(500,500)
    base='/home/steven/Projects/image_fields/CANDELS/GOODS_S_complete_psfmatched/'

    f = pyfits.open(
            base+"fields/gs_all_candels_ers_udf_f125w_060mas_v0.5_rms.fits")
    rms1_data=f[0].data

    f = pyfits.open(
            base+"fields/gs_all_candels_ers_udf_f160w_060mas_v0.5_rms.fits")
    rms2_data=f[0].data

    f = pyfits.open(
        base+"fields/gs_all_candels_ers_udf_wfc3_f125w_v0.5_drz_psfmatch2h_p01.fits")
    image1_data=f[0].data

    f = pyfits.open(
            base+"fields/gs_all_candels_ers_udf_f160w_060mas_v0.5_drz.fits")
    image2_data=f[0].data

    f = pyfits.open(
            base+"fields/gs_all_sx_h_120604_hphotom_comb_seg_psfmatch2h.fits")
    segmap_data=f[0].data

    del f
    cat_data = np.loadtxt(
            base+"catalogs/gs_all_sx_h_120604_hphotom_comb_merge_psfmatch2h.cat")

    active = np.loadtxt(sample)

    # Get the number of processors available
    num_processes = multiprocessing.cpu_count()
    threads = []
    print "+++ Number of galaxies to process: %s" % (len(active[:,0]))

    # run until all the threads are done, and there is no data left
    done = False
    a = 0
    while not done:
        if( len(threads) < num_processes-1):
            galaxy_num = int(active[a][0])

            x_coor = int(cat_data[galaxy_num-1][1])
            y_coor = int(cat_data[galaxy_num-1][2])

            # Load the images into 1D arrays
            rms1 = rms1_data[y_coor-naxes[0]/2:y_coor+naxes[0]/2,
                    x_coor-naxes[1]/2:x_coor+naxes[1]/2]
            rms2 = rms2_data[y_coor-naxes[0]/2:y_coor+naxes[0]/2,
                    x_coor-naxes[1]/2:x_coor+naxes[1]/2]
            image1 = image1_data[y_coor-naxes[0]/2:y_coor+naxes[0]/2,
                    x_coor-naxes[1]/2:x_coor+naxes[1]/2]
            image2 = image2_data[y_coor-naxes[0]/2:y_coor+naxes[0]/2,
                    x_coor-naxes[1]/2:x_coor+naxes[1]/2]
            segmap = segmap_data[y_coor-naxes[0]/2:y_coor+naxes[0]/2,
                    x_coor-naxes[1]/2:x_coor+naxes[1]/2]

            f1 = open("galaxy"+str(galaxy_num).zfill(5)+"_gs_JH.txt","wt")
            p = multiprocessing.Process(target=work,
                    args=[naxes,rms1,rms2,image1,image2,segmap,x_coor,y_coor,galaxy_num,f1])
            p.start()
            print p, p.is_alive()
            threads.append(p)
            a+=1
        else:
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
        #if a == 10:
        if a == len(active[:,0]):
            done = True

def work(naxes,rms1,rms2,image1,image2,segmap,x_coor,y_coor,galaxy_num,f1):

    # Declare arrays for the images to be put into
    rms1_c = (c_float*(naxes[0]*naxes[1]))(-1.0)
    rms2_c = (c_float*(naxes[0]*naxes[1]))(-1.0)
    image1_c = (c_float*(naxes[0]*naxes[1]))(-1.0)
    image2_c = (c_float*(naxes[0]*naxes[1]))(-1.0)
    segmap_c = (c_float*(naxes[0]*naxes[1]))(-1.0)

    rms1 = convert(rms1,rms1_c,naxes,'J')
    rms2 = convert(rms2,rms2_c,naxes,'H')
    image1 = convert(image1,image1_c,naxes,'J')
    image2 = convert(image2,image2_c,naxes,'H')
    segmap = convert(segmap,segmap_c,naxes)

    del rms1_c,rms2_c,image1_c,image2_c,segmap_c

    x_coor = naxes[0]/2
    y_coor = naxes[1]/2

    signal.alarm(30)

    pr = overseer.calc_pr(image2,segmap,c_float(galaxy_num),x_coor,y_coor,naxes)
    if not pr:
        f1.close()
        print "ERROR!!"
        return 0

    pr_map = make_pr_map(image2,segmap,galaxy_num,int(x_coor),int(y_coor),pr,naxes)
    #alpha,beta = calc_scale_factors(galaxy_num,pr_map,image1,image2,rms2)
    alpha,beta = calc_scale_factors3(pr_map, image1, image2, rms2)

    flux = background = 0.0
    g1w = g2w = 10E8
    for i in range(len(pr_map)):
        try:
            if (g1w >= calc_weight(rms1[pr_map[i]])):
                g1w = calc_weight(rms1[pr_map[i]])
            if (g2w >= calc_weight(rms2[pr_map[i]])):
                g2w = calc_weight(rms2[pr_map[i]])
        except:
            pass
        flux+=image1[pr_map[i]]
        background +=rms1[pr_map[i]]**2
    ston = flux/sqrt(background)

    size = int((sqrt(len(pr_map))/2.0)+1.0)
    icd = []
    err = []

    for i in range(9):
        back1=back2=0
        while (0 == back1):
            back1 = get_background_pr(segmap,image1,rms1,size,g1w,naxes)
        while (0 == back2):
            back2 = get_background_pr(segmap,image2,rms2,size,g2w,naxes)

        ICD = calc_icd_pr(alpha, beta, galaxy_num, pr_map, image1, image2,
                back1, back2)
        ERR = icd_error_pr(alpha, beta, pr_map, galaxy_num, image2, back1,
                back2)
        icd.append(ICD)
        err.append(ERR)

    signal.alarm(0)
    ICD = np.median(np.asarray(icd))
    ERR = np.median(np.asarray(err))
    print galaxy_num,ICD,ERR

    f1.writelines(str(galaxy_num)+" ")
    f1.writelines(str(ICD)+" ")
    f1.writelines(str(ERR)+" ")
    f1.writelines(str(ston)+" ")
    f1.writelines(str(pr)+" ")
    f1.writelines(str(alpha))
    f1.close()
# --- END OF MAIN FUNCTION --- #

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
