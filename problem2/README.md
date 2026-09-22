Learning Strings
================

We've glossed over strings as just a fundamental data type, so we need to
take some time to discuss how they work. Strings are a logical sequence
of individual characters, and one of the most common data types you will
work with, regardless of programming language. You've already experienced 
strings, even in the first problem, which only dealt with numbers.

## Writing your first string
There are several ways to compose strings - this problem will only go over the most
basic form. 

```python
name = "Andrew"
```

It's really that simple. Note that there are different acceptable syntaxes for
instantiating a string. Above, the string is composed with double quotes: `""`,
but they can also be created with single quotes:
```python
name = 'Andrew'
```

Sometimes you'll have to be mindful of which quote you choose to use. For example,
if you need to use an apostrophe inside of your string value, this won't work:
```python
sentence = 'This isn't my sentence'
```
because Python will enclose the string with the apostrophe inside the sentence.

To avoid this, you can mix and match single and double quotes:
```python
sentence1 = "This isn't my sentence"
sentence2 = 'And he said, "She sells seashells by the seashore"'
sentence3 = """Her response was, "Well, that's not really my cup of tea, though"."""
```

### Multi-line strings
There is a concept of multi-line strings, as illustrated by `sentence3` in 
the above example. Above, it's use doesn't 100% align with it's name, so we'll go
over what you can do with multi-line strings in this section.

Look at the below code, which does not work:
```python
name = "Andrew
Huynh"
```

This code attempts to put two different words (`"Andrew"`, and `"Huynh"`) on separate
lines, but doesn't work. If you want to embed line separators in a single string, you need
to use a *multi-line string*. These are defined by using three consecutive quote characters
instead of one:
```python
name = """Andrew
Huynh
"""
```

Note that this works for both double quotes and single quotes. 

You might have noticed that the in-line documentation in the problems uses 
multi-line strings without assigning them to any value. Technically, you could
assign them to a value, but there's really no need to. When Python executes the code,
it will discard the strings and move on because they aren't used, making multi-line
strings a great, clean way to organize docstrings in your code.

## Working with strings
This won't go in depth on different string operations. The purpose of this exercise
is to familiarize you with strings first. We'll get into different cool things
you can do with strings in subsequent exercises.

### Concatenation
The concept of concatenation is stitching two strings together. Think of it as:
```
concatenate(a, b) = a + b.
```
Concatenating strings in Python is really simple. You just use the `+` operator.
Note that we'll delve into why that works in a later exercise.

```python
x = "abc"
y = "123"
z = x + y  # this should be "abc123"
```

### String length

Since strings are sequences of characters, you can ask how many characters
are in one using the built-in `len()` function:

```python
name = "Andrew"
len(name)  # 6
```

This works on any sequence in Python, not just strings, so you'll see
`len()` again later when working with lists.

### Indexing and slicing strings

> Immportant note: You'll get more practice with lists/sequences in the following exercise, so don't stress about it too much.

Because a string is a sequence, you can reach into it and grab individual
characters, or ranges of characters, using square brackets `[]` after the
string, along with a position. Positions start counting at 0 for the first
character:

```python
name = "Andrew"
name[0]  # "A", the first character
name[1]  # "n", the second character
```

You can also count backwards from the end of the string using negative
numbers, where `-1` is the last character:

```python
name[-1]  # "w", the last character
```

Grabbing a range of characters (rather than just one) is called *slicing*,
and is done by putting a start and end position, separated by a colon,
inside the brackets. The end position is *exclusive*, meaning the
character at that position is not included in the result:

```python
name = "Andrew Huynh"
name[0:6]   # "Andrew"
name[7:12]  # "Huynh"
```

### Calling methods on a string

So far, every piece of code you've written has been either a standalone
function call, like `add(1, 2)`, or an operator, like `x + y`. Strings also
come with their own built-in *methods* - functions that live directly on
the string value itself, and are called using a dot (`.`) after the string.

```python
name = "Andrew"
shout = name.upper()  # "ANDREW"
```

Here, `upper()` is a method that already exists on every string. To call
it, you write the string (or a variable holding a string) followed by a
`.`, followed by the method name and parentheses. You can chain this off of
a variable or a literal string directly:

```python
"hello".upper()  # "HELLO"
```

A few of the most common string methods:

```python
"WOW".lower()          # "wow"
"wow".upper()           # "WOW"
"hello world".capitalize()  # "Hello world"
```

Note that these methods don't change the original string - they return a
*new* string with the transformation applied. This is because strings in
Python are immutable, meaning once created, a string's contents can't be
changed in place.

### Checking if something is inside a string

Sometimes you need to know whether one string shows up inside another one,
like checking if a word contains a particular letter. Python has a keyword
for exactly this, `in`, which you place between the thing you're looking
for and the thing you're looking inside of:

```python
"e" in "hello"      # True
"z" in "hello"      # False
"lo" in "hello"     # True, this works with more than one character too
```

This expression evaluates directly to a `bool`, just like the comparison
operators from the previous problem.

### Comparing strings

The comparison operators you saw in the previous problem (`==`, `!=`, and
friends) work on strings the same way they work on numbers. `==` checks
whether two strings are exactly the same, character for character:

```python
"hello" == "hello"  # True
"hello" == "Hello"  # False, capitalization matters!
```

That last example is worth paying attention to: string comparisons are
case-sensitive by default, so `"hello"` and `"Hello"` are considered
different strings. If you want to compare two strings while ignoring their
capitalization, you'll need to normalize their case first (see the methods
above) before comparing them.

### Converting between strings and numbers

You may have noticed that Python won't let you combine a string and a
number with `+`:

```python
"Age: " + 25  # This raises a TypeError!
```

This is because `+` requires both sides to be the same type - Python won't
automatically guess that you meant to turn `25` into `"25"` first. To fix
this, you can convert a number into its string representation using the
`str()` function:

```python
"Age: " + str(25)  # "Age: 25"
```

The reverse is also possible: if you have a string that represents a
number and want to actually do math with it, you can convert it using the
`int()` function:

```python
int("25")  # 25, as an actual number, not a string
```

### The empty string

`""` is a perfectly valid string - it's just a string with zero characters
in it. It's a common edge case to consider: what should your code do if
it's handed an empty string instead of one with actual letters in it? Keep
this in mind as you write your functions, and make sure to think through
what the "right" behavior is when a string turns out to be empty.

### Non-ASCII strings
This will not covered as part of this course, but there are ways to 
represent string data that aren't limited to ASCII characters. 
For example, special characters with accents, emoji codes, and bytestrings
are all representable with a string in Python. As already stated, these
will not be covered here.

## Reminders/Tips
* There are a **lot** of built-in string functions that can help you do common transformations or checks. Take a look at the [Python docs](https://docs.python.org/3/library/string.html) and see if what you're looking for already exists as a built-in function.
