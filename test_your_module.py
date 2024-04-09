import unittest
from unittest.mock import patch, MagicMock
from main import Fibonacci, fib

class TestFibonacci(unittest.TestCase):
    def test_Fibonacci_input(self):
        user_input = '5'
        with patch('builtins.input', return_value=user_input):
            result = Fibonacci(int(user_input))
        self.assertEqual(result, 5)

    def test_Fibonacci_recursive(self):
        with patch('__main__.Fibonacci', MagicMock(side_effect=[1, 1, 2, 3, 5])):
            self.assertEqual(Fibonacci(5), 5)

    def test_Fibonacci_large(self):
        expected_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  # Oczekiwane wartości dla 10 elementów
        with patch('__main__.fib', [1, 1]):
            for i in range(2, 10):
                self.assertEqual(Fibonacci(i), expected_values[i - 1])

    def test_Fibonacci_with_negative_input(self):
        with self.assertRaises(ValueError):
            Fibonacci(-1)

if __name__ == '__main__':
    unittest.main()
