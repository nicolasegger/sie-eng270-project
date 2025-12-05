#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define ROWS 100
#define COLS 100
#define MAX_LINE_LENGTH 4096

/*
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

double stefan(double albedo, double emissivity, double sigma, double rayonnement) {
    // Stefan-Boltzmann law: T = [ ( (1 - albedo) * rayonnement ) / (emissivity * sigma) ]^(1/4)
    double temperature_surface = pow(((1.0 - albedo) * rayonnement) /(emissivity * sigma), (1.0/4.0));
    return temperature_surface;
}


double tempMatrix[ROWS][COLS];
int main() {
    double albedomatrix[ROWS][COLS];
    double emissivitymatrix[ROWS][COLS];

    // read 2 files
    lire_csv("albedo_matrix.csv", albedomatrix);
    lire_csv("emissivity_matrix.csv", emissivitymatrix);
    
    // calculs

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            double albedo = albedomatrix[i][j];
            double emissivity = emissivitymatrix[i][j];
            double T = stefan(albedo, emissivity, sigma, rayonnement);
            tempMatrix[i][j] = T;
        }
    }

    FILE *fp = fopen("temperature_matrixe.csv", "w");
        if (fp == NULL) {
            perror("Erreur lors de la création du fichier CSV");
            return 1;
        }

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                fprintf(fp, "%.2f", tempMatrix[i][j]);
                if (j < COLS - 1) {
                    fprintf(fp, ",");
                }
            }
            fprintf(fp, "\n");
        }

        fclose(fp);
        printf("Fichier CSV créé : temp_matrixe.csv\n");

    return 0;
}


    // Exemple d'affichage de la matrice
    printf("Matrice lue (première ligne):\n");
    for (int j = 0; j < COLS; j++) {
        printf("%.10f ", matrix[0][j]);
    }
    printf("\n");



*/


// ... tes #include ...



// ---- NOUVEAU : constants + stefan amélioré ----
const double sigma = 5.67e-8;


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

// ---- ta fonction lire_csv(...) inchangée ----

// ---- variables globales si tu y tiens ----
// double sigma = 5.67e-8;   // <- si tu l’avais ici, garde une seule définition

int main() {
    double albedomatrix[ROWS][COLS];
    double emissivitymatrix[ROWS][COLS];
    double tempMatrix[ROWS][COLS];

    lire_csv("albedo_matrix.csv", albedomatrix);
    lire_csv("emissivity_matrix.csv", emissivitymatrix);

    // ---- NOUVEAU : paramètres atmosphériques ----
    double Ta_K   = 298.15;
    double ea_Pa  = 1500.0;
    double S_down = 800.0;            // ou "rayonnement" si tu veux garder ta variable

    // ---- NOUVELLE BOUCLE DE CALCUL ----
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            double albedo    = albedomatrix[i][j];
            double emissivity = emissivitymatrix[i][j];
            double T = stefan_radiative_eq(albedo, emissivity, S_down, Ta_K, ea_Pa);
            tempMatrix[i][j] = T;
        }
    }

    // ---- sortie CSV (nom corrigé) ----
    FILE *fp = fopen("temperature_matrix.csv", "w");
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
