#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>



double  **lireCSV(char * nomFichier, int *nblignes, int*nbcolonnes) {
    // Ouvrir le fichier
    FILE * file = fopen(nomFichier, "r");
    if (file == NULL) return -1;

    // Lire ligne par ligne
    int n = 0;
    char buffer[1024];
    double **matrice = NULL;
    *nblignes = 0;
    *nbcolonnes = 0;


    while (fgets(buffer, 1024, file) != NULL) {
        char *token = strtok(buffer, ",");
        int col = 0;

        //reallocation pour une nouvelle ligne
        matrice = realloc(matrice, (*nblignes + 1) * sizeof(double *));
        matrice[*nblignes] = NULL;


         while (token) {
            matrice[*nblignes] = realloc(matrice[*nblignes], (col + 1) * sizeof(double));
            matrice[*nblignes][col] = atof(token);
            token = strtok(NULL, ",");
            col++;
        }

        if (col > *nbcolonnes) *nbcolonnes = col;
        (*nblignes)++;
    }

    fclose(file);
    return matrice;
}




int main() {
    int lignes, colonnes;
    double **matrice = lireCSV("projet1/albedo_matrix.csv", &lignes, &colonnes);

    if (!matrice) return 1;

    printf("Matrice %d x %d :\n", lignes, colonnes);
    for (int i = 0; i < lignes; i++) {
        for (int j = 0; j < colonnes; j++) {
            printf("%8.3f ", matrice[i][j]);
        }
        printf("\n");
    }


    // Libération mémoire
    for (int i = 0; i < lignes; i++) {
        free(matrice[i]);
    }
    free(matrice);

    return 0;
}







