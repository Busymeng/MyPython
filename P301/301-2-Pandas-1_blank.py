##############################################################################
##  Introduction to Pandas
##---------------------------------------------------------------------------- 
"""
   * We will learn how to use pandas for data analysis. 
     You can think of pandas as an extremely powerful version of Excel, 
     with a lot more features. 
     
   * We will cover:
     - Series
     - DataFrames
     - Missing Data
     - GroupBy
     - Merging,Joining,and Concatenating
     - Operations
     - Data Input and Output
"""
##############################################################################
##  Series
##----------------------------------------------------------------------------
"""
   * The first main data type we will learn about for pandas is the Series 
     data type. Let's import Pandas and explore the Series object.
   
   * A Series is very similar to a NumPy array (in fact it is built on top of 
     the NumPy array object). 
   
   * What differentiates the NumPy array from a Series, is that a Series can 
     have axis labels, meaning it can be indexed by a label, instead of just 
     a number location. 
     
   * It also doesn't need to hold numeric data, it can hold any arbitrary 
     Python Object.
"""
import numpy as np
import pandas as pd

##  Creating a Series
##  You can convert a list,numpy array, or dictionary to a Series:

##  Using Lists



##  NumPy Arrays


##  Dictionary


##  Data in a Series
"""
   * A pandas Series can hold a variety of object types.
"""


##  Even functions (although unlikely that you will use this)


## Using an Index
"""
   * The key to using a Series is understanding its index. 
   * Pandas makes use of these index names or numbers by allowing for fast 
     look ups of information (works like a hash table or dictionary).
"""


##  Operations are then also done based off of index:



##############################################################################
##  Data Selection in Series
##----------------------------------------------------------------------------

# <1> Series as dictionary



# <2> Series as 1-D array

# slicing by explicit indexing


# slicing by implicit indexing

# masking


# fancy indexing



# <3> Indexers: loc, iloc, and ix

# Potential indexing confusion



# explicit index when indexing



# implicit index when slicing


# loc --> allows indexing and slicing always refer explicit index


# iloc --> allows indexing and slicing always refer implicit index


# ix --> hybrid of loc and iloc, for Series objects is equivalent
#        to standard []-based indexing


##############################################################################
##  DataFrames
##---------------------------------------------------------------------------- 
"""
   * DataFrames are the workhorse of pandas and are directly inspired by 
     the R programming language. 
     
   * We can think of a DataFrame as a bunch of Series objects put together 
     to share the same index. 
     
   * DataFrame as a generalized NumPy array.
   
   * DataFrame as a specialization of Python Dictionary
"""
import pandas as pd
import numpy as np

##  Ways to construct DataFrame



# <1> From a single Series object



# <2> From a list of dicts


# <3> From a dictionary of Series objects



# <4> From a 2-D NumPy array



# <5> From a NumPy structured array





##############################################################################
##  The Pandas Index Object
##---------------------------------------------------------------------------- 
"""
   * This Index object is an interesting structure in itself, and it can be 
     thought of either as an immutable array or as an ordered set 
     (technically a multiset, as Index objects may contain repeated values).
"""
# <1> Index as immutable array



# <2> Index as ordered set





##############################################################################
##  DataFrame Selection and Indexing
##---------------------------------------------------------------------------- 
"""
   * Let's learn the various methods to grab data from a DataFrame. 
"""


##  Pass a list of column names


##  SQL Syntax (NOT RECOMMENDED!) --> it does not work for all cases


##  DataFrame Columns are just Series


##  Creating a new column


##  DataFrame as 2-D array



##  Removing Columns


##  Not inplace unless specified!


##  Can also drop rows this way:


##  Selecting Rows


##  Or select based off of position instead of label 


##  Selecting subset of rows and columns 




##############################################################################
##  Operating on Data in Pandas
##---------------------------------------------------------------------------- 
"""
   * Index Preservation
     - Because Pandas is designed to work with NumPy, any NumPy ufunc will 
       work on Pandas Series and DataFrame objects.
"""


