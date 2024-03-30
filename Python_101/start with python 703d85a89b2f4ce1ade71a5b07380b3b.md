# start with python

![Untitled](start%20with%20python%20703d85a89b2f4ce1ade71a5b07380b3b/Untitled.png)

> Python is a cross-platform programming language, which means it runs on
all the major operating systems
> 

# Fundamentals:

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
    
- **3. inputs & outputs:**
    
    we use these 2 functions to interact with the user:
    
    ```python
    #to scan from the user:
    Name=input("Enter you name:")
    #to print to the user terminal:
    print(f"my name is {Name}")
    ```
    
- **4. Arithmetic Operators:**
    
    **Arithmetic Operators** You can perform various arithmetic operations using the following syntax
    
    ```python
    summation = 2 + 5 #7
    sub = 4 - 10 #-6
    Multiplication = 2 * 8 #16
    Division = 6 / 3 #2
    Modulus = 10 % 3 #1
    exponents = 3 ** 3 #27
    
    #Shortened Form :
    result -= 5
    #instead of : 
    
    result = 10
    result = result - 5
    ```
    

---

> The Python community’s philosophy is contained in “The Zen of Python” by Tim Peters. You can access this brief set of principles for writing good Python code by entering
import this into your interpreter.
> 

```python
import this into
```

![https://www.skillbill.it/uploads/bxphpjcu1xv41.png](https://www.skillbill.it/uploads/bxphpjcu1xv41.png)

![Untitled](start%20with%20python%20703d85a89b2f4ce1ade71a5b07380b3b/Untitled%201.png)