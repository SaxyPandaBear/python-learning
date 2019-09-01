"""
Module that defines some string puzzles and functions
"""

"""
takes two strings, and checks to see if the phrase can be found
in the text. this phrase can be embedded within a word, or made 
of multiple words. this is case-sensitive, meaning capitalization matters.

returns True if the text contains the phrase
returns False if the text does not contain the phrase

Example: contains_phrase("Hello", "Hello") should be True
Example: contains_phrase("Hello, world!", "lo") should return True
Example: contains_phrase("Hello, world!", "o, wor") should return True
Example: contains_phrase("Hello", "hello") should return False
"""
def contains_phrase(text, phrase):
    pass

"""
takes a string and a list of strings, and returns a list of boolean (true or false)
values indicating if each phrase exists in the text string. the position of each
boolean in the list should correspond to the position of the phrase in the original list.
this is case-sensitive, meaning the capitalization needs to match the phrase exactly to count.
if the list of phrases is empty, return an empty list

Example: contains_phrases("Hello, world!", ["Hello", "world"]) should return [True, True]
Example: contains_phrases("Hello, world!", ["hello", ", wor"]) should return [False, True]
Example: contains_phrases("Hello, world!", ["ellO, ", "word!!"]) should return [False, False]
"""
def contains_phrases(text, phrases):
    pass

"""
takes a string and determines whether or not the string is of length 1, indicating
a single character. returns true if the length of text is 1, false otherwise

Example: is_single_char("h") should return True
Example: is_single_char("") should return False
Example: is_single_char("hi") should return False
"""
def is_single_char(text):
    pass

"""
takes a string and a character and returns the count of how many times that character
appears in the text string. this is case-sensitive, meaning capitalization matters 
when counting. because Python does not have a notion of a single character being different
from a string, you need to validate to make sure that the "char" variable is only 1 character long.
if "char" is longer than 1 character, or empty, return 0.

Example: count_characters("Hello, world!", "o") should return 2
Example: count_characters("Hello, world!", "l") should return 3
Example: count_characters("Hello, world!", "z") should return 0
Example: count_characters("Hello, world!", "") should return 0
Example: count_characters("Hello, world!", "Hello") should return 0
"""
def count_characters(text, char):
    pass

"""
takes a string and a character and returns teh count of how many times that character
appears in the text string. this is case-insenstive, meaning that capitalization does
NOT matter. because Python does not have a notion of a single character being different
from a string, you need to validate to make sure that the "char" variable is only 1 character long.
if "char" is longer than 1 character, or empty, return 0.

Example: count_characters("Hello, world!", "o") should return 2
Example: count_characters("Hello, world, hi!", "h") should return 1
Example: count_characters("Hello, world, hi!", "H") should return 0
Example: count_characters("Hello, world!", "") should return 0
Example: count_characters("Hello, world!", "Hello") should return 0
Example: count_characters("ORA ORA ORA", "O") should return 3
"""
def count_characters_ignore_case(text, char):
    pass

"""
takes a string and a character and returns the first index where that character
appears in the string. returns -1 if the character isn't in the string. this is
case sensitive, so capitalization matters. indexes start at 0.
if the char parameter is empty, or not a single character, return -1

Example: find_char_index("Hello, world!", "H") should return 0
Example: find_char_index("Hello, world!", "l") should return 2
Example: find_char_index("Hello, world!", "!") should return 12
Example: find_char_index("Hello, world!", "?") should return -1
Example: find_char_index("Hello, world!", "Hello") should return -1
"""
def find_char_index(text, char):
    pass

"""
tokenizing a string usually means splitting it up into parts.
take a string and return a list of all of the parts of the string, separated by
the space character (" "). an empty string should return an empty list
hint: use the split(...) function that strings provide

Example: tokenize_by_spaces("Hello, world!") should return ["Hello,", "world!"]
Example: tokenize_by_spaces("a b c d e f g") should return ["a", "b", "c", "d", "e", "f", "g"]
Example: tokenize_by_spaces("TheresNoSpaceHere") should return ["TheresNoSpaceHere"]
"""
def tokenize_by_spaces(text):
    pass

"""
a palindrome is spelled the same way forwards and backwards.
take a string and check whether it is a palindrome or not.
return True if it is, false otherwise

Example: is_palindrome("racecar") should return True
Example: is_palindrome("tacocat") should return True
Example: is_palindrome("Hello") should return False
Example: is_palindrome("1010101") should return True
Example: is_palindrome("??!!??") should return True
Example: is_palindrome("abc123") should return False
Example: is_palindrome("") should return True
"""
def is_palindrome(text):
    pass

"""
concatenation is stringing things together. take a list of words and combine them
into one long string.

Example: concatenate(["a", "b", "c", "1", "2", "3"]) should return "abc123"
Example: concatenate(["Hello", ",", " ", "world", "!"]) should return "Hello, world!"
"""
def concatenate(words):
    pass

"""
takes a string and prints it to the screen. this does not return anything

Example: echo("Hello, world!") should print "Hello, world!" to the console
"""
def echo(text_to_print):
    pass

"""
takes a string and a character, counts how many of those characters exist in the
string, and then prints that to the console in a formatted message. The format is:
'The string, "______" contains "__" __ times.'
this does not return anything

Example: print_letter_count("Hello, world!", "l") should print
                The string, "Hello, world!" contains "l" 3 times
"""
def print_letter_count(text, letter):
    pass

"""
Take a string source, a target phrase and some replacement string.
The idea is to look through the source string for each instance of target, then
replace the target with the replacement value. This is case sensitive, so case matters when finding
the target. After doing all of the replacements, return the result.

Hint: This is really easy with the string's built in replace method.

Example: replace("Hello, world!", "Hello", "Goodbye") should return "Goodbye, world!"
"""
def replace(source, target, replacement):
    pass
