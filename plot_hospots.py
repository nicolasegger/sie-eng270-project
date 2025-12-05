from scipy.ndimage import gaussian_filter
from matplotlib.colors import ListedColormap
from pixel import * 
import numpy as np
import matplotlib.pyplot as plt
from plot_tempmap import *

# On repart de ta variable 'fliped' déjà calculée
hot_threshold = 355.0  # K

# Masque des zones chaudes (>= seuil)
hot_mask = fliped >= hot_threshold

# Prépare une image où seuls les pixels chauds sont visibles, le reste en NaN (transparent)
hot_only = np.where(hot_mask, fliped, np.nan)

plt.figure(figsize=(8, 6))
# Fond en gris clair pour "le reste"
plt.imshow(fliped, cmap="Greys", origin="lower", alpha=0.25)
# Superpose les zones chaudes en 'inferno' '''
'''im = plt.imshow(hot_only, cmap="inferno", origin="lower")

# Colorbar calée sur la plage des pixels chauds
if np.isfinite(hot_only).any():
    cbar = plt.colorbar(im, label="Température (K)")
    # Option: borne la colorbar autour du seuil pour lisibilité
    vmin = hot_threshold
    vmax = np.nanmax(hot_only)
    im.set_clim(vmin=vmin, vmax=vmax)'''

# Ajoute un contour cyan autour des zones chaudes pour les repérer facilement
plt.contour(hot_mask.astype(int), levels=[1], colors="cyan", linewidths=1.2, origin="lower")

plt.title(f"Zones les plus chaudes (T ≥ {hot_threshold:.1f} K)")
plt.axis("off")
plt.show()