# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 14:40:49 2018

@author: Michael Meng
"""

###############################################################
##  Lists
"""
    > In Python a list is created when comma-separated expressions are 
      placed between square brackets.
"""

# lists can be assigned to a variable and returned by a function.



# Another demonstration of the creation of a list. Here we see that after a 
# list has been created, subsequent changes to the variables used in the 
# expressions for the elements do not affect the values of the list.
# Create a list x that depends on the current values of a and b.



# Modify a and b and then confirm that this does not affect x.




###############################################################
##  List Methods
"""
    > Because list is a class, the objects in this class will have various 
      methods and attributes which can be listed using the dir() function.
"""

# Demonstration of list concatenation, the len() function, and some of the 
# methods available for lists.

# Concatenate two lists.


# Determine length.


# Show methods and attributes of the list class.


# Sort list.



# Append value to list.



# Sort list again.



# Create an empty list.



# Append value to empty list.



# Extend z with the values from another list.




# Demonstration of the way in which append() differs from extend(). 
# append() appends a single object to a list whereas extend() appends all 
# the objects from the given iterable to the list.




###############################################################
##  For loops
"""
    for <item> in <iterable>:
        <body>
"""

# Demonstrations showing how a for-loop can be used to access each of the 
# elements of a list.



# Initialize a counter.




###############################################################
##  Indexing
"""
    > The first element of a list has an index of zero.
"""

# Demonstration of the use of indexing to access individual elements of a list.


# First element.


# Second element.


# Third element.


# Length of list.

 
# Last element.




# Demonstration that the elements of a list can be accessed using direct 
# indexing and a for-loop. The loop variable is set to an integer in the 
# range of valid indices for the list of interest.





# Demonstration of the use of the range() function in the context of for-loops. 
# The last four loops show how the elements of a list can be conveniently 
# accessed with the aid of the range() function.



    
# Create a list of toppings and display in order.


    
    
# Have index go in descending order to show list in reverse.


   
    
# Have loop variable take on values in ascending order, but
# use this to calculate index which yields list in reverse order.


    
    
# Obtain first and third topping (indices 0 and 2).




###############################################################
##  Mutability, Immutability, and Tuples
"""
    > A list is mutable which merely means we can change it.
    > One difference between a tuple and a list is that a tuple is created 
      by enclosing the comma separated data in parentheses.
    > Python will use parentheses to represent a tuple whether or not
      they were present when the tuple was created.
    > Tuples are immutable, meaning their values cannot be changed.
"""

# Demonstration of the mutability of a list.

# Create list of integers.


# Change second element.


# See what x is now.


# Change last element to a string.




# Demonstration of the use of tuples.




# Demonstration of the immutability of a tuple and how a tuple can be 
# converted to a list.

# Create three-element tuple.



# Cannot change a tuple.



# Convert tuple to a list.




###############################################################
##  Nesting Loops in Functions
"""
    def <function_name>(<parameter_list>):
        <function_body_before_loop>
            for <item> in <iterable>:
                <for_loop_body>
            <function_body_after_loop>
"""

# Flawed implementation of a function where the goal is to show a specified 
# number of multiples of a number that the user enters.





# Another flawed implementation of a function where the goal is to show a 
# specified number of multiples of a given value.





# Function with statements before and after the nested for-loop. 
# This implementation properly obtains input from the user prior to the 
# for-loop and returns the desired value after the for-loop has ended.





###############################################################
##  Simultaneous Assignment with Lists
"""
    > In Python a list is created when comma-separated expressions are 
      placed between square brackets.
"""

# Demonstration that lists, like tuples, can be used in simultaneous 
# assignment statements.

# Tuple to right, without parentheses.



# Tuple to right, with parentheses.



# List to right.




# Demonstration that simultaneous assignment can be used with any data type 
# including entire lists and tuples.

# Assign a list of strings to p.



# Assign a tuple of integers to n.



# Print p and n.

 

# Simultaneous assignment to swap p and n.



# See what p and n are now.



# Define string.



# Print variables.

 

# Swap variables.



# Print variables again.




## Function to create a list of strings where each string is entered by the 
## user.






## Function to calculate the series 1+(1/2)+(1/3)+...+(1/N) 
## The variable total serves as an accumulator.




## Demonstration of a function to calculate the numbers in the Fibonacci 
## sequence.
"""
   fib(0) = 0, fib(1) = 1, fib(2) = 1, ..., fib(N) = fib(N-1) + fib(N-2)  
"""



## An alternative implementation of the Fibonacci sequence that does not use 
## simultaneous assignment.

















































