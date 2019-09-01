Inception
=========

This is a task on recursion. Recursion put simply is performing the same 
action repeatedly until an end condition is reached. This can also be seen 
as a form of iteration, like a `while` or `for` loop that you've already seen 
before. Recursion in general is harder for people to learn because it requires 
a different thought process initially, and if you learn an iterative loop first, 
like a `for` loop, then learning recursion becomes foreign, and harder. Ultimately, 
however, using recursion is actually very similar to looping. Let's look at an example of a for loop:

```python
def iterative():
    letters = ["a", "b", "c"]
    result = ""
    for letter in letters:
        print(letter)
        result += letter
    print(result)
```

In the above example, we loop over a list of things, print each thing and also 
concatenate the strings together to form a final result.

The result of the above is:
```
a
b
c
abc
```

The idea of recursion revolves around two notions.

**The Base Case**
- The base case is the point that recursion stops. 
- There should not be more to operate on when recursion is complete. The task should be done.

**Recursing**
- When you recurse, you are performing the same *action* repeatedly. This is not the same as saying you are doing the exactly the same thing over and over again. That would be an endless cycle. Typically, you are repeating the same action, but on a different set of data.
- For recursion to work, you always have to have some way to break the recursion, using the defined base case.

Let's see this in action by rewriting the above iterative example using recursion.

```python
def recursive():
    letters = ["a", "b", "c"]
    state = ""
    recursion_helper(letters, state)

def recursion_helper(letters, state):
    if len(letters) == 0:
        print(state)
    else:
        print(letters[0])
        recursion_helper(letters[1:], state + letters[0])
```

This is a lot to digest so let's go function by function, then line by line.

#### recursive()

You may have noticed that there are two functions written to provide the same 
functionality as the iterative solution. This is one of the drawbacks to using 
recursion. Another drawback is complexity, but we won't get into what I mean by that.

This function is used primarily as a way to set up the initial state of 
the recursion. Note that there is a similar set up in the iterative solution. 
In that version, the state is set up by initializing the `letters` and `result` 
variables with the intended starting point, then the iteration starts by going 
over each of the items in the list. This is actually very similar, conceptually 
speaking, to the recursive solution. 

#### recursion_helper(letters, state)

There was a very deliberate choice of wording for `state`. When you execute a 
function, all it should know is the parameters it is given, and the logic baked 
into it. There should not be external intervention, such as storing state outside 
of the function. This is an anti-pattern in functional programming, which is where 
recursion shines. In some cases, functional programming languages don't even have 
the ability to execute a `for` or `while` loop, so recursion is the only way to 
iterate.
