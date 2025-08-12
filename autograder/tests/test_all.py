import unittest

from gradescope_utils.autograder_utils.decorators import weight, number

from apputil import *


class TestFunction(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_factorial_basic(self):
        """
        Evaluate a few typical cases:
            2! --> 2
            3! --> 6
            4! --> 24
        """
        self.assertEqual(factorial(2), 2, "factorial(2) --> 2")
        self.assertEqual(factorial(3), 6, "factorial(3) --> 6")
        self.assertEqual(factorial(4), 24, "factorial(4) --> 24")

    @weight(1)
    @number("1.2")
    def text_factorial_edge(self):
        """
        Evaluate a couple edge cases:
            0! --> 1
            1! --> 1
        """
        self.assertEqual(factorial(0), 1, "factorial(0) --> 1")
        self.assertEqual(factorial(1), 1, "factorial(1) --> 1")

    @weight(1)
    @number("1.3")
    def test_fibonacci_basic(self):
        """
        Evaluate a few typical cases:
            
            fibonacci(2) --> 1
            fibonacci(3) --> 2
            fibonacci(4) --> 3
            fibonacci(5) --> 5
        """
        self.assertEqual(fibonacci(2), 1, "fibonacci(2) --> 1")
        self.assertEqual(fibonacci(3), 2, "fibonacci(3) --> 2")
        self.assertEqual(fibonacci(4), 3, "fibonacci(4) --> 3")
        self.assertEqual(fibonacci(5), 5, "fibonacci(5) --> 5")

    @weight(1)
    @number("1.4")
    def test_fibonacci_edge(self):
        """
        Evaluate a couple edge cases:
        
            fibonacci(0) --> 0
            fibonacci(1) --> 1
        """
        self.assertEqual(fibonacci(0), 0, "fibonacci(0) --> 0")
        self.assertEqual(fibonacci(1), 1, "fibonacci(1) --> 1")

    # @weight(2)
    # @number("3.1")
    # def test_exception(self):
    #     """Evaluating 2 ** 8 should raise an exception"""
    #     with self.assertRaises(ValueError):
    #         func("2 ** 8")

    