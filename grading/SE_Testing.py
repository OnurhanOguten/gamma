import unittest

def divisible_by_3_or_5(n):
    return n % 3 == 0 or n % 5 == 0


class TestDivisibleBy3Or5(unittest.TestCase):

    def test_divisible_by_3(self):
        self.assertTrue(divisible_by_3_or_5(9))

    def test_divisible_by_5(self):
        self.assertTrue(divisible_by_3_or_5(10))

    def test_divisible_by_3_and_5(self):
        self.assertTrue(divisible_by_3_or_5(15))

    def test_not_divisible(self):
        self.assertFalse(divisible_by_3_or_5(7))

    def test_zero(self):
        self.assertTrue(divisible_by_3_or_5(0))


if __name__ == "__main__":
    unittest.main()