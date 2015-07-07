#include "header.h"

int image_size(char reffile[],long naxes[]){
/*CFTISIO VARIABLES */
    fitsfile *fptr;             /* FITS file pointer, defined in fitsio.h */
    int status = 0;             /* CFITSIO status value MUST be initialized to zero! */
    int bitpix, naxis;
    FILE *file;

if (!fits_open_file(&fptr, reffile, READONLY, &status)) {
    if (!fits_get_img_param(fptr, 2, &bitpix, &naxis, naxes, &status)) {
        if (naxis > 2 || naxis == 0)
            printf("Error: only 1D or 2D images are supported\n");
        }
        }
if (status) {
        fits_report_error(stderr, status);  /* print any error message */
        return (status);
        }
return(0);
}


