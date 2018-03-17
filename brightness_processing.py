from brightness import get_images_brightness
from diapason import calculate_ranges
from converter import convert_images
from img_loader import get_images_from_links
from xml_util import parse_urls_from_xml, write_ranges_to_xml


def brightness_processing(inner_xml_file: str, outer_xml_file: str):
    urls = parse_urls_from_xml(inner_xml_file)
    images = get_images_from_links(urls)
    images = convert_images(images)
    brightness_values = get_images_brightness(images)
    diapasons = calculate_ranges(brightness_values, 10)
    write_ranges_to_xml(outer_xml_file, diapasons)


brightness_processing("data/in.xml", "data/.out.xml")
