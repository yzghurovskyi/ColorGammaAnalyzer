from PIL import Image


def calculate_brightness(image: Image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)
    for index in range(scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)
    return 1 if brightness == 255 else brightness / scale


def get_images_brightness(images: list):
    images_brightness = []
    for index in range(len(images)):
        images_brightness.append(calculate_brightness(images[index]))
    return images_brightness
