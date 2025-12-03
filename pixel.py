
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
# Charger l'image
image = mpimg.imread("epfl_sat.jpg")  # Remplace par ton fichier ATTENTION, EN .jpg !!!!!!!
#nombre de pixels
target_height, target_width = 100, 100
#taille des pas
h_step = image.shape[0] // target_height 
w_step = image.shape[1] // target_width

#creer une image reduite
small_image = np.zeros((target_height, target_width, image.shape[2]), dtype=np.float32)
for i in range(target_height):
    for j in range(target_width):
        block = image[i*h_step:(i+1)*h_step, j*w_step:(j+1)*w_step]
        small_image[i,j] = block.mean(axis=(0, 1))

#pixelated_image = np.kron(small_image, np.ones((h_step, w_step, 1)))
#small_image : la version réduite (par exemple 50×50 pixels).
#np.ones((h_step, w_step, 1)) : une matrice de 1 qui sert à répéter chaque pixel.
#np.kron(A, B) : prend chaque élément de A et le multiplie par la matrice B, ce qui revient à répliquer chaque pixel en un bloc.
#chaque  pixel devient un gros carré-->agrandissement



#plt.imshow(pixelated_image.astype(np.uint8))
#plt.axis("off")  # Pour enlever les axes
#plt.imsave("image_pixellisee.jpg", pixelated_image.astype(np.uint8))
plt.imsave("image_pixellisee.jpg", small_image.astype(np.uint8))
#plt.show()


"""
plt.show()
#Afficher les images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image)
axes[0].set_title("Image originale")
axes[0].axis("off")

axes[1].imshow(pixelated_image.astype(np.uint8))
axes[1].set_title("Image pixellisée")
axes[1].axis("off")

plt.show()

# Afficher la matrice des pixels réduits
print("Matrice des pixels réduits :", small_image.shape)
print(small_image)
"""

from classify import *


emissivity_matrix = np.zeros((small_image.shape[0],small_image.shape[1]), dtype=float)
for i in range(small_image.shape[0]):
    for j in range(small_image.shape[1]):
        rgb = small_image[i,j]
        surface_class = classify_pixel_emissivite(rgb)
        emissivity_matrix[i, j] = emissivity_table[surface_class]
np.savetxt('emissivity_matrix.csv', emissivity_matrix, delimiter=',')



albedo_matrix = np.zeros((small_image.shape[0], small_image.shape[1]), dtype=float)
for i in range(small_image.shape[0]):
    for j in range(small_image.shape[1]):
        rgb = small_image[i,j]
        surface_class = classify_pixel_albedo(rgb)
        albedo_matrix[i, j] = albedo_table[surface_class]
np.savetxt('albedo_matrix.csv', albedo_matrix, delimiter=',')
