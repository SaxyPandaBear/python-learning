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

## Reminders/Tips
* There are a **lot** of built-in string functions that can help you do common transformations or checks. Take a look at the [Python docs](https://docs.python.org/3/library/string.html) and see if what you're looking for already exists as a built-in function.

## Concepts worked on
