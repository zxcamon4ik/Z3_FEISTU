/*
 *  Swish aktivacna funkcia a pomocne funkcie
 */

#ifndef FUNCTIONS_H
#define FUNCTIONS_H

// aktivacna funkcia neuronovej siete
double swish(double x);
// funkcia na nacitanie pixelov obrazku do pola
void load_image(double *img, unsigned int len);
// funkcia na vypis obrazku
void print_image(const double* img, const unsigned int img_width, const unsigned int img_height);

#endif //FUNCTIONS_H




