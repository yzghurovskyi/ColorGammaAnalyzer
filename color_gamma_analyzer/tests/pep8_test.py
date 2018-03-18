import os
import unittest
import pycodestyle


class TestPep8(unittest.TestCase):
    """Run PEP8 on all project files."""
    def test_pep8(self):
        style = pycodestyle.StyleGuide()
        errors = 0
        for root, _, files in os.walk('color_gamma_analyzer'):
            python_files = [
                os.path.join(root, f)
                for f in files if f.endswith('.py')
            ]
            errors += style.check_files(python_files).total_errors
        self.assertEqual(errors, 0, 'PEP8 style errors: %d' % errors)


if __name__ == '__main__':
    unittest.main()
