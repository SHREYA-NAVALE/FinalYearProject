import rasterio
import numpy as np
from PIL import Image
import os

def convert_to_png(tif_path):
    with rasterio.open(tif_path) as src:

        # ✅ Use correct RGB bands (Sentinel-2)
        red = src.read(4)
        green = src.read(3)
        blue = src.read(2)

        # ✅ Normalize reflectance
        red = red / 10000
        green = green / 10000
        blue = blue / 10000

        rgb = np.stack([red, green, blue], axis=-1)

        # ✅ Normalize to 0–255
        rgb = (rgb - np.min(rgb)) / (np.max(rgb) - np.min(rgb))
        rgb = (rgb * 255).astype(np.uint8)

        # ✅ Save PNG
        png_path = tif_path.replace(".tif", ".png")
        Image.fromarray(rgb).save(png_path)

        return png_path