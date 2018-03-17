from lxml import etree


def parse_urls_from_xml(xml_file: str):
    context = etree.iterparse(xml_file)
    urls = []
    for action, elem in context:
        if elem.tag == "url":
            urls.append(elem.text)
    return urls


def write_ranges_to_xml(xml_file: str, ranges: tuple):
    root = etree.Element('ranges')
    for i in range(len(ranges)):
        child_range = etree.SubElement(root, 'range')
        start, end, count = ranges[i]

        start_child = etree.SubElement(child_range, 'from')
        start_child.text = str(start)

        end_child = etree.SubElement(child_range, 'to')
        end_child.text = str(end)

        count_child = etree.SubElement(child_range, 'count')
        count_child.text = str(count)

    tree = etree.ElementTree(root)
    tree.write(xml_file, pretty_print=True)
