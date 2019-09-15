import unittest
import catch_me
import foo

class Problem3Test(unittest.TestCase):

    def test_some_function(self):
        expected = repr(foo.always_raise_exception())
        self.assertEqual(expected, catch_me.some_function())

    def test_valid_string_and_valid_censor(self):
        s = "qwrtypsdfghjklzxcvbnm"
        censor = "*"
        self.assertEqual(catch_me.scared_of_vowels(s, censor), valid)

    def test_invalid_censor(self):
        # doesn't matter cause an exception will be raised cause of the censor
        s = "asdjoifasnfboiahfdoa"
        censor = "a"  # invalid
        self.assertRaises(Exception, catch_me.scared_of_vowels(s, censor))

    def test_invalid_string_and_valid_censor(self):
        s = "abcdefg"
        censor = "p"

        expected = "pbcdpfg"
        self.assertEqual(expected, catch_me.scared_of_vowels(s, censor))


if __name__ == '__main__':
    unittest.main()
