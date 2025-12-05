import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv

#define directories
projroot = Path(sys.path[0]).parent
#charge the image
image_path = projroot / "data" / "epfl_sat.jpg"
image = mpimg.imread(image_path)
#number of pixels
target_height, target_width = 100, 150
#steps size
h_step = image.shape[0] // target_height 
w_step = image.shape[1] // target_width

#creating reduced image
small_image = np.zeros((target_height, target_width, image.shape[2]), dtype=np.float32)
for i in range(target_height):
    for j in range(target_width):
        block = image[i*h_step:(i+1)*h_step, j*w_step:(j+1)*w_step]
        small_image[i,j] = block.mean(axis=(0, 1))

#pixelated_image = np.kron(small_image, np.ones((h_step, w_step, 1)))
#small_image : la version reduite (par exemple 50 fois 50 pixels).
#np.ones((h_step, w_step, 1)) : une matrice de 1 qui sert a repeter chaque pixel.
#np.kron(A, B) : prend chaque element de A et le multiplie par la matrice B, ce qui revient a repliquer chaque pixel en un bloc.
#chaque  pixel devient un gros carre-->agrandissement
out_path1 = projroot / "data" / "image_pixellisee.jpg"

plt.imsave(out_path1, small_image.astype(np.uint8))
sys.path.append(str(projroot / "src"))

from classify import *

#creating an emissivity matrix based on rgb
emissivity_matrix = np.zeros((small_image.shape[0],small_image.shape[1]), dtype=float)
for i in range(small_image.shape[0]):
    for j in range(small_image.shape[1]):
        rgb = small_image[i,j]
        surface_class = classify_pixel_emissivite(rgb)
        emissivity_matrix[i, j] = emissivity_table[surface_class]
out_path2 = projroot / "data" / "emissivity_matrix.csv"
np.savetxt(out_path2, emissivity_matrix, delimiter=',')


#creating an albedo matrix based on rgb
albedo_matrix = np.zeros((small_image.shape[0], small_image.shape[1]), dtype=float)
for i in range(small_image.shape[0]):
    for j in range(small_image.shape[1]):
        rgb = small_image[i,j]
        surface_class = classify_pixel_albedo(rgb)
        albedo_matrix[i, j] = albedo_table[surface_class]
out_path3 = projroot / "data" / "albedo_matrix.csv"
np.savetxt(out_path3, albedo_matrix, delimiter=',')
