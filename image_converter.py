from io import BytesIO

from PIL import Image


def convert_base64_to_image(image):
    return Image.open(BytesIO(image))

