import unittest
from Functions import is_even


class MyTestCase(unittest.TestCase):


    def test_something(self):
        self.assertTrue(is_even(44))


if __name__ == '__main__':
    unittest.main()
