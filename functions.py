#!/usr/bin/python

import math
from ctypes import *

# Load the library for the CFitsio routines
overseer = CDLL("/home/steven/Projects/galaxy_icd/libraries/liboverseer.so.0")

def read_cat_fits(reffile):
    import pyfits
    hdulist = pyfits.open(reffile)
    tbdata = hdulist[1].data
    return tbdata

def convert(input, output,naxes,band=False):
    zpt = 0.0
    if band == 'B':
        zpt = 25.68386
    elif band == 'V':
        zpt = 26.50507
        #zpt = 25.97
    elif band == 'I':
        zpt = 25.67853
        #zpt = 24.94
    elif band == 'Z':
        zpt = 24.86658
        #zpt = 24.38
    elif band == 'Y':
        zpt = 26.24728
        #zpt = 26.27
    elif band == 'J':
        zpt = 26.24728
        #zpt = 26.25
    elif band == 'H':
        zpt = 25.95582
        #zpt = 25.96
    convert = 10**(-0.4*(zpt-23.9))

    for j in range(naxes[1]):
        for i in range(naxes[0]):
            if not band == False:
                output[i+naxes[0]*j] = input[j][i] * convert
            else:
                output[i+naxes[0]*j] = input[j][i]
    return output

def calc_scale_factors3(pr_map, image1, image2, rms):
    from astLib import astStats
    import numpy as np
    galaxy1=[]
    galaxy2=[]
    error=[]
    arr=[]
    for i in range(len(pr_map)):
        galaxy1.append(image1[pr_map[i]])
        galaxy2.append(image2[pr_map[i]])
        error.append(rms[pr_map[i]])

    datalist =np.column_stack((galaxy1, galaxy2, error))
    result = astStats.weightedLSFit(datalist, 'errors')
    return result['slope'], result['intercept']

############################################################
# This function fits a stright line to the galaxy pixels.  #
# Basically, this function calculates Alpha and Beta which #
# are used in the ICD calucations. It does a good job.     #
############################################################

def calc_scale_factors(gal_num,pr_map,image1,image2,rms):
    factors = (c_float*2)(-1.0)
    error = (c_double*len(pr_map))(-1.0)
    galaxy1 = (c_double*len(pr_map))(-1.0)
    galaxy2 = (c_double*len(pr_map))(-1.0)

    # Prep the galaxies to be fit.
    for i in range(len(pr_map)):
        galaxy1[i] = image1[pr_map[i]]
        galaxy2[i] = image2[pr_map[i]]
        error[i] = calc_weight(rms[pr_map[i]])

    overseer.fit(galaxy1,galaxy2,error,factors,len(pr_map))
    alpha = factors[0]
    beta = factors[1]

    return alpha,beta

######################################################
# This calculates a "weight map" for the images that #
# we are interested in. The weight is just 1/RMS^2   #
# This is used in the ICD calulations as a check.    #
######################################################

def calc_weight(rms):
    if rms == 0.0:
        rms = 1E-5
    weight = 1./math.pow(rms,2)
    return weight

##############################################################
# This function returns a contiguous section of pixels       #
# for use in the background subtraction. It returns 0        #
# if the pixels selected don't meet the required conditions. #
##############################################################

def get_background_pr(segmap,image,rms,size,weight,naxes):
    import random
    background =[]
    pix = random.randint(0,naxes[0]*naxes[1]-1)
    #print pix
    #print len(segmap), len(image),len(rms),size,naxes[0],naxes[1]
    try:
        if not image[pix] == 0.0:
            y_coor = pix/naxes[0]
            x_coor = pix - y_coor*naxes[0]
            for i in range((x_coor-size),(x_coor+size)):
                for j in range((y_coor-size),(y_coor+size)):
                    pix = i+naxes[0]*j
                    if segmap[pix] != 0:
                        #print "galaxy found"
                        return 0
                    elif image[pix] == 0.0:
                        #print "Pixel Zero"
                        return 0
                    elif rms[pix] == 0.0:
                        #print "rms bad"
                        return 0
                    elif (calc_weight(rms[pix]) < weight):
                        #print "Pixel Weight"
                        return 0
                    else:
                        background.append(image[pix])

        else:
            #print "No Flux"
            return 0
        #print "Sucess!"
        return background
    except:
        return 0

#############################################################
# This function creates a map of the data that will be used #
# to calculate the ICD. It serves the same function as the  #
# segmap but it is for the singular galaxy in question and  #
# does not contain all of the data for all of the galaxies. #
#############################################################

def make_pr_map(image,segmap,galaxy_num,x_center,y_center,radius,naxes):
	pr_map = []
	for i in range(0,naxes[0]*naxes[1]):
		if (segmap[i] == galaxy_num or segmap[i] == 0 and image[i] != 0):
			y = i/naxes[0]
			x = i - y*naxes[0]
			d = math.sqrt(math.pow(x-x_center,2) + math.pow(y-y_center,2))

			if (d < radius):
				pr_map.append(i)
				#print x,y, 'x,y-pr'
			if (d >= radius and d < (radius+1)):
				pr_map.append(i)
				#print x,y, 'x,y-pr'

	return pr_map

#####################################################
# This is the main ICD calculator. All of the real  #
# "work" happens in this function. This function    #
# uses the Pertrosian radius and not the segmap for #
# all of the calculations.                          #
#####################################################

def calc_icd_pr(alp,bet,galaxy_num,pr_map,i1,i2,b1,b2):
    a=b=c=d=0.0

	#This is the main ICD calulcation.
    for i in range(len(pr_map)):
        a += math.pow(i2[pr_map[i]] - alp*i1[pr_map[i]] - bet,2)
        b += math.pow(b2[i] - alp*b1[i],2)
        c += math.pow(i2[pr_map[i]] - bet,2)

    icd = (a-b)/(c-b)
    #icd = (a)/(c)

    return icd

#########################################################################
# This function simply uses the petrosian radius instead of the segmap. #
#########################################################################

def icd_error_pr(alp,bet,pr_map,galaxy_num,image,b1,b2):
	a=b=c=0.0

	for i in range(len(pr_map)):
		a+= math.pow(b2[i],2) + math.pow(alp,2)*math.pow(b1[i],2)
		b+= math.pow(image[pr_map[i]] - bet,2)
		c+= math.pow(b2[i] - alp*b1[i],2)

	err = (math.sqrt(2.0/len(pr_map))*a)/(b-c)

	return err

