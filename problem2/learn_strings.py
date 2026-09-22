"""
Module that goes over common string operations
"""

def concatenate(a: str, b: str) -> str:
    """
    Given two strings, *concatenate* them, meaning combine them together
    to form a single string.

    For example, a concatenation of "foo" and "bar" would be "foobar",
    because order matters.

    Example: concatenate("bar", "foo") should return "barfoo"
    :param a A string
    :param b Another number
    :return the concatenation of a and b
    """
    pass

def to_lowercase(s: str) -> str:
    """
    Regardless of the existing capitalization scheme, take a string and
    transform it so that all letters are lowercase.

    Hint: There might be a simple helper that already exists for this

    Example: to_lowercase("WOW 123 wow") should return "wow 123 wow"
    :param s a string
    :return the string with all relevant letters transformed to lowercase
    """
    pass

def to_uppercase(s: str) -> str:
    """
    Like the to_lowercase function, do the opposite. Take a string and
    transform it so that all letters are uppercase.

    Example: to_uppercase("WOW 123 wow") should return "WOW 123 WOW"
    :param s a string
    :return the string with all relevant letters transformed to uppercase
    """
    pass

def capitalize_string(s: str) -> str:
    """
    Take a string and capitalize it, meaning change the first letter to uppercase.
    Note that if there's more than one word in the string, it still only capitalizes
    the first word.

    Example: capitalize_string("hello world") should return "Hello world"
    :param s a string to capitalize
    :return the string capitalized
    """
    pass

def contains_letter(word: str, letter: str) -> bool:
    """
    Determine if a given word contains a specific letter. If the letter is
    empty, the response should always be True, even if the word is also
    empty. Otherwise, if the word is empty, the response should always be
    False.

    Example: contains_letter("foo", "f") should return True
    Example: contains_letter("", "") should return True
    Example: contains_letter("", "a") should return False
    :param word a word
    :param letter a letter to verify is in the word
    :return True if the letter is found in the word, False otherwise.
    """
    pass

def case_insensitive_match(a: str, b: str) -> bool:
    """
    Given two strings, return True if the strings match, ignoring case. Return False
    otherwise.

    Example: case_insensitive_match("Hello", "hELLO") should return True
    :param a a string
    :param b another string
    :return True if the strings match, ignoring case, False otherwise
    """
    pass

def string_length(s: str) -> int:
    """
    Given a string, return how many characters are in it.

    Example: string_length("hello") should return 5
    Example: string_length("") should return 0
    :param s a string
    :return the number of characters in s
    """
    pass

def first_letter(s: str) -> str:
    """
    Given a string, return its first character. If the string is empty,
    return an empty string.

    Hint: strings can be indexed like a list, using square brackets and a
    position, starting at 0 for the first character.

    Example: first_letter("hello") should return "h"
    Example: first_letter("") should return ""
    :param s a string
    :return the first character of s, or "" if s is empty
    """
    pass

def last_letter(s: str) -> str:
    """
    Given a string, return its last character. If the string is empty,
    return an empty string.

    Hint: Python allows negative indexes, which count backwards from the
    end of a sequence, starting at -1 for the last character.

    Example: last_letter("hello") should return "o"
    Example: last_letter("") should return ""
    :param s a string
    :return the last character of s, or "" if s is empty
    """
    pass

def substring(s: str, start: int, end: int) -> str:
    """
    Given a string and a start/end position, return the portion of the
    string starting at the start position, up to (but not including) the
    end position.

    Example: substring("hello world", 0, 5) should return "hello"
    Example: substring("hello world", 6, 11) should return "world"
    :param s a string
    :param start the index to start the substring at (inclusive)
    :param end the index to end the substring at (exclusive)
    :return the substring of s from start to end
    """
    pass

def number_to_string(n: int) -> str:
    """
    Given a number, convert it to its string representation.

    This is useful when you want to combine a number with other text -
    concatenating a string and a number directly with + isn't allowed in
    Python, since both sides of + need to be the same type.

    Example: number_to_string(25) should return "25"
    :param n a number
    :return the string representation of n
    """
    pass

def string_to_number(s: str) -> int:
    """
    Given a string that represents a whole number, convert it to an int.

    You can assume the string given will always be a valid whole number.

    Example: string_to_number("25") should return 25
    :param s a string containing a whole number
    :return the integer value represented by s
    """
    pass
