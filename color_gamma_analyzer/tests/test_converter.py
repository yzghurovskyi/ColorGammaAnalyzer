import base64
import unittest

from color_gamma_analyzer.converter import convert_images


class TestBrightnessMethods(unittest.TestCase):
    def setUp(self):
        self.images = []
        with open("./resources/images/white.png", "rb") as imageFile:
            self.images.append(imageFile.read())
        with open("./resources/images/black.png", "rb") as imageFile:
            self.images.append(imageFile.read())
        # load invalid image to arr
        with open("./resources/images/scrum_logo.jpg", "rb") as imageFile:
            self.images.append(base64.b64encode(imageFile.read()))

    def test_convert_images(self):
        self.assertEqual(len(convert_images(self.images)), 2)


if __name__ == '__main__':
    unittest.main()
