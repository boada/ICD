#include "header.h"

int write_image(char filename[], float image[], long naxes[])
{

    fitsfile *fptr;		/* pointer to the FITS file, defined in fitsio.h */
    int status, ii, jj, x, y;
    int naxis = 2;
    int bitpix = FLOAT_IMG;	//USHORT_IMG;       /* 16-bit unsigned short pixel values       */
    long fpixel, nelements, exposure;
    float *array[naxes[0]];


    /* allocate memory for the whole image */
    array[0] = (float *) malloc(naxes[0] * naxes[1] * sizeof(float));
    /* initialize pointers to the start of each row of the image */
    for (ii = 1; ii < naxes[1]; ii++)
	array[ii] = array[ii - 1] + naxes[0];

    remove(filename);		/* Delete old file if it already exists */

    status = 0;			/* initialize status before calling fitsio routines */

    if (fits_create_file(&fptr, filename, &status))	/* create new FITS file */
	printerror(status);	/* call printerror if error occurs */

    if (fits_create_img(fptr, bitpix, naxis, naxes, &status))
	printerror(status);

    for (jj = 0; jj < naxes[1]; jj++) {
	for (ii = 0; ii < naxes[0]; ii++) {
	    array[jj][ii] = image[ii + naxes[0] * jj];
	}
    }
    fpixel = 1;			/* first pixel to write      */
    nelements = naxes[0] * naxes[1];	/* number of pixels to write */

    /* write the array of unsigned integers to the FITS file */
    if (fits_write_img(fptr, TFLOAT, fpixel, nelements, array[0], &status))
	printerror(status);

    free(array[0]);		/* free previously allocated memory */

    if (fits_close_file(fptr, &status))	/* close the file */
	printerror(status);

    return;
}
