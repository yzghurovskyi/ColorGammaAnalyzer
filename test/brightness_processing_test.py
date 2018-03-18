import unittest
from lxml import objectify
from brightness_processing import brightness_processing


class TestBrightnessProcessingMethod(unittest.TestCase):
    def test_brightness_processing(self):
        brightness_processing(2, "./resources/data_files/input_brightness_processing_test.xml",
                              "./resources/data_files/output_brightness_processing_test.xml")
        file = open("./resources/data_files/output_brightness_processing_test.xml")
        string_data = file.read()
        file.close()
        root = objectify.fromstring(string_data)
        self.assertEqual(int(root.attrib['all_images']), 1)
        self.assertEqual(float(root.getchildren()[0].attrib['start']), 0)
        self.assertEqual(float(root.getchildren()[0].attrib['end']), 0.5)
        self.assertEqual(int(root.getchildren()[0].getchildren()[0].text), 0)
        self.assertEqual(float(root.getchildren()[1].attrib['start']), 0.5)
        self.assertEqual(float(root.getchildren()[1].attrib['end']), 1)
        self.assertEqual(int(root.getchildren()[1].getchildren()[0].text), 1)

    def test_exception_from_brightness_processing(self):
        brightness_processing(2, "./resources/data_files/input_brightness_processing_test.xml",
                              "./resources/data_files/output_brightness_processing_test.xml")
        self.assertRaises(ValueError, brightness_processing, -1,
                          "./resources/data_files/input_brightness_processing_test.xml",
                          "./resources/data_files/output_brightness_processing_test.xml")
        self.assertRaises(ValueError, brightness_processing, 0,
                          "./resources/data_files/input_brightness_processing_test.xml",
                          "./resources/data_files/output_brightness_processing_test.xml")


if __name__ == '__main__':
    unittest.main()