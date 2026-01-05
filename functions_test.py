import unittest
from Functions import *


class MyTestCase(unittest.TestCase):


    def test_something(self):
        self.assertTrue(is_even(44))

    def test_that_get_maximum_returns_the_maximum_number_in_a_list(self):
        result = get_maximum([12, 34, 90, 12])
        self.assertEqual(result, 90)



if __name__ == '__main__':
    unittest.main()
