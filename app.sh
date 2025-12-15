#python3 ~src./pixel.py data./epfl_sat.jpg

#cd $(find . -name "CMT" -type d | head -n 1)


#!/bin/bash
set -e
set -x
#cd "$(dirname "$0")"

#demander au prof ou sera le dossier
 #modif!!!
# 1. treatment of the image
python3 src/pixel.py src/classify.py data/plainpalais.jpg

# 2. porgramm C compilation
gcc src/read_file.c -o bin/read_file -lm

# 3. execution of the programm C
cd bin
./read_file data/albedo_matrix.csv data/emissivity_matrix.csv results/temperature_matrixe.csv
cd ..
# 4. final overlay
python3 src/overlay.py results/temperature_matrixe.csv
















#python3 src/pixel.py src/classify.py data/epfl_sat.jpg
#gcc lire_fichier ../data/albedo_matrix.csv ../data/emissivity_matrix.csv ../data/temperature_matrix.csv

#python3 src/superposition.py data/temperature_matrix