import unittest
import sys
import io  # python 3+ only
import puzzles

class Problem2Test(unittest.TestCase):

    def test_contains_phrase(self):
        sentence = "Hello, Bob. My name is Bob."
        self.assertTrue(puzzles.contains_phrase(sentence, "name"))
        self.assertTrue(puzzles.contains_phrase(sentence, "Bob"))
        self.assertFalse(puzzles.contains_phrase(sentence, "bob"))

    def test_contains_phrases(self):
        sentence = "Hello, Bob. My name is Bob."
        self.assertListEqual([True, True, True], puzzles.contains_phrases(sentence, ["He", "ll", "o"]))
        self.assertListEqual([False, True], puzzles.contains_phrases("Hello, world!", ["hello", ", wor"]))
        self.assertListEqual([False, False], puzzles.contains_phrases("Hello, world!", ["ellO, ", "word!!"]))

    def test_is_single_char(self):
        self.assertTrue(puzzles.is_single_char(" "))
        self.assertTrue(puzzles.is_single_char("a"))
        self.assertFalse(puzzles.is_single_char("abc"))
        self.assertFalse(puzzles.is_single_char(""))

    def test_count_characters(self):
        self.assertEqual(3, puzzles.count_characters("abcabcabc", "a"))
        self.assertEqual(0, puzzles.count_characters("abc123", "z"))
        self.assertEqual(1, puzzles.count_characters("Abcabc", "A"))

    def test_count_characters_ignore_case(self):
        self.assertEqual(3, puzzles.count_characters_ignore_case("abcAbcabc", "a"))
        self.assertEqual(0, puzzles.count_characters_ignore_case("abc123", "z"))
        self.assertEqual(2, puzzles.count_characters_ignore_case("Abcabc", "A"))

    def test_find_char_index(self):
        self.assertEqual(0, puzzles.find_char_index("Hello, world", "H"))
        self.assertEqual(4, puzzles.find_char_index("Hello, world", "o"))
        self.assertEqual(11, puzzles.find_char_index("Hello, world", "d"))
        self.assertEqual(6, puzzles.find_char_index("Hello, world", " "))
        self.assertEqual(-1, puzzles.find_char_index("Hello, world", "?"))
        self.assertEqual(-1, puzzles.find_char_index("Hello, world", "abc123"))
        self.assertEqual(-1, puzzles.find_char_index("Hello, world", "Hello, world"))

    def test_tokenize_by_spaces(self):
        self.assertListEqual(["Hello", "world"], puzzles.tokenize_by_spaces("Hello world"))
        self.assertListEqual(["a", "b", "c", "d", "e", "f", "g"], puzzles.tokenize_by_spaces("a b c d e f g"))
        self.assertListEqual([], puzzles.tokenize_by_spaces(""))

    def test_is_palindrome(self):
        self.assertTrue(puzzles.is_palindrome("racecar"))
        self.assertTrue(puzzles.is_palindrome("tacocat"))
        self.assertTrue(puzzles.is_palindrome("123454321"))
        self.assertFalse(puzzles.is_palindrome("abc123"))
        self.assertFalse(puzzles.is_palindrome("Rracecarr"))

    def test_concatenate(self):
        self.assertEqual("abcdefg", puzzles.concatenate(["a", "b", "c", "d", "e", "f", "g"]))
        self.assertEqual("Hello, world!", puzzles.concatenate(["Hello", ",", " ", "world", "!"]))

    def test_echo(self):
        out = io.StringIO()
        sys.stdout = out
        sentence = "Hello, world!"
        result = puzzles.echo(sentence)
        sys.stdout = sys.__stdout__
        self.assertIsNone(result)
        self.assertEqual(sentence, out.getvalue().strip())

    def test_print_letter_count(self):
        out = io.StringIO()
        sys.stdout = out
        expected = '"Hello, world!" contains "l" 3 times'
        result = puzzles.print_letter_count("Hello, world!", "l")
        sys.stdout = sys.__stdout__
        self.assertIsNone(result)
        self.assertEqual(expected, out.getvalue().strip())

    def test_replace(self):
        self.assertEqual("Goodbye, world!", puzzles.replace("Hello, world!", "Hello", "Goodbye"))
        self.assertEqual("12346", puzzles.replace("12345", "5", "6"))
        self.assertEqual("Hello, world!", puzzles.replace("Hello, world!", "hello", "Goodbye"))

if __name__ == '__main__':
    unittest.main()
