
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>



//initialisation des variables
double sigma = 5.67e-8;
double rayonnement = 1000;
double temperature_surface = 0;
double* albedo_c

//loi de stefan
double stefan(double* albedo_matrix, double* emissivity_matrix, double sigma){
    temperature_surface = pow((((1-(double* albedo_matrix))*rayonnement)/((emissivity_matrix)*sigma)),(1/4));
    return temperature_surface;
}


int main(int argc, char * argv[]) {
    
    double T = stefan(double* albedo_matrix, double* emissivity_matrix, double sigma);
    

    return 0;
}