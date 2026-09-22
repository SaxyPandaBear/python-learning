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
    Determine if a given word contains a specific letter. If the word is empty,
    then the response should always be False. If the letter is empty, the
    response should always be True.

    Example: contains_letter("foo", "f") should return True
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
