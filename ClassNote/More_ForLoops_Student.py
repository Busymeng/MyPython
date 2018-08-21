# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:15:17 2018

@author: Michael Meng
"""

########################################################################
##  More For-loops
##

## Nested for-loops that generate seven lines of integers.
"""
    1
    12
    123
    1234
    12345
    123456
    1234567
"""



## A triangle of ampersands generated using a single for-loop or 
## nested for-loops. The implementation with a single loop takes advantage 
## of Python’s string repetition capabilities.
"""
    &
    &&
    &&&
    &&&&
    &&&&&
    &&&&&&
    &&&&&&&
"""



## An “inverted triangle” realized using a single for-loop.
"""
    &&&&&&&
    &&&&&&
    &&&&&
    &&&&
    &&&
    &&
    &
"""




## An inverted triangle of ampersands is combined with an upright triangle 
## of integers to form a rectangular structure of characters.
"""
    &&&&&&&1
    &&&&&&12
    &&&&&123
    &&&&1234
    &&&12345
    &&123456
    &1234567
"""




## Pyramid of integers that is constructed with an outer for-loop and 
## two inner for-loops.
"""
          1
         121
        12321
       1234321
      123454321
     12345654321
    1234567654321
"""




## Function to display the row and column indices for a two-dimensional 
## table or matrix where the row and column numbers start at zero.




########################################################################
##  Lists of lists
##

## Demonstration of nesting of one list as an element of another.



## Nesting of multiple lists inside a list. Here the list produce consists of
## lists that each contain a string as well as either one or two integers. 
## The contents of a list may span multiple lines since an open bracket 
## serves as a multi-line delimiter in the same way as an open parenthesis.


## Creation of a list within a list within a list.




## Demonstration of the use of multiple brackets to access an element of a 
## nested list.




## A function to display the make and list of models of a car manufacturer.


## Function to display the elements of lists that are nested within 
## another list.



################################################
## Simultaneous Assignment and lists of lists

## Demonstration of “unpacking” a list that contains an embedded list. 
## Simultaneous assignment is used to assign the elements of the toyota list 
## to appropriately named variables.



## A function to display a list of artists in which each element of the 
## artists list contains an artist’s name and a list of songs.


# Create a list of artists.




## Demonstration of simultaneous assignment used in the header of a for-loop. 
## This sets the value of two loop variables in accordance with the contents 
## of the two-element lists that are nested in the iterable (i.e., nested in 
## the list shoes).




## Demonstration that tuples and lists behave in the same way when it comes 
## to nesting and simultaneous assignment in for-loop headers.


    

# Create a tuple of tuples.




########################################################################
##  References and list Mutability
##

## Demonstration that when a list is assigned to a variable, the variable 
## serves as a reference (or alias) to the underlying data in memory.



## As demonstrated in the following, although two variables may initially 
## be aliases for the same underlying data, if one of the variables is 
## assigned new data, this will not affect the original data.




## Demonstration that changes to a list that occur inside a function are 
## visible outside the function.





########################################################################
##  Strings as Iterables or Sequences
##

## Explicit indexing used to access the characters of a string. 
## As with tuples and lists, the index represents the offset from the 
## beginning.



## Use of a for-loop and explicit indexing to loop over all the characters 
## in a string.


## Demonstration of negative indexing for a string. Elements of a tuple or a 
## list can also be accessed using negative indexing.



## Demonstration of slicing a string.



## Demonstration that a slice can be used to obtain an independent copy of 
## an entire list.




## Demonstration of slicing where the increment is provided as the third term 
## in brackets.



## Demonstration that out-of-range values can be given for a slice 
## but cannot be given for an individual item in a sequence.




## A modified version of doubler() that returns a new list.



## Demonstration of list comprehension in which a new list is produced 
## where the value of its elements are twice that of an existing list.


# Use list comprehension to obtain a new list where the values are
# twice that of mylist.




## Demonstration of the use of explicit indexing within list comprehensions.





































