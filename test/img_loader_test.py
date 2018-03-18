import unittest
from img_loader import get_all_images_from_link, get_images_from_links


class TestImageLoading(unittest.TestCase):
    def setUp(self):
        self.links = []
        self.links.append('http://www.biathlon.com.ua/')
        self.links.append('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B1%D0' +
                          '%BE%D1%80%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C')
        self.links.append('https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=0' +
                          'ahUKEwjA36iwhvbZAhXkNJoKHWLyAzUQ_AUICigB&biw=1855&bih=990')
        self.links.append('https://fake.com')

    def test_images_amount_from_link(self):
        error_msg = "Not all images were received"
        self.assertEqual(len(get_all_images_from_link(self.links[0])), 1, error_msg)
        self.assertEqual(len(get_all_images_from_link(self.links[1])), 14, error_msg)
        self.assertEqual(len(get_all_images_from_link(self.links[2])), 20, error_msg)
        self.assertEqual(len(get_all_images_from_link(self.links[3])), 0, error_msg)

    def test_images_amount_from_links(self):
        error_msg = "Invalid images grouping"
        self.assertEqual(len(get_images_from_links([self.links[0], self.links[1]])), 15, error_msg)
        self.assertEqual(len(get_images_from_links([self.links[1], self.links[2]])), 34, error_msg)
        self.assertEqual(len(get_images_from_links([self.links[0], self.links[2]])), 21, error_msg)
        self.assertEqual(len(get_images_from_links([self.links[1], self.links[1]])), 28, error_msg)


if __name__ == '__main__':
    unittest.main()