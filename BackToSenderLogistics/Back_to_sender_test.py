import unittest
from BackToSenderLogistics import back_to_sender


class MyTestCase(unittest.TestCase):
    def test_that_back_to_sender_returns_the_price_an_employee_receives(self):
        result = back_to_sender.get_price(80)
        self.assertEqual(45000, result)



if __name__ == '__main__':
    unittest.main()
