class LetterA(Exception):
    pass
class LetterE(Exception):
    pass
class LetterI(Exception):
    pass
class LetterO(Exception):
    pass
class LetterU(Exception):
    pass

# This function will always just raise a plain Exception with no message.
def always_raise_exception():
    raise Exception("I'm always raised")

def divide_number_by_zero(number):
    return number / 0

"""
Validates whether the string contains any vowels
"""
def validate_string(s):
    # if we don't raise an exception, then the string is valid.
    for i in range(len(s)):
        letter = s[i]
        if  letter == 'a' or letter == 'A':
            raise LetterA()
        elif letter == 'e' or letter == 'E':
            raise LetterE()
        elif letter == 'i' or letter == 'I':
            raise LetterI()
        elif letter == 'o' or letter == 'O':
            raise LetterO()
        elif letter == 'u' or letter 'U':
            raise LetterU()
