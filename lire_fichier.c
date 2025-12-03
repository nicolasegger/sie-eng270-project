#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ROWS 100
#define COLS 100
#define MAX_LINE_LENGTH 2048


void lire_csv(const char *filename, double matrix[ROWS][COLS]) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error");// error if file doesn't open
        exit(1);
    }

    char line[MAX_LINE_LENGTH];
    int row = 0;

    while (fgets(line, sizeof(line), file) && row < ROWS) {
        char *token = strtok(line, ","); //cut the line at every ","
        int col = 0;

        while (token != NULL && col < COLS) {
            matrix[row][col] = atof(token); //convert the .csv value into a number (double)
            token = strtok(NULL, ",");
            col++;
        }
        row++;
    }

    fclose(file);
    
}

//initialisation des variables
double sigma = 5.67e-8;
double rayonnement = 1000;
double temperature_surface = 0;

//loi de stefan
double stefan(double* matrix1, double* matrix2, double sigma){
    temperature_surface = pow((((1-(double* albedo_matrix))*rayonnement)/((emissivity_matrix)*sigma)),(1/4));
    return temperature_surface;
}


int main() {
    double albedomatrix[ROWS][COLS];
    double emissivitymatrix[ROWS][COLS];

    // read 2 files
    lire_csv("albedo_matrix.csv", albedomatrix);
    lire_csv("emissivity_matrix.csv", emissivitymatrix);
    
   
/*
    // Exemple d'affichage de la matrice
    printf("Matrice lue (première ligne):\n");
    for (int j = 0; j < COLS; j++) {
        printf("%.10f ", matrix[0][j]);
    }
    printf("\n");
*/
    return 0;
}


