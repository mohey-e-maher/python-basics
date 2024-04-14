<h1 align="center">start with python</h1>

![Untitled](../_media/Untitled.png)

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
    
- **5. Advanced Datatype:**
    
    we here show the advanced datatypes : (Lists -  tuples - string) 
    
    # 1. Lists
    
    it’s a **collection of data** and it may consist of **same/different data types** and it able to change anytime
    
    ```python
    names =['Mohey', 'Maher', 'Ali','Nasr']
    dump = ['mega',20,169.2,19,True]
    ```
    
     we could access any element from the list by detecting **the index** of the element and we could change it 
    
    ```python
    names =['Mohey', 'Maher', 'Ali','Nasr']
    print(names)
    names[0] = 'Memo'
    print(names)
    # ['Memo', 'Maher', 'Ali','Nasr']
    ```
    
    to add new element to the List { **append(element)** } / { **insert( index , element)** }
    
    ```python
    names =['Mohey', 'Maher', 'Ali','Nasr']
    print(names)
    names.append(2020)
    # ['Mohey', 'Maher', 'Ali','Nasr',2020]
    names.insert(0,'Ana')
    # ['Ana','Mohey', 'Maher', 'Ali','Nasr',2020]
    ```
    
    to remove element from list { **remove(element)** } / { **clear()** }
    
    ```python
    names =['Mohey', 'Maher', 'Ali','Nasr']
    names.remove('Mohey')
    print(names)
    # ['Maher', 'Ali','Nasr']
    names.clear()
    print(names)
    # []
    ```
    
    We could do list comprehensions”
    
    ```python
    # this code add new list and change the value of it
    nums = [0, 1, 2, 3, 4]
    squares = []
    for x in nums:
        squares.append(x ** 2)
    print(squares)
    # it could be written simply like this 
    nums =[0,1,2,3,4]
    squares = [x**2 for x in nums]
    print(squares)
    ```
    
    **List comprehensions can also contain conditions:**
    
    ```python
    nums = [0,1,2,3,4,5]
    even = [x **2 for x in nums if x%2==0]
    ```
    
    # 2. Tuples
    
    one of the advanced data type but it’s suitable for creating **unchangeable list** (couldn’t edit/remove/append )
    
    ```python
    student1 = ('Ahemed',18,170.3,True)
    print(student1[0])
    # we could create a tuple without the bracities
    student1 = 'Ahemed',18,170.3,True
    ```
    
    # 3. Dictionaries
    
    it’s a way to save a collection of data in the form of (key , value) which makes the access to the data easier than the index way
    
    ```python
    student_one  = {'Name': 'Ahmed','birthcity':'Giza','birthdate':'19-3-2003'}
    # to select an element by the key 
    student_one['Name']
    #>> Ahemd
    
    # to select all elements in dictionary 
    print(student_one.values())
    # {'Ahmed','Giza','19-3-2003'}
    
    # to know what's the keys of the dictionary
    print(student_one.keys())
    # 'Name','birthcity','birthdate'
    ```
    
    - **Set an entry in a dictionary**
    
    ```python
    dic['mohey'] = 'Good'
    print(dic['moehy']) # Good
    print(dic)
    # {'cat': 'cute', 'dog': 'furry', 'fish': 'wet'}
    ```
    
    - **we check if the key exists in the dictionary or not**
    
    ```python
    print(dic.get('money','Not exist'))
    # will return 'Not exist' because the value not in the dictionary
    print(dic.get('mohey','Empty'))
    # Good
    ```
    
    - **to remove an element from the dictionary:**
    
    ```python
    del dic['mohey']
    ```
    
    - **to iterate in a dictionary**
    
    ```python
    for key,value in dic.items():
    	print(f'{key} is {value}')
    # cat is cute
    # dog is furry
    # fish is we
    ```
    
    - **we could create a dictionary of sub-dictionaries and add to it:**
    
     
    
    ```
    # Dictionary of dictionaries
    europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
               'france': { 'capital':'paris', 'population':66.03 },
               'germany': { 'capital':'berlin', 'population':80.62 },
               'norway': { 'capital':'oslo', 'population':5.084 } }
    
    # Print out the capital of France
    print(europe['france']['capital'])
    
    # Create sub-dictionary data
    data = { 'capital':'rome', 'population':59.83}
    
    # Add data to europe under key 'italy'
    europe['italy']=data
    ```
    
