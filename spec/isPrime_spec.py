import unittest
from src.isPrime import isPrime


# Here's our "unit tests".
class isPrime_tests(unittest.TestCase):

    def test01(self):
        self.failUnless(isPrime(17))

    def test02(self):
        self.failIf(isPrime(24))

    def test03(self):
        self.failIf(isPrime(15))


