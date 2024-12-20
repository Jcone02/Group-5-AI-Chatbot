import json

# Sample data
data = [
    {"messages": [{"role": "user", "content": "What is a variable in Python?"}, {"role": "assistant", "content": "A variable in Python is used to store data values. Variables are created when you assign a value to them."}]}
    {"messages": [{"role": "user", "content": "How do you create a variable in Python?"}, {"role": "assistant", "content": "You create a variable by simply assigning a value to a name: e.g., `x = 10`."}]}
    {"messages": [{"role": "user", "content": "What are Python data types?"}, {"role": "assistant", "content": "Common Python data types include integers, floats, strings, booleans, lists, tuples, sets, and dictionaries."}]}
    {"messages": [{"role": "user", "content": "How do you create a list in Python?"}, {"role": "assistant", "content": "A list is created using square brackets: e.g., `my_list = [1, 2, 3]`."}]}
    {"messages": [{"role": "user", "content": "What is a function in Python?"}, {"role": "assistant", "content": "A function in Python is a block of reusable code that performs a specific task. It is defined using the `def` keyword."}]}
    {"messages": [{"role": "user", "content": "How do you define a function in Python?"}, {"role": "assistant", "content": "You define a function using the `def` keyword: `def my_function():`."}]}
    {"messages": [{"role": "user", "content": "What is a for loop in Python?"}, {"role": "assistant", "content": "A for loop in Python is used to iterate over a sequence (like a list, tuple, or string) and execute a block of code multiple times."}]}
    {"messages": [{"role": "user", "content": "Give an example of a Python for loop."}, {"role": "assistant", "content": "Example: `for i in range(5): print(i)` will print numbers from 0 to 4."}]}
    {"messages": [{"role": "user", "content": "What is a while loop in Python?"}, {"role": "assistant", "content": "A while loop in Python repeatedly executes a block of code as long as the given condition is `True`."}]}
    {"messages": [{"role": "user", "content": "Give an example of a Python while loop."}, {"role": "assistant", "content": "Example: `while x < 5: x += 1` will increment `x` until it reaches 5."}]}
    {"messages": [{"role": "user", "content": "What is an if statement in Python?"}, {"role": "assistant", "content": "An if statement is used to run a block of code based on a condition being `True`."}]}
    {"messages": [{"role": "user", "content": "Give an example of an if statement in Python."}, {"role": "assistant", "content": "Example: `if x > 10: print('x is greater than 10')`."}]}
    {"messages": [{"role": "user", "content": "What is a dictionary in Python?"}, {"role": "assistant", "content": "A dictionary in Python is an unordered collection of key-value pairs. It is defined using curly braces: `my_dict = {'key': 'value'}`."}]}
    {"messages": [{"role": "user", "content": "How do you access values in a dictionary?"}, {"role": "assistant", "content": "You can access values in a dictionary using their keys: `my_dict['key']`."}]}
    {"messages": [{"role": "user", "content": "What is a tuple in Python?"}, {"role": "assistant", "content": "A tuple is a collection of ordered and immutable objects. Tuples are defined using parentheses: `my_tuple = (1, 2, 3)`."}]}
    {"messages": [{"role": "user", "content": "How do you create a class in Python?"}, {"role": "assistant", "content": "You create a class using the `class` keyword: `class MyClass:`."}]}
    {"messages": [{"role": "user", "content": "What is inheritance in Python?"}, {"role": "assistant", "content": "Inheritance in Python allows a class to inherit properties and methods from another class, promoting code reusability."}]}
    {"messages": [{"role": "user", "content": "How do you handle exceptions in Python?"}, {"role": "assistant", "content": "You handle exceptions using try-except blocks: `try: ... except Exception as e:`."}]}
    {"messages": [{"role": "user", "content": "What is a list comprehension in Python?"}, {"role": "assistant", "content": "List comprehensions provide a concise way to create lists. Example: `[x for x in range(5)]`."}]}
    {"messages": [{"role": "user", "content": "What is a lambda function in Python?"}, {"role": "assistant", "content": "A lambda function is a small anonymous function in Python, defined using the `lambda` keyword. Example: `lambda x: x + 2`."}]}
    {"messages": [{"role": "user", "content": "What is the difference between a list and a tuple?"}, {"role": "assistant", "content": "A list is mutable (can be changed), whereas a tuple is immutable (cannot be changed after creation)."}]}
    {"messages": [{"role": "user", "content": "How do you install a package in Python?"}, {"role": "assistant", "content": "You can install a package using `pip`, the Python package manager. Example: `pip install requests`."}]}
    {"messages": [{"role": "user", "content": "How do you import a module in Python?"}, {"role": "assistant", "content": "You can import a module using the `import` statement. Example: `import math`."}]}
    {"messages": [{"role": "user", "content": "What is the purpose of the `__init__` method in Python classes?"}, {"role": "assistant", "content": "The `__init__` method is a constructor used to initialize an object's attributes when a class is instantiated."}]}
    {"messages": [{"role": "user", "content": "What is a decorator in Python?"}, {"role": "assistant", "content": "A decorator in Python is a function that takes another function and extends its behavior without explicitly modifying it."}]}
    {"messages": [{"role": "user", "content": "What are *args and **kwargs in Python?"}, {"role": "assistant", "content": "`*args` is used to pass a variable number of non-keyword arguments, and `**kwargs` allows you to pass a variable number of keyword arguments to a function."}]}
    {"messages": [{"role": "user", "content": "How do you open a file in Python?"}, {"role": "assistant", "content": "You can open a file using the `open()` function: `file = open('filename.txt', 'r')`."}]}
    {"messages": [{"role": "user", "content": "What is the difference between `append()` and `extend()` in Python?"}, {"role": "assistant", "content": "`append()` adds a single element to the end of a list, while `extend()` adds all elements from another iterable to the list."}]}
    {"messages": [{"role": "user", "content": "How do you check the length of a list in Python?"}, {"role": "assistant", "content": "You can check the length of a list using the `len()` function. Example: `len(my_list)`."}]}
    {"messages": [{"role": "user", "content": "How do you reverse a list in Python?"}, {"role": "assistant", "content": "You can reverse a list using the `reverse()` method or by slicing: `my_list[::-1]`."}]}
    {"messages": [{"role": "user", "content": "What is a set in Python?"}, {"role": "assistant", "content": "A set is an unordered collection of unique elements, created using curly braces: `my_set = {1, 2, 3}`."}]}
    {"messages": [{"role": "user", "content": "How do you remove duplicates from a list in Python?"}, {"role": "assistant", "content": "You can remove duplicates from a list by converting it to a set: `list(set(my_list))`."}]}
    {"messages": [{"role": "user", "content": "How do you comment in Python?"}, {"role": "assistant", "content": "Single-line comments start with a `#`. Multi-line comments can be created using triple quotes: `'''comment'''`."}]}
    {"messages": [{"role": "user", "content": "What is the difference between `==` and `is` in Python?"}, {"role": "assistant", "content": "`==` checks for value equality, while `is` checks for object identity."}]}
    {"messages": [{"role": "user", "content": "What is the Python `range()` function?"}, {"role": "assistant", "content": "`range()` is used to generate a sequence of numbers. Example: `range(0, 10)` generates numbers from 0 to 9."}]}
]

# Write data to a JSONL file
with open('file-training.jsonl', 'w') as jsonl_file:
    for entry in data:
        jsonl_file.write(json.dumps(entry) + '\n')
