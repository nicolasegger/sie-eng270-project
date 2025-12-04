"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Charger le CSV
data = pd.read_csv("temperature_matrix.csv", header=None)

# Convertir en matrice NumPy
temperature_matrix = data.values

# Créer la heatmap
plt.figure(figsize=(8, 6))
plt.imshow(temperature_matrix, cmap='inferno', origin='upper')
plt.colorbar(label="Température (K)")
plt.title("Carte des températures")
plt.xlabel("Colonnes")
plt.ylabel("Lignes")

# Afficher le plot
plt.show()
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("temperature_matrix.csv", delimiter=",")

plt.imshow(data, cmap="inferno", origin="lower")
plt.colorbar(label="Température (K)")
plt.title("Carte de température")
plt.show()


