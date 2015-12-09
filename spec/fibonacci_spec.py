import unittest
from src.fibonacci import fibonacci


# Here's our "unit tests".
class fibonacci_tests(unittest.TestCase):

    def test01(self):
        self.failIf(fibonacci(1) != 1)

    def test02(self):
        self.failIf(fibonacci(6) != 8)


