Reading 1
=========

## Brushing up on Python syntax
There is an assumption of basic exposure to Python prior to starting
this, but just to go over some of the things here. 

Python is a scripting language, and as such, a Python file 
(the `.py` extension) is always technically some form of script. Now,
we don't always use them that way. For example, in this exercise, you
are expected to make modifications to the `calculator.py` file, but
we aren't running a script within that file. It acts as a utility of sorts,
that we are using in another Python script file, `problem1_test.py`.

### The anatomy of a Python function
Functions are probably the most important piece of code inside of a Python
script. Let's take an example from `calculator.py` and deconstruct it, since
some additions in Python 3.7+ have made Python code more readable and maintainable,
but may not be common knowledge for people just starting, or moving from a 
different language.

```python
def add(x: int, y: int) -> int:
    """
    takes two numbers and returns the sum of them.

    Example: add(1, 2) should return 3
    :param x a number
    :param y another number
    :return the sum of x and y
    """
    pass
```

Starting at the top, we have the function definition. To tell Python we
want to create a new function, we use the `def` keyword, followed by
the name of the function we want to write. In this case, the name of the
function in is `add`. After the name of the function, we list out the
parameters (also known as arguments) of the function. 

Here, we are saying that our add function requires two parameters, 
`x` and `y`. These are the names of the variables that we can 
reference inside of our function. When someone calls the add function,
we can reference the input used with those variable names. 
For example, if I call `add(1, 2)`, then `x` is 1, and `y` is 2 
when I call it. If you call `add(2, 3)`, then `x` is 2, and `y` 
is 3, for when you called the function.

Next thing to look at is the _type annotation_ on the function parameters.
Specifically, let's look at `x: int`. This is a way for us as the developer
to tell other developers "Hey, I am defining this parameter as 'x', and I
am expecting the value to be of type `int`." It's important to note that
Python is a weakly typed, dynamic language. Even though we are saying that
we expect a number for that parameter, that does not stop someone from using
our add function and providing something else that may not work, like a string.
We have to be very diligent when writing Python code, to make sure that we
account for misuse of our functions.

Skipping on ahead in the function definition, after the parameters are defined,
we have another type annotation that denotes what we expect the return type of
the function to be. In the case of the add function, we have ` -> int:`, so
we are saying that we expect the add function to return an int.

**Note that the type annotations for the function parameters and return value
and purely optional, but they can help with readability**.

After the function definition, here we have a block comment in the form of
triple quotes. This is documentation on our function. Here, we can write whatever
useful information we may want to, to help developers (including ourselves)
understand what this function does at a glance.

## Math Operations

In Python, you can do basic arithmetic pretty easily. It can compute things
like how you would have written them in your school math classes.
For example:

```python
x = 1
y = 2
z = x + y
a = x - 1
b = x * 4 - y
```

Python will follow the same basic order of operations that you learned in math 
class. That being said, the notion of an exponent is not written the same way you 
would write it in your algebra class.

```python
x = 2 ** 3 # this is 2^3 in math
```

Python also has the idea of "modular" division. This is performing division on 
something and only getting back the remainder. For example, 5 mod 2 gives 1, which 
is the remainder of 5 divided by 2. In Python, it is denoted as such:

```python
y = 5 % 2
```

This comes in handy when you need to evenly distribute things, or when you want
to check if a number is odd or even. If the remainder is 0 when you mod by 2, then
the number must be even!

## List Operations

We'll only touch on this briefly. A "list" is what we will refer to as a 
sequence of things. In some languages, like Java, the types of things in 
the list must be the same, but we won't get into that for the purposes of 
this exercise. 

Things in a list in Python are grouped by brackets, `[]`. 

For example:

```python
numbers = [1, 2, 4, 5, 6, 7, 8, 9]
```

Now we have a list of numbers, ranging from 1 to 9.

## My First Function

Writing functions in Python are helpful for illustrating a specific
action that we want to take. Using problem 1 as an example, I want
a way to tell if two numbers are the same.

```python
def is_odd(num):
    # some code goes here!
```

The structure of a function follows this pattern:
1. A function always starts with the keyword `def`
2. After `def` comes the name of the function - NO SPACES ALLOWED
3. After the name of the function, you can list the _parameters_ that you want the function to take. In the above example, we are saying that we expect a `num`, which is just a placeholder name of some value, that we want to use as part of the function.
4. The function closes with a `:`
5. All of the code of the function is indented
