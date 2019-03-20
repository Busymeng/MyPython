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
   
   * Linear algebra, Fourier transform, random number capabilities

   * Building block for other packages (e.g. Scipy)

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


##-------------------------------------------------------------------

# save to file

# read from file


#####################################################################
##  Datatypes
##
"""
   * Every numpy array is a grid of elements of the same type. 
   
   * Numpy provides a large set of numeric datatypes that you can use to 
     construct arrays. 
     
   * Numpy tries to guess a datatype when you create an array, but functions 
     that construct arrays usually also include an optional argument to 
     explicitly specify the datatype. 

"""
##-------------------------------------------------------------------



#####################################################################
##  Array math
##
"""
   * Basic mathematical functions operate elementwise on arrays, and are 
     available both as operator overloads and as functions in the numpy module.
"""
##-------------------------------------------------------------------



##-------------------------------------------------------------------
"""
   * We use the dot() function to compute inner products of vectors, 
     to multiply a vector by a matrix, and to multiply matrices. 
     - dot() is available both as a function in the numpy module and 
       as an instance method of array objects.
"""
##-------------------------------------------------------------------


# Inner product of vectors


# Matrix / vector product 



# Matrix / matrix product


##-------------------------------------------------------------------


# Vector Operations


##-------------------------------------------------------------------
"""
   * Operations along axes
"""
##-------------------------------------------------------------------




#####################################################################
##  Broadcasting
##
"""
   * Broadcasting is a powerful mechanism that allows numpy to work with 
     arrays of different shapes when performing arithmetic operations. 
     
   * Frequently we have a smaller array and a larger array, and we want to 
     use the smaller array multiple times to perform some operation on the 
     larger array.
"""
##-------------------------------------------------------------------


##-------------------------------------------------------------------
# Real Numpy broadcasting
"""
   * Rule of broadcasting
     1. If the arrays do not have the same rank, prepend the shape of the 
        lower rank array with 1s until both shapes have the same length.
     2. The two arrays are said to be compatible in a dimension if they have 
        the same size in the dimension, or if one of the arrays has size 1 in 
        that dimension.
     3. The arrays can be broadcast together if they are compatible in all 
        dimensions.
     4. After broadcasting, each array behaves as if it had shape equal to 
        the elementwise maximum of shapes of the two input arrays.
     5. In any dimension where one array had size 1 and the other array had 
        size greater than 1, the first array behaves as if it were copied 
        along that dimension
   
"""
##-------------------------------------------------------------------






#####################################################################
##  Other Matrix Operations
##
"""
   * import numpy.linalg
       eye(3)              #Identity matrix
       trace(A)            #Trace
       column_stack((A,B)) #Stack column wise
       row_stack((A,B,A))  #Stack row wise
     
   * Linear Algebra
       import numpy.linalg
       qr           Computes the QR decomposition
       cholesky     Computes the Cholesky decomposition
       inv(A)       Inverse
       solve(A,b)   Solves Ax = b for A full rank
       lstsq(A,b)   Solves arg minx kAx − bk2
       eig(A)       Eigenvalue decomposition
       eig(A)       Eigenvalue decomposition for symmetric or hermitian
       eigvals(A)   Computes eigenvalues.
       svd(A, full) Singular value decomposition
       pinv(A)      Computes pseudo-inverse of A
     
   * Fourier Transform
       import numpy.fft
       fft  1-dimensional DFT
       fft2 2-dimensional DFT
       fftn N-dimensional DFT
       ifft 1-dimensional inverse DFT (etc.)
       rfft Real DFT (1-dim)
       ifft Imaginary DFT (1-dim)
     
   * Random Sampling
       import numpy.random
       rand(d0,d1,...,dn)       Random values in a given shape
       randn(d0, d1, ...,dn)    Random standard normal
       randint(lo, hi, size)    Random integers [lo, hi)
       choice(a, size, repl, p) Sample from a
       shuffle(a)               Permutation (in-place)
       permutation(a)           Permutation (new array)
       
   * Distributions in Random
       import numpy.random
       The list of distributions to sample from is quite long, and includes
       beta
       binomial
       chisquare
       exponential
       dirichlet
       gamma
       laplace
       lognormal
       pareto
       poisson
       power
"""
##-------------------------------------------------------------------

