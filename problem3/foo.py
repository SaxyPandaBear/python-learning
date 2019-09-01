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
    raise Exception()

def divide_number_by_zero(number):
    return number / 0