"""
   * If we apply a NumPy ufunc on either of these objects, the result will 
     be another Pandas object with the indices preserved
"""



"""
   * Index Alignment
     - For binary operations on two Series or DataFrame objects, Pandas will 
       align indices in the process of performing the operation.
"""
#  (1) Index alignment in Series


"""
   * This index matching is implemented this way for any of Python’s built-in 
     arithmetic expressions; any missing values are filled in with NaN by 
     default.
"""



"""
   * If using NaN values is not the desired behavior, we can modify the fill 
     value using appropriate object methods in place of the operators.
"""



#  (2) Index alignment in DataFrame



#  Fill with the mean of all values in A (which we compute by first stacking 
#  the rows of A)



"""
   * Mapping between Python operators and Pandas methods
         +  add()
         -  sub(), subtract()
         *  mul(), multiply()
         /  truediv(), div(), divide()
         // floordiv()
         %  mod()
         ** pow()
"""

#  (3) Operations Between DataFrame and Series


"""
   * According to NumPy’s broadcasting rules, subtraction between a 
     two-dimensional array and one of its rows is applied row-wise.
"""




##############################################################################
##  Conditional Selection
##---------------------------------------------------------------------------- 
"""
   * An important feature of pandas is conditional selection using bracket 
     notation, very similar to numpy.
"""



##  For two conditions you can use | and & with parenthesis:



##############################################################################
##  More Index Details
##---------------------------------------------------------------------------- 
"""
   * Let's discuss some more features of indexing, including resetting the 
     index or setting it something else. 
     
   * We'll also talk about index hierarchy.
"""


##  Reset to default 0,1...n index




##############################################################################
##  Missing Data
##---------------------------------------------------------------------------- 
"""
   * Real-world data is "rarely" clean and homogeneous.
   
   * Different data sources may indicate missing data in different ways.
     - We’ll refer to missing data in general as null, NaN, or NA values.
     
   * Two strategies to handle missing data: 
     - using a mask that globally indicates missing values, or 
     - choosing a sentinel value that indicates a missing entry.
     
   * In the masking approach, the mask might be an entirely separate Boolean 
     array, or it may involve appropriation of one bit in the data 
     representation to locally indicate the null status of a value.
     
   * In the sentinel approach, the sentinel value could be some data-specific 
     convention, such as indicating a missing integer value with –9999 or 
     some rare bit pattern, or it could be a more global convention, such as 
     indicating a missing floating-point value with NaN (Not a Number), 
     a special value which is part of the IEEE floating-point specification.
     
   * Trade-Offs in Missing Data Conventions
     - Use of a separate mask array requires allocation of an additional 
       Boolean array, which adds overhead in both storage and computation. 
     - A sentinel value reduces the range of valid values that can be 
       represented, and may require extra (often non-optimized) logic in CPU 
       and GPU arithmetic. Common special values like NaN are not available 
       for all data types.
       
   * Pandas chose to use sentinels for missing data, and further chose to 
     use two already-existing Python null values: the special floating point
     NaN value, and the Python None object.
"""
import numpy as np
import pandas as pd

##  (1) None: Pythonic missing data





##  (2) NaN: Missing numerical data



##  (3) NaN and None in Pandas



##  (4) Operating on Null Values
"""
   * Pandas treats None and NaN as essentially interchangeable for indicating
     missing or null values. 
     
   * To facilitate this convention, there are several useful methods for 
     detecting, removing, and replacing null values in Pandas data structures.
     - isnull() ==> Generate a Boolean mask indicating missing values
     - notnull() ==> Opposite of isnull()
     - dropna() ==> Return a filtered version of the data
     - fillna() ==> Return a copy of the data with missing values filled or 
                    imputed
"""
## Detecting null values



## Dropping null values


"""
   * We cannot drop single values from a DataFrame; we can only drop full 
     rows or full columns.
     
   * Depending on the application, you might want one or the other, so
     dropna() gives a number of options for a DataFrame.
"""



## Filling null values

# forward-fill

# back-fill




