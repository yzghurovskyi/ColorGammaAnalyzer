import unittest

from PIL import Image

from brightness import calculate_brightness


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.images = []
        self.images.append(Image.open("./resources/images/white.png"))

    def test_calculate_brightness(self):
        self.assertEqual(calculate_brightness(self.images[0]), 1, "The value obtained are not correct !!!")


if __name__ == '__main__':
    unittest.main()