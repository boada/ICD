#include "header.h"

int
fit(double image1[], double image2[], double error[], float factors[],
    int n)
{
/*
    if (gsl_fit_wlinear
	(image1, 1, error, 1, image2, 1, n, &beta, &alpha, &cov00, &cov01,
	 &cov11, &chisq)) {
	fprintf(stderr, "Linear Fitting Failed!\n");
	return (1);
    }

    factors[0] = alpha;
    factors[1] = beta;
*/
/*SECOND SET OF VARIABLES!!!*/
    int i;
    double chisq;
    gsl_matrix *X, *cov;
    gsl_vector *y, *w, *c;
	
    X = gsl_matrix_alloc(n, 2);
    y = gsl_vector_alloc(n);
    w = gsl_vector_alloc(n);
    c = gsl_vector_alloc(2);
    cov = gsl_matrix_alloc(2, 2);
	
    for (i = 0; i < n; i++) {
	gsl_matrix_set(X, i, 0, 1.0);
	gsl_matrix_set(X, i, 1, image1[i]);
	gsl_vector_set(y, i, image2[i]);
	gsl_vector_set(w, i, error[i]);
    }
	
    gsl_multifit_linear_workspace *work = gsl_multifit_linear_alloc(n, 2);
    gsl_multifit_wlinear(X, w, y, c, cov, &chisq, work);
    gsl_multifit_linear_free(work);

#define C(i) (gsl_vector_get(c,(i)))

//  printf("# best fit: Y = %g + %g X\n", C(0), C(1));

    gsl_matrix_free(X);
    gsl_vector_free(y);
    gsl_vector_free(w);
    gsl_vector_free(c);
    gsl_matrix_free(cov);

    factors[0] = C(1);
    factors[1] = C(0);
	return 0;
}
