import unittest

from problem2 import learn_strings


class Problem2Test(unittest.TestCase):
    def test_concatenate(self):
        s1 = "abc"
        s2 = "123"
        expected = "abc123"
        result = learn_strings.concatenate(s1, s2)

        self.assertEqual(expected, result)

    def test_concatenate_empty(self):
        s = "abc"
        result = learn_strings.concatenate(s, "")
        self.assertEqual(s, result)

        result = learn_strings.concatenate("", s)
        self.assertEqual(s, result)

    def test_to_lowercase(self):
        pass

    def test_to_uppercase(self):
        pass

    def test_capitalize_string(self):
        pass

    def test_contains_letter(self):
        # TODO: change these to use a list of tuples where each tuple
        #       is a self-contained test scenario
        xs = ["hello", "hello", "hello", "", ""]
        ys = ["h", "z", "", "a", ""]
        answers = [True, False, True, False, True]
        self.assertListEqual(answers, [learn_strings.contains_letter(x, y) for x, y in zip(xs, ys)])

    def test_case_insensitive_match(self):
        xs = ["hello", "hello", "Hello", "", "", "hello"]
        ys = ["hello", "HELLO", "hELLO", "hello", "", "world"]
        answers = [True, False, False, False, True, False]
        self.assertListEqual(answers, [learn_strings.case_insensitive_match(x, y) for x, y in zip(xs, ys)])
