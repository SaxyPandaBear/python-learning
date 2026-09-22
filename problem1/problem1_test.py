import unittest

from problem1 import numbers


class Problem1Test(unittest.TestCase):
    def test_add(self):
        xs = [1, 3, 5, 4, 10, 5]
        ys = [1, 2, 3, 4, 0, -10]
        answers = [2, 5, 8, 8, 10, -5]

        self.assertListEqual(answers, [numbers.add(x, y) for x, y in zip(xs, ys)])

    def test_multiply(self):
        xs = [0, 1, 5, 20, 3]
        ys = [100, 5, 0, 2, -2]
        answers = [0, 5, 0, 40, -6]

        self.assertListEqual(answers, [numbers.multiply(x, y) for x, y in zip(xs, ys)])

    def test_remainder(self):
        nums = [1, 3, 4, 100, 101]
        divs = [1, 2, 2, 37, 19]
        answers = [0, 1, 0, 26, 6]
        self.assertListEqual(answers, [numbers.remainder(x, y) for x, y in zip(nums, divs)])

    def test_add_all(self):
        xs = [1,2,3,4,5]
        empty = []
        single = [600]
        ys = [2, 50, 1, -53]

        self.assertEqual(15, numbers.add_all(xs))
        self.assertEqual(0, numbers.add_all(empty))
        self.assertEqual(600, numbers.add_all(single))
        self.assertEqual(0, numbers.add_all(ys))

    def test_subtract_from(self):
        x, xs = 10, [1, 3, 5]
        y, ys = 5, [1, 2, 3]
        z, zs = 100, []
        w, ws = 0, [-1, -2, -3, -4, -5]

        self.assertEqual(1, numbers.subtract_from(x, xs))
        self.assertEqual(-1, numbers.subtract_from(y, ys))
        self.assertEqual(100, numbers.subtract_from(z, zs))
        self.assertEqual(15, numbers.subtract_from(w, ws))

    def test_is_odd(self):
        self.assertTrue(numbers.is_odd(5))
        self.assertFalse(numbers.is_odd(10))

    def test_is_even(self):
        self.assertFalse(numbers.is_even(5))
        self.assertTrue(numbers.is_even(10))


if __name__ == '__main__':
    unittest.main()
