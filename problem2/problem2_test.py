import unittest

import learn_strings


class Problem2Test(unittest.TestCase):
    def test_concatenate(self):
        # each tuple is (a, b, expected)
        cases = [
            ("abc", "123", "abc123"),
            ("abc", "", "abc"),
            ("", "abc", "abc"),
        ]

        for a, b, expected in cases:
            self.assertEqual(expected, learn_strings.concatenate(a, b))

    def test_to_lowercase(self):
        # each tuple is (s, expected)
        cases = [
            ("WOW 123 wow", "wow 123 wow"),
            ("HELLO", "hello"),
            ("already lower", "already lower"),
            ("", ""),
        ]

        for s, expected in cases:
            self.assertEqual(expected, learn_strings.to_lowercase(s))

    def test_to_uppercase(self):
        # each tuple is (s, expected)
        cases = [
            ("WOW 123 wow", "WOW 123 WOW"),
            ("hello", "HELLO"),
            ("ALREADY UPPER", "ALREADY UPPER"),
            ("", ""),
        ]

        for s, expected in cases:
            self.assertEqual(expected, learn_strings.to_uppercase(s))

    def test_capitalize_string(self):
        # each tuple is (s, expected)
        cases = [
            ("hello world", "Hello world"),
            ("hello", "Hello"),
            ("Hello world", "Hello world"),
            ("", ""),
        ]

        for s, expected in cases:
            self.assertEqual(expected, learn_strings.capitalize_string(s))

    def test_contains_letter(self):
        # each tuple is (word, letter, expected)
        cases = [
            ("hello", "h", True),
            ("hello", "z", False),
            ("hello", "", True),
            ("", "a", False),
            ("", "", True),
        ]

        for word, letter, expected in cases:
            self.assertEqual(expected, learn_strings.contains_letter(word, letter))

    def test_case_insensitive_match(self):
        # each tuple is (a, b, expected)
        cases = [
            ("hello", "hello", True),
            ("hello", "HELLO", True),
            ("Hello", "hELLO", True),
            ("", "hello", False),
            ("", "", True),
            ("hello", "world", False),
        ]

        for a, b, expected in cases:
            self.assertEqual(expected, learn_strings.case_insensitive_match(a, b))

    def test_string_length(self):
        # each tuple is (s, expected)
        cases = [
            ("hello", 5),
            ("", 0),
            ("a", 1),
            ("hello world", 11),
        ]

        for s, expected in cases:
            self.assertEqual(expected, learn_strings.string_length(s))

    def test_first_letter(self):
        # each tuple is (s, expected)
        cases = [
            ("hello", "h"),
            ("a", "a"),
            ("", ""),
        ]

        for s, expected in cases:
            self.assertEqual(expected, learn_strings.first_letter(s))

    def test_last_letter(self):
        # each tuple is (s, expected)
        cases = [
            ("hello", "o"),
            ("a", "a"),
            ("", ""),
        ]

        for s, expected in cases:
            self.assertEqual(expected, learn_strings.last_letter(s))

    def test_substring(self):
        # each tuple is (s, start, end, expected)
        cases = [
            ("hello world", 0, 5, "hello"),
            ("hello world", 6, 11, "world"),
            ("hello", 1, 1, ""),
            ("hello", 0, 100, "hello"),
        ]

        for s, start, end, expected in cases:
            self.assertEqual(expected, learn_strings.substring(s, start, end))

    def test_number_to_string(self):
        # each tuple is (n, expected)
        cases = [
            (25, "25"),
            (0, "0"),
            (-5, "-5"),
        ]

        for n, expected in cases:
            self.assertEqual(expected, learn_strings.number_to_string(n))

    def test_string_to_number(self):
        # each tuple is (s, expected)
        cases = [
            ("25", 25),
            ("0", 0),
            ("-5", -5),
        ]

        for s, expected in cases:
            self.assertEqual(expected, learn_strings.string_to_number(s))


if __name__ == '__main__':
    unittest.main()
