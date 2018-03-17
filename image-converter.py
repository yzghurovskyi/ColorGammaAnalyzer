from PIL import Image


def convert_base64_to_image(base64_string):
    return Image.open(base64_string)