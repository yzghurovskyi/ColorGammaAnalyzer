from color_gamma_analyzer.brightness import get_images_brightness
from color_gamma_analyzer.diapason import calculate_ranges
from color_gamma_analyzer.converter import convert_images
from color_gamma_analyzer.img_loader import get_images_from_links
from color_gamma_analyzer.xml_util \
    import parse_urls_from_xml, write_ranges_to_xml


def brightness_processing(
        intervals_count: int,
        inner_xml_file: str,
        outer_xml_file: str):
    urls = parse_urls_from_xml(inner_xml_file)
    images = get_images_from_links(urls)
    images = convert_images(images)
    brightness_values = get_images_brightness(images)
    diapasons = calculate_ranges(brightness_values, intervals_count)
    write_ranges_to_xml(outer_xml_file, diapasons)
