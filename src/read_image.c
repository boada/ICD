#include "header.h"

int read_image(char reffile[], float image[], long naxes[])
{
    fitsfile *fptr;		/* FITS file pointer */
    int status = 0;		/* CFITSIO status value MUST be initialized to zero! */
    int hdutype, naxis, ii, j;
    long totpix, fpixel[2];
    double *pix,maxval =0.0;

    if (!fits_open_image(&fptr, reffile, READONLY, &status)) {
	if (fits_get_hdu_type(fptr, &hdutype, &status)
	    || hdutype != IMAGE_HDU) {
	    printf
		("Error: this program only works on images, not tables\n");
	    return (1);
	}

	fits_get_img_dim(fptr, &naxis, &status);
	// fits_get_img_size(fptr, 2, naxes, &status);

	if (status || naxis != 2) {
	    printf("Error: NAXIS = %d.  Only 2-D images are supported.\n",
		   naxis);
	    return (1);
	}

	pix = (double *) malloc(naxes[0] * sizeof(double));	/* memory for 1 row */

	if (pix == NULL) {
	    printf("Memory allocation error\n");
	    return (1);
	}

	totpix = naxes[0] * naxes[1];
	fpixel[0] = 1;		/* read starting with first pixel in each row */

	/* process image one row at a time; increment row # in each loop */
	j = 0;
	for (fpixel[1] = 1; fpixel[1] <= naxes[1]; fpixel[1]++) {
	    /* give starting pixel coordinate and number of pixels to read */
	    if (fits_read_pix
		(fptr, TDOUBLE, fpixel, naxes[0], 0, pix, 0, &status))
		break;		/* jump out of loop on error */

	    for (ii = 0; ii < naxes[0]; ii++) {
		image[ii + naxes[0] * j] = (float) pix[ii];
		if (pix[ii] > maxval)
		    maxval = pix[ii];	/* max values    */
	    }
	    j++;
	}

	free(pix);
	fits_close_file(fptr, &status);
    }

    if (status) {
	fits_report_error(stderr, status);	/* print any error message */
    }
    //return(status);
    return (maxval);
}
