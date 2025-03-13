/*
 *  Swish aktivacna funkcia a pomocne funkcie
 */

#include <stdio.h>
#include <math.h>
#include "functions.h"

// Swish aktivacna funkcia
double swish(const double x){
    double beta = 0.5;
    return x/(1+ exp(-beta*x));
}

// funkcia na nacitanie pixelov obrazku 'img' s dlzkou 'len'
// zo standardneho vstupu (stdin)
void load_image(double *img, const unsigned int len){
    for(unsigned int i = 0; i< len;i++){
        scanf("%lf", &img[i]);
    }
}

// funkcia na vypis obrazku 'img' (ocakavaju sa pixely v rozsahu <0,1>)
// obrazok 'img' ma sirku 'img_width' a vysku 'img_height'
// Poznamka: pole 'img' je 1D pole, ktore predstavuje pixely obrazku (pixely su v nom usporiadane tak,
// ako idu v obrazku po riadkoch)
void print_image(const double* img, const unsigned int img_width, const unsigned int img_height){
    char white[3] = "WW";
    char black[3] = "..";
    for(unsigned int i=0; i<img_height;i++){
        for(unsigned int j=0; j<img_width;j++){
            if(img[i*img_height+j]>=0.10){
                printf("%s", white);
            }
            else{
                printf("%s", black);
            }
        }
        printf("\n");
    }
    printf("\n");
}



