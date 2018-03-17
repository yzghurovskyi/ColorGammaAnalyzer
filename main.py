from brightness import get_images_brightness
from diapason import calculate_ranges
from image_converter import convert_images
from img_loader import get_images_from_links
from xml_util import parse_urls_from_xml, write_ranges_to_xml

if __name__ == "__main__":
    urls = parse_urls_from_xml('data/in.xml')
    images = get_images_from_links(urls)
    images = convert_images(images)
    brightness_values = get_images_brightness(images)
    diapasons = calculate_ranges(brightness_values, 10)
    write_ranges_to_xml('data/out.xml', diapasons)

