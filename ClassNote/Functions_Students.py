# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:29:41 2018

@author: Michael Meng
"""

###############################################################
##  Functions
"""
  Advantages of function:
    > Even before writing any code, functions allow a hierarchical approach 
      to thinking about and solving the problem.
    > After determining the functions that are appropriate for a solution, 
      these functions can be implemented, tested, and debugged, individually.
    > Functions provide modularization (or compartmentalization).
    > Functions facilitate code reuse.
    
  Ways to use the funtions:
    > A function may be called for the value it returns.
    > A function may be called solely for its side effects. A side effect 
      is an action the function takes that does not produce a return value.
    > A function may be called both for its side effects and its return value.
"""

###############################################################
##  void Functions and None
"""
    > The print() function produces output, but in fact, it's a void function.
    > If a function doesn’t explicitly return data and yet it is used in an 
      expression, the function evaluates to None.
    > It may not be obvious at the moment, but the values returned by 
      functions will be extremely important in much of what we will do later.
"""



###############################################################
##  Create void Functions
"""
    def <function_name>(<parameter_list>):
        <body>
        
"""

# Create Hello-World function that takes no parameters.


# Create function to greet a user.



# Calculation of BMI using a void function. Here all input and output are 
# handled within the function bmi().



###############################################################
##  Create non-void Functions
"""
    def <function_name>(<parameter_list>):
        <body>
        return statement
        
"""

# Function to calculate a batting average given the number of
# hits and at-bats.


# See what sort of help we get on this function. Not much...


# Function to calculate change.


# Try to get help on this function. "Docstring" is given!



# Reimplementation of the BMI calculation where the calculation itself has 
# been separated from the handling of the input and output.



###############################################################
##  Scope of variables
"""
    > All the parameters and variables that are defined in a function are 
      local to a function, meaning that these variables cannot be “seen” by 
      code outside of the function.
        
"""



# Another demonstration of the local scope of variables within a function.



# Demonstration of a way in which a function can be used to change the value 
# of an int variable. Here one must assign the return value of the function 
# back to the variable.




###############################################################
##  Scope of functions
"""
    > It is also possible to define a function within the body of another. 
    > When this is done, the inner function can only be invoked from within 
      the function in which it was defined. Thus the scope of the inner 
      function is local to the outer function.
        
"""

# Demonstration that one function can be defined within another. 
# However, when this is done, the scope of the inner function is restricted to
# the outer function in which it was defined.




###############################################################
##  Scope of functions
"""
    > print() and return are fundamentally different and a failure to 
      understand how they differ can lead to errors.
        
"""

# Demonstration of the difference between a function that prints a value and 
# one that returns the same value.



# Demonstration that print() and return statements can appear in the 
# same function.




###############################################################
##  Using the main() Function
"""
    > The programmers create a main() function and often call this in the 
      final line of code in the program. Thus, after all the functions have 
      been defined, including main() itself, the main() function is called.
            
"""




###############################################################
##  Optional Parameters
"""
    > print() can take a variable number of parameters, and it also accepts 
      optional parameters.
    > The optional parameters are sep and end which specify the string used 
      to separate arguments and what should appear at the end of the output, 
      respectively.
            
"""

# Demonstration of the use of the sep and end optional parameters for print().

# Separator defaults to a blank space.


# Explicitly set separator to string "-*-".


# Issue two separate print() statements. (Multiple statements can
# appear on a line if they are separated by semicolons.)
# By default, print() terminates its output with a newline.


# Override the default separator and line terminator with the
# optional arguments of sep and end.



# Function demonstration



# Function to raise a given number to an exponent. 
# The exponent is an optional parameter.




# Function to calculate the y value for a straight line given by y = mx + b. 
# The value of x must be given. However, m and b are optional with default 
# values of 1 and 0, respectively.
































