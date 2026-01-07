import unittest
from BackToSenderLogistics import back_to_sender


class MyTestCase(unittest.TestCase):
    def test_that_back_to_sender_returns_the_price_an_employee_receives(self):
        result = back_to_sender.get_price(80)
        self.assertEqual(45000, result)


    def test_that_back_to_sender_throws_an_error_if_CollectionRateIsNegative(self):
        self.assertRaises(ValueError, back_to_sender.get_price, -1)

    def test_that_back_to_sender_raises_an_error_if_you_pass_any_argument_that_not_of_type_int(self):
        self.assertRaises(TypeError, back_to_sender.get_price, "abc")





if __name__ == '__main__':
    unittest.main()