- **6. if statements:**
    
    to create **conditions or instructions** on the code to verify the right condition and it runs the correct (True) condition
    
    ```python
    age = input("Enter your age :")
    if age >=18:
    	print("able to Enter the program")
    elif age <10:
    	print("anta men ya 3am")
    else:
    	print("sorry for you, not able to Enter")
    ```
    
- **7. Loops:**
    
    to make iterations on detect part of code for n number of times
    
    ### while loop
    
    ```python
    # while loop
    i=1
    while i<=5:
    	print(i)
    	i += 1 
    ```
    
    ### for loop & for loop with range() function
    
    ```python
    std = ["mohey","mo","ali","Bob"]
    for i in std:
    	print(std[i])
    #-------------------------------------
    for i in range(1,10,2 >>steps):
    	print(i)
    # will print from 1 to 9
    ```
    
    - **we could show the index in for loop by using {enumerate}**
    
    ```python
    fam = [1.73, 1.68, 1.71, 1.89]
    for index, height in enumerate(fam) :
    print(f"index {index} : {height}")
    ```
    
    - Do **for loop** on **Array** to print 2 columns
    
    ```python
    # house list of lists
    house = [["hallway", 11.25], 
             ["kitchen", 18.0], 
             ["living room", 20.0], 
             ["bedroom", 10.75], 
             ["bathroom", 9.50]]
             
    # Build a for loop from scratch
    for x in house:
        print(f"the {x[0]} is {x[1]} sqm")
    ```
    
    - For Loop on **Dictionary**
    
    ```python
    world = { "afghanistan":30.55,
    					"albania":2.77,
    					"algeria":39.21 }
    #the method items give us the key and the value in 2 variables 
    
    for key, value in world.items() :
    	print(f"{key} -- {value}")
    ```
    
    - to print 2D array in 1D array:
    
    we use nditer() function
    
    ```python
    # For loop over np_baseball
    for x in np.nditer(np_baseball):
        print(x)
    ```
    
    - to print the rows of Data Frame with the key or index:
    
    ```python
    import pandas as pd
    brics = pd.read_csv("brics.csv", index_col = 0)
    for lab, row in brics.iterrows():
    print(lab)
    print(row)
    ```
    
    - to print the rows of pandas coulmn
    
    ```python
    import pandas as pd
    brics = pd.read_csv("brics.csv", index_col = 0)
    for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])
    ```
    
- **8. Functions:**
    
    collect some of programming instructions in one collected body and it run after calling the function and could take parameters as input and return with values
    
    ```python
    def sum(x,y):
    	return x+y;
    	
    # to call the function
    z = sum(2,3)
    
    ```
    
    we could make the function take more that 1 parameter
    
    ```python
    def equa(x,y,z):
    	return (x*y)+z
    	
    result = equa(2,5,8)
    ```
    
- **9.Classes**
    
    The syntax for defining classes in Python is straightforward:
    
    ```python
    # initialize class 
    Class animals:
    	#Constructor
    	def __init__(self,name):
    		self.name = name
    # Instance method
    	def greet(self, loud = False):
    		if loud:
    			print('HELLO, {}'.format(self.name.upper()))
    		else:
    			print('Hello, {}!'.format(self.name))
    
    # (Not sure) create object from the class
    F_name = animals('Mohey')
    
    # call the instance method 
    F_name.greet()
    # Mohey
    F_name.greet(loud = True)
    # MOHEY
    ```
    

---

> The Python community’s philosophy is contained in “The Zen of Python” by Tim Peters. You can access this brief set of principles for writing good Python code by entering
import this into your interpreter.
> 

```python
import this into
```

![https://www.skillbill.it/uploads/bxphpjcu1xv41.png](https://www.skillbill.it/uploads/bxphpjcu1xv41.png)

![Untitled](../_media/Untitled%201.png)

---

In the end we have to say 

![41f05b9a516c6bb1d42a75e1eba940dc.webp](https://i0.wp.com/islamphotos.net/wp-content/uploads/2018/10/41f05b9a516c6bb1d42a75e1eba940dc.png?fit=914%2C608)