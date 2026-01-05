import unittest
from Functions import *


class MyTestCase(unittest.TestCase):


    def test_something(self):
        self.assertTrue(is_even(44))

    def test_that_get_maximum_returns_the_maximum_number_in_a_list(self):
        result = get_maximum([12, 34, 90, 12])
        self.assertEqual(result, 90)

    def test_that_get_minimum_returns_the_minimum_in_an_array(self):
        result = get_minimum([1, 2, 3, 67, -5])
        self.assertEqual(result, -5)



if __name__ == '__main__':
    unittest.main()
