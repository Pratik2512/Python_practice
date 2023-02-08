import unittest
from testing_module import city_info


class MyTestCase(unittest.TestCase):
    """Tests for 'city_info'"""

    def test_city_country_name(self):
        neat_name = city_info('mumbai', 'india')
        self.assertEqual(neat_name, 'Mumbai, India')

    def test_city_country_population_name(self):
        neat_name = city_info('santiago', 'chile', 5000000)
        self.assertEqual(neat_name, 'Santiago, Chile, Population:5000000')


if __name__ == '__main__':
    unittest.main()

