from lxml import etree


def parse_urls_from_xml(xml_file: str) -> list:
    context = etree.iterparse(xml_file)
    return [elem.text for action, elem in context if elem.tag == "url"]


def write_ranges_to_xml(xml_file: str, ranges: list):
    root = etree.Element('ranges')
    counts = [count for (start, end, count) in ranges]
    root.set('all_images', str(sum(counts)))
    for i in range(len(ranges)):
        start, end, count = ranges[i]
        range_child = etree.SubElement(root, 'range', start=str(start))
        range_child.set('end', str(end))

        count_child = etree.SubElement(range_child, 'images_count')
        count_child.text = str(count)

    tree = etree.ElementTree(root)
    tree.write(xml_file, pretty_print=True)
