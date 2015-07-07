#include "header.h"

int calc_pr(float image[], float segmap[], float galaxy_num, int x_center,
	    int y_center, long naxes[])
{

    int i, x, y, radius;
    int n_inside, n_radius;
    float pr, sum_inside, sum_radius, d;
    pr = 1.0;
    radius = 0;

if (segmap[x_center+naxes[0]*y_center] != galaxy_num) {
	printf("Galaxy Center Not Found!\n");
	return(radius);
}

    while (pr >= 0.2) {
	sum_inside = sum_radius = 0.0;
	n_inside = n_radius = 0;
	radius++;
	for (i = 0; i < naxes[0] * naxes[1]; i++) {
		if (segmap[i] == galaxy_num){
		y = i / naxes[0];
		x = i - y * naxes[0];
		}
	    if (segmap[i] == galaxy_num || segmap[i] == 0) {

		y = i / naxes[0];
		x = i - y * naxes[0];

		d = sqrt(pow((x - x_center), 2) + pow((y - y_center), 2));

		if (d < (float) radius) {
		    sum_inside += image[i];
		    n_inside++;
		}
		if (d >= (float) radius && d < (float) (radius + 1)) {
		    sum_radius += image[i];
		    n_radius++;
		}
	    }

	}

	pr = (sum_radius / n_radius) / (sum_inside / n_inside);
	/*
	   printf("# Inside = %d # Radius = %d\n", n_inside, n_radius);
	   printf("Inside = %f Radius = %f\n", sum_inside, sum_radius);
	   printf("Radius = %d\n", radius);
	   printf("Pr = %f\n", pr);
	   fprintf(f1,"%d %f\n",radius,pr);
	*/
    }
	   printf("Pr = %d\n", radius);
    return (radius);
}
