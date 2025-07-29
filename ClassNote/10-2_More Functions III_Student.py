#############################################################################
##  Higher-Order Function
##---------------------------------------------------------------------------
"""
   * Using Function - Don't Repeat Yourself (DRY)
   
   * Purpose of higher-order functions
     - Functions are first-class: 
       Functiona can be manipulated as values in our programming language.
     - Higher-order function:
       A function that takes a function as an augument or return as a
       return value.
       - Express general methods of computation
       - Remove repetition from program
       - Separate concerns among functions
"""
"""
   * Make a function with 2 positive numbers and return whether the 2 numbers 
     have same number of digits
"""


    

## DRY




# Generalizing patterns using arguments
"""
   * Get the area of a circle, a square and a hexagon.
     - Find the common structure allows for shared implementation
"""



## If we want to make sure the value of r is positive.
"""
   * assert r>0 --> May need to add to all three functions.
     - this is DRY
 
   * Generalize the three examples by factoring out the part that they have
     in common.
"""






# Generalizing over computational process
"""
   * The common structure among functions may be a computational process, 
     rather than a number.
   
   * Use function as argument
"""




# Another approach




## We can also define function in another way




# Local function definitions; returning functions



#############################################################################
##  args and kwargs
##---------------------------------------------------------------------------
"""
   * We can specify a function that takes arbitrary arguments and keyword
     arguments. We can do this with argument unpacking.
    
   * args is a tuple of its unnamed arguments and kwargs is a dict of its 
     named arguments. 
     - It works the other way too, if you want to use a list (or tuple) and 
       dict to supply arguments to a function.
"""



"""
   * We want to create a higher-order function that takes as input 
     some function f and returns a new function that for any input 
     returns twice the value of f.
"""




# does not work for more arguments



# use args and kwargs to do the help

