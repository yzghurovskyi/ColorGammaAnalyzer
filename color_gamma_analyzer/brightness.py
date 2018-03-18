from PIL import Image


def calculate_brightness(image: Image) -> float:
    grey_scale_image = image.convert('L')
    histogram = grey_scale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)
    for index in range(scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)
    return 1 if brightness == 255 else brightness / scale


def get_images_brightness(images: list) -> list:
    return [calculate_brightness(images[i]) for i in range(len(images))]
