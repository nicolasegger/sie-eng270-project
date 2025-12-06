
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from PIL import Image
import sys
from pathlib import Path

projroot = Path(sys.path[0]).parent
path = projroot / "data" / "image_pixellisee.jpg"

# --- Paramètres ---
hot_threshold = 355.0  # K
smooth_sigma = 0.0     # Gaussian smoothing pour le masque (0 = pas de lissage)
base_cmap = "Greys"    # Colormap pour l'image de fond
contour_color = "cyan" # Couleur du contour
contour_width = 1.5    # Épaisseur du contour
alpha_base = 1.0       # Transparence de l'image de fond (1.0 = opaque)

# --- Donnée d'entrée attendue : 'fliped' ---
# Assure-toi que la variable 'fliped' est définie avant d'exécuter ce code.
# fliped = ...  # ton tableau 2D de températures (en K)

# 1) Calcul du masque chaud (>= seuil)
image = Image.open(path)
hot_mask = image >= hot_threshold

# 2) Optionnel : lissage pour obtenir des contours plus doux
if smooth_sigma and smooth_sigma > 0:
    # On lisse l'image de température, puis on recalcule le masque sur l'image lissée
    fliped_smooth = gaussian_filter(image, sigma=smooth_sigma)
    hot_mask_for_contour = fliped_smooth >= hot_threshold
else:
    hot_mask_for_contour = hot_mask

# 3) Affichage : image originale + contour des zones chaudes
plt.figure(figsize=(8, 6))

# Image de fond (originale)
im_base = plt.imshow(image, cmap=base_cmap, origin="lower", alpha=alpha_base)
plt.title(f"Contours des zones chaudes superposés (T ≥ {hot_threshold:.1f} K)")
plt.axis("off")

# 4) Superposition du contour (en cyan, par défaut)
# Utilise levels=[1] car hot_mask est binaire (0/1)
plt.contour(
    hot_mask_for_contour.astype(int),
    levels=[1],
    colors=contour_color,
    linewidths=contour_width,
    origin="lower",
)

# 5) Optionnel : colorbar de l'image de fond (température)
cbar = plt.colorbar(im_base, label="Température (K)")
# Si tu veux fixer la plage de couleurs :
# im_base.set_clim(vmin=np.nanmin(fliped), vmax=np.nanmax(fliped))

plt.show()
