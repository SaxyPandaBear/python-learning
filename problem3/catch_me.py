"""
Module that makes use of try-except-finally blocks
"""
import foo


"""
Call the always_raise_exception() function from the foo module,
catch it, and return the exception's representation (the repr() function)
"""
def some_function():
    pass

"""
Call the validate_string() function from the foo module. 
If the validate_string sees any vowels in it, it will throw an exception 
based on the first vowel it finds. If it doesn't see any vowels, it will print
the string that you pass in, and return True

The flow of this function is laid out below:
1. try to validate the string
2. if an exception is raised, catch it, print the exception, and then depending 
   on the vowel that was found, replace the vowel with the censor character
3. try to validate the string again after censoring the caught vowel.
4. do this until the validate_string() method returns True
"""
def scared_of_vowels(some_str, censor):
    pass
