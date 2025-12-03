import numpy as np
# Table simplifiée d'émissivité
emissivity_table = {
    "vegetation": 0.98,
    "water": 0.96,
    "concrete": 0.92,
    "asphalt": 0.93,
    "metal": 0.60
}
def classify_pixel_emissivite(rgb):
    r,g,b = rgb
    if g>b and g>r:
        return "vegetation"
    elif b>r and b>g:
        return "water"
    elif abs(r-g) < 20 and abs(g-b)<20:
        return "concrete"
    else:
        return "asphalt"
    

# Table simplifiée d'albedo
albedo_table = {
    "vegetation": 0.25,  # Exemple d'albédo pour la végétation
    "water": 0.05,       # Albédo pour l'eau
    "concrete": 0.30,    # Albédo pour le béton
    "asphalt": 0.15,     # Albédo pour l'asphalte
    "metal": 0.60        # Albédo pour le métal
}

def classify_pixel_albedo(rgb):
    r, g, b = rgb
    if g > b and g > r:
        return "vegetation"
    elif b > r and b > g:
        return "water"
    elif abs(r - g) < 20 and abs(g - b) < 20:
        return "concrete"
    else:
        return "asphalt"