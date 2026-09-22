Strings, again
==============

Now that we've done some work with lists, we can spend some more time with
strings, since strings in Python are a `List` of individual character elements. In other languages, it is common for a `Character` data type to
exist outside of strings, but in Python, a character is just a string 
of size 1.

Because of this characteristic, it's actually possible to infinitely reference
the first or last element of a string:
```python
s = "abc"
print(s[0][-1][0][-1][0][-1][0]) # prints 'a'
```

### Reminders/Tips

### Concepts
