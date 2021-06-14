##############################################################################
## NumPy 
##---------------------------------------------------------------------------- 
"""
   * NumPy (or Numpy) is a Linear Algebra Library for Python, the reason it 
     is so important for Data Science with Python is that almost all of the 
     libraries in the PyData Ecosystem rely on NumPy as one of their main 
     building blocks.
 
   * Numpy is also incredibly fast, as it has bindings to C libraries. 
     For more info on why you would want to use Arrays instead of lists, 
     check out this great [StackOverflow post]
     (http://stackoverflow.com/questions/993984/why-numpy-instead-of-python-lists).
 
   * We will only learn the basics of NumPy, to get started we need to 
     install it!

   * Installation Instructions
     - It is highly recommended you install Python using the Anaconda 
       distribution to make sure all underlying dependencies (such as Linear 
       Algebra libraries) all sync up with the use of a conda install. 
     - If you have Anaconda, install NumPy by going to your terminal or 
       command prompt and typing:
           conda install numpy
     
     - If you do not have Anaconda and can not install it, please refer to 
       [Numpy's official documentation on various installation instructions.]
       (http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
"""

###############################################################################
##  Using NumPy
##-----------------------------------------------------------------------------
"""
   * Once you've installed NumPy you can import it as a library.
"""
import numpy as np


"""
   * Numpy has many built-in functions and capabilities. We won't cover them 
     all but instead we will focus on some of the most important aspects of 
     Numpy: vectors, arrays, matrices, and number generation. 
     
   * Let's start by discussing arrays.
"""

###############################################################################
##  Numpy Arrays
##-----------------------------------------------------------------------------
"""
   * NumPy arrays are the main way we will use Numpy throughout the course. 
   
   * Numpy arrays essentially come in two flavors: vectors and matrices. 
     - Vectors are strictly 1-d arrays and matrices are 2-d (but you should 
       note a matrix can still have only one row or one column).
 
   * Let's begin our introduction by exploring how to create NumPy arrays.
"""

"""
   * Creating NumPy Arrays
     - From a Python List
       > We can create an array by directly converting a list or list of lists.
"""



##############################################################################
##  Built-in Methods
##----------------------------------------------------------------------------
"""
   * There are lots of built-in ways to generate Arrays.
   
   * arange()
     - Return evenly spaced values within a given interval.
"""




##############################################################################
##  zeros and ones
##---------------------------------------------------------------------------- 
"""
   * Generate arrays of zeros or ones
"""




##############################################################################
##  linspace
##---------------------------------------------------------------------------- 
"""
   * Return evenly spaced numbers over a specified interval.
"""




##############################################################################
##  eye
##---------------------------------------------------------------------------- 
"""
   * Creates an identity matrix.
"""




##############################################################################
##  Random
##---------------------------------------------------------------------------- 
"""
   * Numpy also has lots of ways to create random number arrays:
     - rand()
       > Create an array of the given shape and populate it with random 
         samples from a uniform distribution over [0, 1)
"""




"""
    - randn()
      > Return a sample (or samples) from the "standard normal" distribution. 
        Unlike rand which is uniform:
"""



"""
    - randint()
      > Return random integers from 'low' (inclusive) to 'high' (exclusive).
"""




##############################################################################
##  Array Attributes and Methods
##---------------------------------------------------------------------------- 
"""
   * Let's discuss some useful attributes and methods or an array.
"""



##############################################################################
##  Reshape
##---------------------------------------------------------------------------- 
"""
   * Returns an array containing the same data with a new shape.
"""



##############################################################################
##  max,min,argmax,argmin
##---------------------------------------------------------------------------- 
"""
   * These are useful methods for finding max or min values. Or to find their 
     index locations using argmin or argmax
"""



##############################################################################
##  Shape
##---------------------------------------------------------------------------- 
"""
   * Shape is an attribute that arrays have (not a method).
"""

##  Vector



##  Notice the two sets of brackets



## dtype
""" 
   * You can also grab the data type of the object in the array.
"""




##############################################################################
##  NumPy Indexing and Selection
##---------------------------------------------------------------------------- 
"""
   * In this lecture we will discuss how to select elements or groups of 
     elements from an array.
"""
import numpy as np

##  Creating sample array


##############################################################################
##  Bracket Indexing and Selection
##----------------------------------------------------------------------------
"""
   * The simplest way to pick one or some elements of an array looks very 
     similar to python lists.
"""
##  Get a value at an index



##  Get values in a range



##############################################################################
##  Broadcasting
##---------------------------------------------------------------------------- 
"""
   * Numpy arrays differ from a normal Python list because of their ability to 
     broadcast.
"""
##  Setting a value with index range (Broadcasting)



##  Reset array, we'll see why I had to reset in  a moment



##  Important notes on Slices



##  Change Slice


##  Now note the changes also occur in our original array!



##  Data is not copied, it's a view of the original array! 
##  This avoids memory problems!

##  To get a copy, need to be explicit



##############################################################################
##  Indexing a 2D array (matrices)
##----------------------------------------------------------------------------
"""
   * The general format is "arr_2d[row][col]" or "arr_2d[row,col]". 
     I recommend usually using the comma notation for clarity.
"""



##  Indexing row



##  Getting individual element value



##############################################################################
##  2D array slicing
##----------------------------------------------------------------------------

##  Shape (2,2) from top right corner



##  Shape bottom row




##############################################################################
##  Fancy Indexing
##---------------------------------------------------------------------------- 
"""
   * Fancy indexing allows you to select entire rows or columns out of order,
     to show this, let's quickly build out a numpy array.
"""
##  Set up matrix


##  Length of array



##  Set up array





##  Fancy indexing allows the following



##  Allows in any order




##############################################################################
##  More Indexing Help
##----------------------------------------------------------------------------
"""
   * Indexing a 2d matrix can be a bit confusing at first, especially when 
     you start to add in step size. 
     
   * Try google image searching NumPy indexing to fins useful images, 
     like this one:
     - <img src= 'http://memory.osu.edu/classes/python/_images/
       numpy_indexing.png' width=500/>
"""

##############################################################################
##  Selection
##---------------------------------------------------------------------------- 
"""
   * Let's briefly go over how to use brackets for selection based off of 
     comparison operators.
"""




##############################################################################
##  NumPy Operations
##----------------------------------------------------------------------------
"""
   * Arithmetic
     - You can easily perform array with array arithmetic, or scalar with 
       array arithmetic.
"""



##  Warning on division by zero, but not an error!
##  Just replaced with nan



# Also warning, but not an error instead infinity




##############################################################################
##  Universal Array Functions
##----------------------------------------------------------------------------
"""
   * Numpy comes with many [universal array functions]
     (http://docs.scipy.org/doc/numpy/reference/ufuncs.html), which are 
     essentially just mathematical operations you can use to perform the 
     operation across the array.
"""
##  Taking Square Roots



##  Calcualting exponential (e^)

