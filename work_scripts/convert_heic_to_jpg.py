from PIL import Image
import pyheif

heif_file = pyheif.read("IMG_7424.HEIC")
image = Image.frombytes(
    heif_file.mode, 
    heif_file.size, 
    heif_file.data,
    "raw",
    heif_file.mode,
    heif_file.stride,
    )
image.save("IMG_7424.jpg", "JPEG")
