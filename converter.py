from io import BytesIO
from PIL import Image


def convert_images(images: list):
    lst = []
    for i in range(len(images)):
        lst.append(Image.open(BytesIO(images[i])).convert("RGBA"))
    return lst


