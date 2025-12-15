from scipy.ndimage import gaussian_filter
from matplotlib.colors import ListedColormap
from pixel import * 
import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

projroot = Path(sys.path[0]).parent
path = projroot / "data" / "temperature_matrixe.csv"
pixelated_image = np.kron(small_image, np.ones((h_step, w_step, 1)))
#temp_path = projroot / "data" / "temperature_matrixe.csv"
data = np.loadtxt(path, delimiter=",")

def mean_filter_2d(arr, k=5):
  
    if k % 2 == 0:
        raise ValueError("k doit être impair")
    pad = k // 2

    arr_p = np.pad(arr, pad_width=pad, mode='edge')

    kernel = np.ones((k, k), dtype=float) / (k * k)

    cumsum_h = np.cumsum(arr_p, axis=1)

    h = cumsum_h[:, k:] - cumsum_h[:, :-k]
    h = h / k

    h_p = np.pad(h, ((pad, pad), (0, 0)), mode='edge')

    cumsum_v = np.cumsum(h_p, axis=0)
    v = cumsum_v[k:, :] - cumsum_v[:-k, :]
    v = v / k

    return v

smoothed = mean_filter_2d(data, k=7)
smoothed_rot = np.rot90(smoothed,2)
fliped = np.fliplr(smoothed_rot)
plt.imshow(fliped, cmap="inferno", origin="lower")
plt.colorbar(label="Température (K)")

plt.title("Carte de température (moyenne locale k=5)")
plt.show()

# On repart de ta variable 'fliped' déjà calculée
hot_threshold = 370.0  # K

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

def save_hot_contours(fliped, hot_threshold=355.0, out_path="hot_contours.png",
                      color="cyan", linewidth=1.5, origin="lower"):
    """
    Sauvegarde un fichier image (PNG) avec uniquement les contours des zones chaudes,
    sur fond transparent.
    """
    H, W = fliped.shape
    hot_mask = fliped >= hot_threshold

    # Figure sans bord et fond transparent
    fig = plt.figure(figsize=(8, 6), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])  # plein cadre
    ax.axis("off")

    # Tracer uniquement les contours du masque
    cs = ax.contour(
        hot_mask.astype(int),
        levels=[1],
        colors=color,
        linewidths=linewidth,
        origin=origin,
        extent=(0, W, 0, H) if origin == "lower" else (0, W, H, 0),
    )

    # Sauvegarde avec transparence
    out_path = projroot / "data" / "overlay_contours.png"
    fig.savefig(out_path, transparent=True, bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    print(f"Contours enregistrés: {out_path.resolve()}")

save_hot_contours(fliped, hot_threshold=370)   