#python3 ~src./pixel.py data./epfl_sat.jpg

#find . -name "app.sh"
#cd ~/Desktop/myfiles/CMT

#!/bin/bash
set -e
set -x
#cd "$(dirname "$0")"

# 1. Traitement de l'image satellite
python3 src/pixel.py src/classify.py data/epfl_sat.jpg

# 2. Compilation du programme C
gcc src/lire_fichier.c -o src/lire_fichier -lm

# 3. Exécution du programme C
cd src
./lire_fichier data/albedo_matrix.csv data/emissivity_matrix.csv data/temperature_matrixe.csv
cd ..
# 4. Superposition finale
python3 src/superposition.py data/temperature_matrixe.csv
















#python3 src/pixel.py src/classify.py data/epfl_sat.jpg
#gcc lire_fichier ../data/albedo_matrix.csv ../data/emissivity_matrix.csv ../data/temperature_matrix.csv

#python3 src/superposition.py data/temperature_matrix