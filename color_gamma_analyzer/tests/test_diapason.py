import unittest
from color_gamma_analyzer.diapason import calculate_ranges


class TestCalculatingOfRanges(unittest.TestCase):
    def setUp(self):
        self.brightness_data = [0.56, 0.76, 0.12, 0.97, 0.121, 0.454, 0.656]

    def test_calculating_diapason_ranges(self):
        calculated_ranges_first = [
            (0, 0.33, 2),
            (0.33, 0.67, 3),
            (0.67, 1.0, 2)
        ]
        self.assertEqual(
            calculated_ranges_first,
            calculate_ranges(self.brightness_data, 3)
        )

        calculated_ranges_second = [(0, 0.5, 3), (0.5, 1.0, 4)]
        self.assertEqual(
            calculated_ranges_second,
            calculate_ranges(self.brightness_data, 2)
        )

        calculated_ranges_third = [
            (0, 0.1, 0),
            (0.1, 0.2, 2),
            (0.2, 0.3, 0),
            (0.3, 0.4, 0),
            (0.4, 0.5, 1),
            (0.5, 0.6, 1),
            (0.6, 0.7, 1),
            (0.7, 0.8, 1),
            (0.8, 0.9, 0),
            (0.9, 1.0, 1)
        ]
        self.assertEqual(
            calculated_ranges_third,
            calculate_ranges(self.brightness_data, 10)
        )
        self.assertRaises(
            ValueError,
            calculate_ranges,
            self.brightness_data, -12
        )
        self.assertRaises(
            ValueError,
            calculate_ranges,
            self.brightness_data, 0
        )


if __name__ == '__main__':
    unittest.main()
