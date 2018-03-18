from io import BytesIO

from PIL import Image


def convert_images(images: list) -> list:
    lst = []
    for i in range(len(images)):
        try:
            lst.append(Image.open(BytesIO(images[i])).convert("RGBA"))
        except OSError:
            print("Invalid image!!!")
    return lst
