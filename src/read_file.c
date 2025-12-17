 files#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define ROWS 100
#define COLS 100
#define MAX_LINE_LENGTH 4096

const double sigma = 5.67e-8;

// open files
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

//define stefan's law
double stefan_radiative_eq(double albedo, double emissivity,
                           double S_down, double Ta_K, double ea_Pa)
{
    double ea_mb = ea_Pa / 100.0;
    double epsilon_a = 1.24 * pow(ea_mb / Ta_K, 1.0/7.0);
    if (epsilon_a > 1.0) epsilon_a = 1.0;
    if (epsilon_a < 0.0) epsilon_a = 0.0;
    double L_down = epsilon_a * sigma * pow(Ta_K, 4.0);

    double denom = emissivity * sigma;
    if (denom <= 0.0) denom = 1e-9;

    double numerateur = (1.0 - albedo) * S_down + emissivity * L_down;
    return pow(numerateur / denom, 0.25);
}

//main
int main() {
    double albedomatrix[ROWS][COLS];
    double emissivitymatrix[ROWS][COLS];
    double tempMatrix[ROWS][COLS];

    lire_csv("../data/albedo_matrix.csv", albedomatrix);
    lire_csv("../data/emissivity_matrix.csv", emissivitymatrix);

// parametrisation
    double Ta_K   = 298.15;
    double ea_Pa  = 1500.0;
    double S_down = 800.0;           
//creating the matrix
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            double albedo    = albedomatrix[i][j];
            double emissivity = emissivitymatrix[i][j];
            double T = stefan_radiative_eq(albedo, emissivity, S_down, Ta_K, ea_Pa);
            tempMatrix[i][j] = T - 50;
        }
    }

//crearting temperature_matrixe.csv
    FILE *fp = fopen("../results/temperature_matrixe.csv", "w");
    if (fp == NULL) {
        perror("Erreur lors de la création du fichier CSV");
        return 1;
    }
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            fprintf(fp, "%.2f", tempMatrix[i][j]);
            if (j < COLS - 1) fprintf(fp, ",");
        }
        fprintf(fp, "\n");
    }
    fclose(fp);
    printf("Fichier CSV créé : temperature_matrixe.csv\n");
    return 0;
}
