import numbers
import unittest


class Problem1Test(unittest.TestCase):
    def test_add(self):
        # each tuple is (x, y, expected)
        cases = [
            (1, 1, 2),
            (3, 2, 5),
            (5, 3, 8),
            (4, 4, 8),
            (10, 0, 10),
            (5, -10, -5),
        ]

        for x, y, expected in cases:
            self.assertEqual(expected, numbers.add(x, y))

    def test_multiply(self):
        # each tuple is (x, y, expected)
        cases = [
            (0, 100, 0),
            (1, 5, 5),
            (5, 0, 0),
            (20, 2, 40),
            (3, -2, -6),
            (-3, -2, 6),
            (7, 1, 7),
        ]

        for x, y, expected in cases:
            self.assertEqual(expected, numbers.multiply(x, y))

    def test_remainder(self):
        # each tuple is (numerator, divisor, expected)
        cases = [
            (1, 1, 0),
            (3, 2, 1),
            (4, 2, 0),
            (100, 37, 26),
            (101, 19, 6),
            (0, 5, 0),
            (3, 100, 3),
        ]

        for numerator, divisor, expected in cases:
            self.assertEqual(expected, numbers.remainder(numerator, divisor))

    def test_is_odd(self):
        # each tuple is (num, expected)
        cases = [
            (5, True),
            (10, False),
            (0, False),
            (-3, True),
        ]

        for num, expected in cases:
            self.assertEqual(expected, numbers.is_odd(num))

    def test_is_even(self):
        # each tuple is (num, expected)
        cases = [
            (5, False),
            (10, True),
            (0, True),
            (-4, True),
        ]

        for num, expected in cases:
            self.assertEqual(expected, numbers.is_even(num))


if __name__ == "__main__":
    unittest.main()
