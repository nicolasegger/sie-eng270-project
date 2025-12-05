from PIL import Image

image = Image.open("epfl_sat.jpg")

pixel_size = 16

small = image.resize(
    (image.width // pixel_size, image.height // pixel_size),
    resample= Image.NEAREST
)


pixelated = small.resize(image.size, Image.NEAREST)

pixelated.show()

pixelated.save("epfl_sat_pix.jpg")

#