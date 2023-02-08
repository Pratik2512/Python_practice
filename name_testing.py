import unittest
from testing_module import get_formatted_name


class MyTestCase(unittest.TestCase):
    """Tests for 'get_formatted_name' """

    def test_first_last_name(self):
        formatted_name = get_formatted_name('alex', 'hales')
        self.assertEqual(formatted_name, 'Alex Hales')

    def test_first_middle_last_year(self):
        formatted_name = get_formatted_name('vamika', 'kolhi', 'virat')
        self.assertEqual(formatted_name, 'Vamika Virat Kolhi')


if __name__ == '__main__':
    unittest.main()
