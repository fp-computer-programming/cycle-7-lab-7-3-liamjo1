"""
Create a Python file named lab_7-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-1 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately

"""
# Liam O'Hara 

def greeting():
    """
    This function prints 'Hello World' on one line & returns the docstring.
    """
    print("Hello World!")

    # Docstring is the greeting
    return greeting.__doc__ 

# Another statement to call the function:
greeting()

# 1: Call the function again

# This should print 'Hello World!' again on one line.
greeting()

# 2: Call the function with a different name

# This should also print 'Hello World!' on one line.
def another_greeting():
    greeting()

another_greeting()

# 3: Call the function multiple times

# This should print 'Hello World!' each time it's called.
for _ in range(3):
    greeting()

# Test Case 4: Call the function in a loop with a break

# This should print 'Hello World!' once and then break out of the loop.
while True:
    greeting()
    break