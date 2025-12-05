from scipy.ndimage import gaussian_filter
from matplotlib.colors import ListedColormap
from pixel import * 
import numpy as np
import matplotlib.pyplot as plt

projroot1 = Path(sys.path[0]).parent
pixelated_image = np.kron(small_image, np.ones((h_step, w_step, 1)))
#temp_path = projroot / "data" / "temperature_matrixe.csv"
data = np.loadtxt("temperature_matrixe.csv", delimiter=",")

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