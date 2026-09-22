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
based on the first vowel it finds. If it doesn't see any vowels, it does 
nothing. The goal of this function is to call the validate_string() function.
If an exception is thrown, catch it and print it's repr(). If the string is 
valid, then print the string.

The flow of this function is laid out below:
1. try to validate the string
2. if an exception is raised, catch it, print the exception, and then depending 
   on the vowel that was found, replace the vowel with the censor character
3. try to validate the string again after censoring the caught vowel.
4. do this until the validate_string() method finishes without an exception.
5. When the validation is complete, return the final, censored string.

Note that this can create an infinite loop, because if there are no restrictions
on what the censor phrase is, you can attempt to make the censor a vowel. 
In this scenario, the function would continuously see a vowel, replace it with 
a vowel, and attempt to validate again. 

To protect against this, you need to check if the censor contains any vowels in 
it, and if so raise an Exception.
"""
def scared_of_vowels(some_str, censor):
    pass
