Read, Write
===========

There are functions that need to be written in `read_files.py`, as well as `write_files.py`

To validate your code, run `python problem4_test.py`

### Reminders / Tips
- If you want to use a tab character or start on a newline, the characters for those are `\t` and `\n` respectively. Example: `"\tTabbed over.\nNow a new line."`
- Always use the `with open(...)` style syntax when interacting with files unless you know what you are doing, to make sure that file streams are closed properly.
- When you read lines and write lines, remember that explicitly accounts for newline characters
- Make good use of the `json` library in Python
- Dictionaries and JSON objects are almost synonymous in Python. Access values by keys by doing `the_value = my_dict["Some_Key"]`
- Setting values in dictionaries are simple: `my_dict["some_key"] = some_value`

### Concepts Focused On
- String operations
- Understanding file paths
- Reading from files
- Writing to files
- List operations
- Iterating over strings
- Dictionaries
- Introduction to working with JSON data
- Introduction to method / function overloading
