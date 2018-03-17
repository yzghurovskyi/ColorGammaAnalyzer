from PIL import Image


def convert_base64_to_image(base64_string: str):
    return Image.open(base64_string)
