import unittest
from testing_module import Employee


class MyTestCase(unittest.TestCase):
    """Tests for class Employee"""

    def setUp(self):
        """Create a set of attributes for use in all methods."""
        self.employee = Employee('jason', 'roy', 50000)

    def test_give_default_raise(self):
        """Test default raise."""
        self.employee.give_raise()
        self.assertEqual(55000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        """Test custom raise."""
        self.employee.give_raise(10000)
        self.assertEqual(60000, self.employee.annual_salary)


if __name__ == '__main__':
    unittest.main()
