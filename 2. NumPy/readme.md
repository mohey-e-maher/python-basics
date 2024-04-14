
<h1 align="center">NumPy</h1>

> NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. If you are already familiar with MATLAB, you might find this [tutorial](http://wiki.scipy.org/NumPy_for_Matlab_Users) useful to get started with Numpy.
> 

# Fundamentals:

- **How to use it ?**
    
    **how to import the library**
    
    ```python
    import numpy as np
    ```
    
- **array initialization**
    
    we could NumPy array from a list 
    
    ```python
    a = np.array([1, 2, 3])  # Create a rank 1 array
    print(type(a), a.shape, a[0], a[1], a[2])
    # <class 'numpy.ndarray'> (3,) 1 2 3
    ```
    
    as 2D array
    
    ```python
    b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
    ```
    
- **Methods**
    - we could create an array of zeros
    
    ```python
    a = np.zeros((2,2))  # Create an array of all zeros
    print(a)
    # [[0. 0.]
       [0. 0.]
    ```
    
    - we could create an array of Ones
    
    ```python
    b = np.ones((1,2))   # Create an array of all ones
    print(b)
    # [[1. 1.]]
    ```
    
    - we could create an array of constant
    
    ```python
    c = np.full((2,2), 7) # Create a constant array
    print(c)
    # [[7 7]
       [7 7]]
    ```
    
    - create an array of random numbers
    
    ```python
    e = np.random.random((2,2)) # Create an array filled with random values
    print(e)
    '''
    [[0.79825356 0.96284263]
     [0.73245882 0.4551524 ]] 
    '''
    ```
    
- **Array indexing**
    
    Slicing: Similar to Python lists, numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each dimension of the array:
    
    ```python
    import numpy as np
    a = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
    
    # Use slicing to pull out the subarray consisting of the first 2 rows
    # and columns 1 and 2; b is the following array of shape (2, 2):
    b = a[:2, 1:3]
    print(b)
    # [[2 3]
    #  [6 7]]
    ```
    
    another example on slicing
    
    ```python
    row_r1 = a[1, :]    # Rank 1 view of the second row of a  
    row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
    row_r3 = a[[1], :]  # Rank 2 view of the second row of a
    print(row_r1)
    print(row_r2)
    print(row_r3)
    
    #[[5 6 7 8],
    #[1 2 3 4],
    #[6 8 9 7]
    
    ```
    
    **Boolean array indexing:** Boolean array indexing lets you pick out arbitrary elements of an array. Frequently this type of indexing is used to select the elements of an array that satisfy some condition. Here is an example:
    
    ```python
    import numpy as np
    a = np.array([[1,2], [3, 4], [5, 6]])
    bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                        # this returns a numpy array of Booleans of the same
                        # shape as a, where each slot of bool_idx tells
                        # whether that element of a is > 2.
    print(bool_idx)
    # [[False False]
    #  [ True  True]
    #  [ True  True]]
    ```
    
- **Array Math**
    
    Basic mathematical functions operate elementwise on arrays, and are available both as operator overloads and as functions in the numpy module:
    
    - to make addition between 2 numpy arrays
    
    ```python
    x = np.array([[1,2]
    						 ,[3,4]], dtype=np.float64)
    
    y = np.array([[5,6]
                 ,[7,8]], dtype=np.float64)
    
    # Elementwise sum; both produce the array
    print(x + y)
    print(np.add(x, y))
    # **[[ 6.  8.]
    #  [10. 12.]]**
    ```
    
    - difference (-)
    
    ```python
    # Elementwise difference; both produce the array
    print(x - y)
    print(np.subtract(x, y))
    ```
    
    - product ( * )
    
    ```python
    # Elementwise product; both produce the array
    print(x * y)
    print(np.multiply(x, y))
    ```
    
    - division (/)
    
    ```python
    # Elementwise division; both produce the array
    print(x / y)
    print(np.divide(x, y))
    ```
    
    - square root
    
    ```python
    # Elementwise square root; produces the array
    print(np.sqrt(x))
    ```
    
    `*` is elementwise multiplication, not matrix multiplication. We instead use the dot function to compute the inner products of vectors, to multiply a vector by a matrix, and to multiply matrices. dot is available both as a function in the numpy module and as an instance method of array objects:
    
    ```python
    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])
    
    v = np.array([9,10])
    w = np.array([11, 12])
    
    # Inner product of vectors; both produce 219
    print(v.dot(w))
    print(np.dot(v, w))
    # 219
    # 219
    ```
    
- **Comparison Operators**
    
    we couldn’t use Boolean operators in NumPy like normal variables instead we use Functions: 
    
    ```python
    # for AND we use
    np.logical_and(bmi > 21, bmi < 22)
    bmi[np.logical_and(bmi > 21, bmi < 22)]
    
    # for OR we use
    np.logical_or(bmi > 21, bmi < 22)
    
    # for NOT we use
    logical_not()
    ```
    
- **Random Packages**
    - **to get random values:**
    1. **[ rand() function ]:**
    
    ```python
    import numpy as np
    np.random.rand()
    ```
    
    - we could make the random value consistency by using **seed**
    
    ```python
    np.random.seed(123)   # Starting from a seed
    np.random.rand()
    # it will result the same value every time executed the code
    ```
    
    **example on it:** 
    
    ```python
    import numpy as np
    np.random.seed(123)
    coin = np.random.randint(0,2) # Randomly generate 0 or 1
    print(coin)
    if coin == 0:
    print("heads")
    else:
    print("tails")
    ```
    
    **to print integer number between range of numbers**  
    
    ```python
    # Import numpy and set seed
    import numpy as np
    np.random.seed(123)
    
    # Use randint() to simulate a dice
    print(np.random.randint(1,7))
    ```