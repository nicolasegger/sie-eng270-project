#python3 ~src./pixel.py data./epfl_sat.jpg

python3 src/pixel.py src/classify.py data/epfl_sat.jpg
gcc gcc src/lire_fichier.c -o src/lire_fichier
./src/lire_fichier data/albedo_matrix.csv data/emissivity_matrix.csv data/temperature_matrix.csv

python3 src/plot_tempmap.py data/temperature_matrix