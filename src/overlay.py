
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image, ImageOps
import sys

# paths
projroot = Path(sys.path[0]).parent
matrix_path = projroot / "results" / "temperature_matrixe.csv"
pix_path = projroot / "data" / "image_pixel.jpg"
epfl_path = projroot / "data" / "epfl_sat.jpg"
plainpalais_path = projroot / "data" / "plainpalais.jpg"
out_tempmap_png = projroot / "results" / "tempmap.png"       # carte des températures
out_overlay_png = projroot / "results" / "overlay_contours.png"  # superposition finale
img = Image.open(pix_path)
width, height = img.size
# datas
data = np.loadtxt(matrix_path, delimiter=",")

data_img = Image.fromarray(data)
data = np.array(data_img.resize((width, height), resample=Image.NEAREST))


# mean filter
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
#threshold 85%
hot_threshold =  float(np.percentile(fliped, 85))
hot_mask = fliped >= hot_threshold

#tempmap
plt.figure(figsize=(8, 6), dpi=200)
im = plt.imshow(fliped, cmap="inferno", origin="lower", extent=(0, W, 0, H))
cbar = plt.colorbar(im, label="Temperature (K)")
plt.title(f"Temperature map (local mean)")
plt.axis("off")
plt.tight_layout()
plt.savefig(out_tempmap_png, dpi=200)
plt.show()
print(f"Carte des températures sauvegardée: {out_tempmap_png.resolve()}")

# overlay + jpg + flip
sat_img = Image.open(plainpalais_path).convert("RGB")
sat_img = ImageOps.flip(sat_img)  
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
plt.title(f"heat islands (T ≥ 85% mean temp ({hot_threshold:.1f} K) )")
plt.axis("off")
plt.tight_layout()
plt.savefig(out_overlay_png, dpi=200)
plt.show()
print(f"Superposition sauvegardée: {out_overlay_png.resolve()}")
