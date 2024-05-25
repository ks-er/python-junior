import unittest

from common import (
    factorial,
    MyException,
)

from implementation import (
    cache_value,
)

class MyTestCase(unittest.TestCase):
    def test_on_correct_values5(self):
        new_factorial = cache_value(factorial)
        self.assertEqual(new_factorial(5), 120)

    def test_on_str_value(self):
        new_factorial = cache_value(factorial)
        self.assertRaises(MyException, new_factorial, '1')

    def test_on_none_value(self):
        new_factorial = cache_value(factorial)
        self.assertRaises(MyException, new_factorial, None)

    def test_on_float_value(self):
        new_factorial = cache_value(factorial)
        self.assertRaises(MyException, new_factorial, 7.5)

    def test_on_negative_value(self):
        new_factorial = cache_value(factorial)
        self.assertRaises(MyException, new_factorial, -1)

    def test_on_zero_value(self):
        new_factorial = cache_value(factorial)
        self.assertEqual(new_factorial(0), 1)

    def test_on_correct_values5_dbl(self):
        new_factorial = cache_value(factorial)
        self.assertEqual(new_factorial(5), 120)

    def test_on_correct_values7(self):
        new_factorial = cache_value(factorial)
        self.assertEqual(new_factorial(7), 5040)

    def test_on_correct_values7_dbl(self):
        new_factorial = cache_value(factorial)
        self.assertEqual(new_factorial(7), 5040)

if __name__ == '__main__':
    unittest.main()
