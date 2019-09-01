"""
Module that is used to read and manipulate files. Note that a lot of 
the functionality is replicated, but with different parameters. This
is method overloading - where multiple functions/methods share the same
name, but have different parameters. What is done in this file specifically
is not truly method overloading, because the intent is to have the same
value returned regardless of the method signature (the parameters given)
"""
import json  # use the json library to parse JSON data


def read_file(filepath):
    pass

def read_file_as_string(filepath):
    pass

def read_file_as_lines(filepath):
    pass

def read_file(some_path, filename):
    pass

def is_valid_json(jsonfile):
    pass
