import numpy as np
# Table 1
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
    
# Table 2
albedo_table = {
    "vegetation": 0.25, 
    "water": 0.05,       
    "concrete": 0.30,    
    "asphalt": 0.15,     
    "metal": 0.60        
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
