"""
Module that defines some basic math calculation utility functions
"""

def add(x: int, y: int) -> int:
    """
    takes two numbers and returns the sum of them.

    Example: add(1, 2) should return 3
    :param x a number
    :param y another number
    :return the sum of x and y
    """
    pass

"""
takes two numbers and returns the product of them.

Example: multiply(2, 5) should return 10
"""
def multiply(x: int, y: int) -> int:
    pass

"""
takes two numbers and returns the remainder of n / d.

Example: remainder(3, 2) should return 1
Example: remainder(100, 37) should return 26
Example: remainder(4, 2) should return 0
Example: remainder(0, 5) should return 0
"""
def remainder(numerator, divisor):
    pass

"""
takes a list of numbers and returns the sum of all of the numbers in the list.
If the list of numbers is empty, it should return 0

Example: add_all([1,2,3,4,5]) should return 15
Example: add_all([]) should return 0
Example: add_all([600]) should return 600
"""
def add_all(numbers):
    pass

"""
takes a number and a list of numbers, then returns the result of
subtractiong all of the numbers in the list from the first parameter.

Example: subtract_from(10, [2,4]) should return 4 because 10 - 2 - 4 = 4
Example: subtract_from(5, [1,2,3]) should return -1 because 5 - 1 - 2 - 3 = -1
Example: subtract_from(100, []) should return 100
"""
def subtract_from(num, numbers):
    pass


"""
takes a number and returns True if the number is odd, False otherwise

How do you know if a number is odd? 

Example: is_odd(5) should return True
Example: is_odd(8) should return False
"""
def is_odd(num: int):
    pass


"""
takes a number and returns True if the number is even, False otherwise

Hint: If a number is even, can it also be odd? 

Example: is_even(5) should return False
Example: is_even(8) should return True
"""
def is_even(num):
    pass
