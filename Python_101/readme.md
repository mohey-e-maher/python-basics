# start with python

## Python 101

> Python is a cross-platform programming language, which means it runs on
all the major operating systems
> 
- **1. Comments:**
    
    It is ignored by the compiler in running the code.
    
    ```python
    #one line of comment here
    
    ```
    
- **2. Variables:**
    
    we use it to store the values:
    
    ```python
    #all the types of the variables:
    #string
    name = "Mohey"
    #integer
    age = 21
    #float
    salary = 2.5
    #boolean
    Married = True
    ```
    
    # Strings
    
    > Anything inside quotes is considered a string in Python
    > 
    
    ```python
    "This is a string."
    'This is also a string.'
    ```
    
    to know the type of the variable we use type() function
    
    ```python
    print(type(name))
    ```
    
    displays each word in title case, where each word begins with a title() capital letter, and upper case and lower case 
    
    ```python
    name = "ada lovelace"
    print(name.title())
    # Ada Lovelace
    
    name = "Ada Lovelace"
    print(name.upper())
    print(name.lower())
    # ADA LOVELACE
    
    # ada lovelace
    ```
    
    # Combining or Concatenating Strings
    
    It’s often useful to combine strings. For example, you might want to store a first name and a last name in separate variables.
    
    ```python
    F_name = "Mohey Eldeen"
    S_name = "Maher"
    full_Name = F_name +" "+ S_name
    print(full_Name)
    ```
    
    # Adding Whitespace to Strings with Tabs or Newlines
    
    ```python
    #the tab 
    >>> print("Python")
    Python
    >>> print("\tPython")
        Python
    # New Line 
    >>> print("Languages:\nPython\nC\nJavaScript")
    Languages:
    Python
    C
    JavaScript
    #
    ```
    
    Avoiding Type Errors with the str() Function
    Often, you’ll want to use a variable’s value within a message. For example,
    say you want to wish someone a happy birthday. You might write code
    like this:
    
    ```python
    age = 23
    message = "Happy " + age + "rd Birthday!"
    # we use in this case typecasting funstion
    >>> message = "Happy " + str(age) + "rd Birthday!" #it works
    print(message)
    ```
    
