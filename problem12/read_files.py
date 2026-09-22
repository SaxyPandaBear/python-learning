"""
Module that is used to read and manipulate files. Note that a lot of 
the functionality is replicated, but with different parameters. This
is method overloading - where multiple functions/methods share the same
name, but have different parameters. What is done in this file specifically
is not truly method overloading, because the intent is to have the same
value returned regardless of the method signature (the parameters given)
"""
import json  # use the json library to parse JSON data

"""
Given a file path that is expected to point to an existing file, read all of 
the characters in the file and print each of them to the console.
"""
def read_file(filepath):
    pass

"""
Given a file path that is expected to point to an existing file, read all of
file contents as a single string and return that value.
"""
def read_file_as_string(filepath):
    pass

"""
Given a file path that is expected to point to an existing file, read all of
the lines in the file and return the list of strings.
"""
def read_file_as_lines(filepath):
    pass

"""
Given a filename and the path where the file exists, read all of the lines in 
the file and print each of them to the console. This should be the same 
functionality as the other read_file() function.

The parameters should conform to the following assumptions.
Must validate this before attempting the read:
1. the path parameter MUST end with a trailing '/' character
2. the filename MUST NOT start /with a leading '/' character
If either of these conditions are not met, then an Exception must be raised.
Use the TestException class provided
"""
def read_file(some_path, filename):
    pass

"""
Given a filepath to where a json file is, attempt to read it. If the read fails,
the json module will raise a JSONDecodeError. In this function, the goal is to 
catch the JSONDecodeError if it occurs, and return false

If an exception is raised that is NOT a JSONDecodeError, you should just raise
it again. If it is a JSONDecodeError, return False. If no error occurred, 
return True.
"""
def is_valid_json(filepath):
    pass
