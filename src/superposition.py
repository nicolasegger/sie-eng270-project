
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image, ImageOps
import sys

# --- paramètres & chemins ---
projroot = Path(sys.path[0]).parent
matrix_path = projroot / "data" / "temperature_matrixe.csv"
pix_path = projroot / "data" / "image_pixellisee.jpg"
epfl_path = projroot / "data" / "epfl_sat.jpg"
plainpalais_path = projroot / "data" / "plainpalais.jpg"
out_tempmap_png = projroot / "results" / "tempmap.png"       # carte des températures
out_overlay_png = projroot / "results" / "overlay_contours.png"  # superposition finale
img = Image.open(pix_path)
width, height = img.size
# --- charge données ---
data = np.loadtxt(matrix_path, delimiter=",")

data_img = Image.fromarray(data)
data = np.array(data_img.resize((width, height), resample=Image.NEAREST))


# Filtre moyenneur (si nécessaire)
def mean_filter_2d(arr, k=9):
    if k % 2 == 0:
        raise ValueError("k doit être impair")
    pad = k // 2
    arr_p = np.pad(arr, pad_width=pad, mode='edge')
    cumsum_h = np.cumsum(arr_p, axis=1)
    h = (cumsum_h[:, k:] - cumsum_h[:, :-k]) / k
    h_p = np.pad(h, ((pad, pad), (0, 0)), mode='edge')
    cumsum_v = np.cumsum(h_p, axis=0)
    v = (cumsum_v[k:, :] - cumsum_v[:-k, :]) / k
    return v

smoothed = mean_filter_2d(data, k=9)
smoothed_rot = np.rot90(smoothed, 2)
fliped = np.fliplr(smoothed_rot)

H, W = fliped.shape

hot_threshold = 314.0
hot_mask = fliped >= hot_threshold

# === 1) Carte des températures (PNG) ===
plt.figure(figsize=(8, 6), dpi=200)
im = plt.imshow(fliped, cmap="inferno", origin="lower", extent=(0, W, 0, H))
cbar = plt.colorbar(im, label="Température (K)")
plt.title(f"Carte de température (moyenne locale)")
plt.axis("off")
plt.tight_layout()
plt.savefig(out_tempmap_png, dpi=200)
plt.show()
print(f"Carte des températures sauvegardée: {out_tempmap_png.resolve()}")

# === 2) Superposition contours + image de fond (PNG) ===
sat_img = Image.open(plainpalais_path).convert("RGB")
sat_img = ImageOps.flip(sat_img)  # flip vertical pour aligner
sat_arr = np.array(sat_img)

plt.figure(figsize=(8, 6), dpi=200)
plt.imshow(sat_arr, extent=(0, W, 0, H), origin="lower")
plt.contour(
    hot_mask.astype(int),
    levels=[1],
    colors="cyan",
    linewidths=1.5,
    origin="lower",
    extent=(0, W, 0, H)
)
plt.title(f"Zones chaudes superposées (T ≥ {hot_threshold:.1f} K)")
plt.axis("off")
plt.tight_layout()
plt.savefig(out_overlay_png, dpi=200)
plt.show()
print(f"Superposition sauvegardée: {out_overlay_png.resolve()}")

"""

# --- charge données ---
data1 = np.loadtxt(path, delimiter=",")

# Redimensionner la matrice à la taille de l'image
data_img = Image.fromarray(data1)
data_resized = np.array(data_img.resize((width, height), resample=Image.NEAREST))

# Filtre moyenneur sur la matrice redimensionnée
smoothed = mean_filter_2d(data_resized, k=21)
smoothed_rot = np.rot90(smoothed, 2)
fliped = np.fliplr(smoothed_rot)

H, W = fliped.shape
hot_threshold = 369.0
hot_mask = fliped >= hot_threshold

# === 1) Carte des températures ===
plt.figure(figsize=(8, 6), dpi=200)
im = plt.imshow(fliped, cmap="inferno", origin="lower")
cbar = plt.colorbar(im, label="Température (K)")
plt.title("Carte de température (moyenne locale)")
plt.axis("off")
plt.tight_layout()
plt.savefig(out_tempmap_png, dpi=200)
plt.show()

# === 2) Superposition ===
sat_img = Image.open(sat_path_2).convert("RGB")
sat_img = ImageOps.flip(sat_img)  # flip vertical pour aligner
sat_arr = np.array(sat_img)

plt.figure(figsize=(8, 6), dpi=200)
plt.imshow(sat_arr, origin="lower")  # pas besoin d'extent si tailles identiques
plt.contour(
    hot_mask.astype(int),
    levels=[1],
    colors="cyan",
    linewidths=1.5,
    origin="lower"
)
plt.title(f"Zones chaudes superposées (T ≥ {hot_threshold:.1f} K)")
plt.axis("off")
plt.tight_layout()
plt.savefig(out_overlay_png, dpi=200)
plt.show()"""
