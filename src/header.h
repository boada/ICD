#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "fitsio.h"
#include <gsl/gsl_fit.h>
#include <gsl/gsl_multifit.h>

//The Function Declarations
int read_image(char[],float[],long[]);
int read_table(char[]);
int write_image(char[],float[],long[]);
int image_size(char[], long[]);
int fit(double[],double[],double[],float[],int);
int calc_pr(float[],float[],float,int,int,long[]);
void printerror(int);
