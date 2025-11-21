import numpy as np
# Table simplifiée d'émissivité
emissivity_table = {
    "vegetation": 0.98,
    "water": 0.96,
    "concrete": 0.92,
    "asphalt": 0.93,
    "metal": 0.60
}
def classify_pixel(rgb):
    r,g,b = rgb
    if g>b and g>r:
        return "vegetation"
    elif b>r and b>g:
        return "water"
    elif abs(r-g) < 20 and abs(g-b)<20:
        return "concrete"
    else:
        return "asphalt"