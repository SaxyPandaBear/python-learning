Reading 1
=========

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
