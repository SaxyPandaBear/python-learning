Reading 1
=========

## Brushing up on Python syntax
There is an assumption of basic exposure to Python prior to starting
this, but just to go over some of the things here. 

Python is a scripting language, and as such, a Python file 
(the `.py` extension) is always technically some form of script. Now,
we don't always use them that way. For example, in this exercise, you
are expected to make modifications to the `numbers.py` file, but
we aren't running a script within that file. It acts as a utility of sorts,
that we are using in another Python script file, `problem1_test.py`.

> This crash course won't really cover the use cases of libraries/modules.

### The anatomy of a Python function
Functions are probably the most important piece of code inside of a Python
script. Let's take an example from `numbers.py` and deconstruct it, since
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

## Booleans
Booleans are straightforward, as they are either `True` or `False`. In some languages,
these values are represented by the literal values `1` and `0`, respectively. Booleans
are best suited to be a descriptive type for answering yes-or-no questions. 

For example, if I pose a question, "Is this number negative?", logically, you know how
to determine this. **If** the number is zero, or greater than zero, then the number is
*not* negative, thus `False`. 

> Note: if-else and branching code will be a part of a later problem.

### Comparison operators

To actually answer yes-or-no questions like the one above in code, Python gives you
comparison operators. Each one compares two values and evaluates directly to a `bool`
(`True` or `False`), which you can return straight out of a function without needing
`if`/`else` at all.

```python
x == y  # is x equal to y?
x != y  # is x NOT equal to y?
x > y   # is x greater than y?
x < y   # is x less than y?
x >= y  # is x greater than or equal to y?
x <= y  # is x less than or equal to y?
```

Note that `==` (comparison) is different from `=` (assignment). `x = 5` sets `x` to 5,
while `x == 5` asks "does `x` currently equal 5?" and gives back `True` or `False`.

Combining this with modular division from above, you can check whether a number is
even by asking whether the remainder after dividing by 2 is equal to 0:

```python
num % 2 == 0  # True if num is even, False otherwise
```

## My First Function

Writing functions in Python are helpful for illustrating a specific
action that we want to take. Using problem 1 as an example, I want
a way to tell if a number is odd.

```python
def is_odd(num: int):
    # some code goes here!
```

The structure of a function follows this pattern:
1. A function always starts with the keyword `def`
2. After `def` comes the name of the function - NO SPACES ALLOWED
3. After the name of the function, you can list the _parameters_ that you want the function to take. In the above example, we are saying that we expect a `num`, which is just a placeholder name of some value, that we want to use as part of the function.
4. The function closes with a `:`
5. All of the code of the function is indented

## Running the tests

Once you've filled in the functions in `numbers.py`, you can check your work by
running the test suite. From inside the `problem1` folder (not the root of the
repository), run:

```
python3 problem1_test.py
```

This will report how many tests passed and, for any failures, which function
produced the wrong answer.
