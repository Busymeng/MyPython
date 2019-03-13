#####################################################################
##  Introduction to NumPy Arrays
##
"""
   * NumPy is a Python module designed for scientific computation.
   
   * NumPy arrays are n-dimensional array objects.
     - They are used for representing vectors and matrices.
     - NumPy arrays have a size that is fixed when they are constructed.
     - Elements of NumPy arrays are also all of the same data type leading 
       to more efficient and simpler code than using Python's standard 
       data types.
   * np.zeros(), np.ones(), np.empty()

"""
##-------------------------------------------------------------------


##-------------------------------------------------------------------


##-------------------------------------------------------------------


##-------------------------------------------------------------------


##-------------------------------------------------------------------




#####################################################################
##  Slicing NumPy Arrays
##
"""
   * With one-dimension arrays, we can index a given element by its position, 
     keeping in mind that indices start at 0.

   * With two-dimensional arrays, the first index specifies the row of the 
     array and the second index specifies the column of the array.
     
   * With multi-dimensional arrays, you can use the colon character in place 
     of a fixed value for an index, which means that the array elements 
     corresponding to all values of that particular index will be returned.
     
   * For a two-dimensional array, using just one index returns the given row 
     which is consistent with the construction of 2D arrays as lists of lists, 
     where the inner lists correspond to the rows of the array.

"""
##-------------------------------------------------------------------



#####################################################################
##  Indexing NumPy Arrays
##
"""
   * NumPy arrays can also be indexed with other arrays or other 
     sequence-like objects like lists.
     
   * Index can be defined as a Python list, but we could also have defined 
     that as a NumPy array.
     
   * When you slice an array using the colon operator, you get a view of 
     the object.
     - This means that if you modify it, the original array will 
       also be modified.
     - This is in contrast with what happens when you index an array, 
       in which case what is returned to you is a copy of the original data.

"""
##-------------------------------------------------------------------


##-------------------------------------------------------------------



##-------------------------------------------------------------------





#####################################################################
##  Building and Examining NumPy Arrays
##
"""
   * To construct an array of 10 linearly spaced elements starting with 0
     and ending with 100, we can use the NumPy linspace function.
     
   * To construct an average of 10 logarithmically spaced elements between 
     10 and 100, we can use the NumPy logspace command.

"""
##-------------------------------------------------------------------



##-------------------------------------------------------------------



##-------------------------------------------------------------------



# Finds whether x is prime

 