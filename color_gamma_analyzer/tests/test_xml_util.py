import unittest

from color_gamma_analyzer.xml_util import parse_urls_from_xml


class TestXMLUtilParser(unittest.TestCase):
    def setUp(self):
        self.urls_first = parse_urls_from_xml(
            'resources/data_files/xml_util_test_input1.xml'
        )
        self.urls_second = parse_urls_from_xml(
            'resources/data_files/xml_util_test_input2.xml'
        )

    def test_xml_parser(self):
        self.assertEqual(len(self.urls_first), 3)
        self.assertEqual(len(self.urls_second), 0)
        self.assertRaises(
            FileNotFoundError,
            parse_urls_from_xml,
            'xml_data/bad_path.xml'
        )
        self.assertEqual(self.urls_first[0], 'http://www.biathlon.com.ua/')
        self.assertEqual(self.urls_first[1], 'https://sinoptik.ua/')
        self.assertEqual(self.urls_first[2], 'https://football.ua')


if __name__ == '__main__':
    unittest.main()
