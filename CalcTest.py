import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5
    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(7, 3)
        self.assertEqual(result, 4)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(7, 3)
        self.assertEqual(result, 21)

    def test_divide_returns_float_for_non_integer_result(self):
        calc = Calculator()
        result = calc.divide(7, 2)
        self.assertEqual(result, 3.5)

    def test_divide_by_zero_raises_value_error(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(7, 0)

    def test_modulo(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(7, 3), 1)
        self.assertEqual(calc.modulo(-7, 3), 2)
        self.assertEqual(calc.modulo(7, -3), -2)
        with self.assertRaises(ValueError):
            calc.modulo(7, 0)

    def test_power(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(0, 0), 1)
        self.assertEqual(calc.power(2, -1), 0.5)

if __name__ == "__main__":
    unittest.main()