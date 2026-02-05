## Lab 02: Prompt Engineering Solutions

### Problem 1: Debugging

**My Prompt:**
You are a senior Python developer. I have a function that's supposed to sum all even numbers in a list, but it's giving wrong results. Can you identify the bug and provide the corrected version? Please explain what was wrong. Here is the code:

```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list."""
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```
**AI's Corrected Code:**

```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list."""
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Fixed: check for even numbers
            total += num
    return total
```

**What I Learned:**
The function was checking for odd numbers instead of even numbers. The AI showed me that carefully reviewing conditionals is key when debugging logic errors.

### Problem 2: Refactoring

**My Prompt:**
You are a senior Python developer. I have a function that extracts names of adult users (18+) from a list of dictionaries. It works but is written in a confusing, non-Pythonic way. Can you refactor this function to be more Pythonic, readable, and concise using best practices? Here is the code:

```python
def get_names_of_adults(users):
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

**AI's Corrected Code:**

```python
def get_names_of_adults(users):
    """Return a list of names of users who are 18 or older."""
    return [user['name'] for user in users if user['age'] >= 18]
```

**What I Learned:**
List comprehensions make Python code much shorter and more readable. Using direct iteration over items avoids unnecessary indexing.

### Problem 3: Documenting

**My Prompt:**
You are an expert Python developer and technical writer familiar with NumPy-style docstrings. I have a function that calculates the area of a rectangle and raises a ValueError for non-positive inputs. Can you add a professional NumPy-style docstring including parameters, return value, and exceptions? Here is the code:

```python
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```
**AI's Corrected Code:**

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle. Must be a positive number.
    width : float
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float
        The area of the rectangle.

    Raises
    ------
    ValueError
        If length or width is not a positive number.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```
**What I Learned:**
The AI showed me how to write clear, professional documentation in NumPy style, including parameter descriptions, return types, and exceptions for robust functions.
