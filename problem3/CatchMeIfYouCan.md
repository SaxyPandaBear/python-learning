Catch Me If You Can
===================

There are some functions that need to be written in `catch_me.py`. Do not modify the `foo.py` file. You will be using the code from `foo.py` within your own python file.

To validate your code, run `python problem3_test.py`

### Reminders / Tips
- When you want to wrap code in a `try` block, make sure to confine the code in that block to be as succinct as possible. This is so that you don't catch something that shouldn't be caught with your logic.
- Remember to use the `finally` block to reset anything that needs to, such as an opened file or database connection. These are resources that should be closed so you don't leak memory.
- Although you can usually catch all exceptions with an umbrella exception, such as `Exception`, this is not advisable because generally there will be different decisions based on which exception is raised.
- Make use of the `as` keyword to declare an exception that is caught as a variable so you can use it in the `except` block.
- You can have multiple `except` blocks tied to a single `try` block, but only one `finally` block.
- The `repr` function for Exceptions in Python will be more helpful than the `str`, becaues it provides more information. Example: `repr(some_exception)`

### Concepts Focused On
- Exception handling
- Using external functions
