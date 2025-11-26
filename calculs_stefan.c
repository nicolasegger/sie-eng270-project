#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


//initialisation des variables
double sigma = 5.67e-8;
double rayonnement = 1000;
double temperature_surface = 0;

//loi de stefan
double stefan(double* albedo_matrix, double sigma){
    temperature_surface = pow((((1-(double* albedo_matrix))*rayonnement)/(0.95*sigma)),(1/4));
    return temperature_surface;
}


int main(int argc, char * argv[]) {
    // Vérifier le nombre de paramètres
    if (argc != 3) {
        printf("Utilisation:\n");
        printf("./projet FICHIER SEUIL\n");
        return 1;
    }

    // Lire les paramètres
    int * matrix_height = argv[1];
    int * matrix_length = argv[2];

    // Vérifier le seuil
    if (seuil < 10) {
        printf("Le seuil doit être 10 ou plus grand.\n");
        return 1;
    }

    ...

    return 0;
}