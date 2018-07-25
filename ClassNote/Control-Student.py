# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:09:09 2018

@author: Michael Meng
"""

################################################################
## Booleans and Logical Operations
##
##  - Booleans are data that have values Ture or False.
##  - Good for making decisions.
##  - Official name: bool


## Relational operators
##  <, <=, >, >=, ==, !=


##  == check whether two names refers to objects that have same value
##  is check whether two names refers to the same object (same ID)



## Chained comparison


## Floating-point number comparison


## True and False
##  - Any value in Python can be used as a Boolean.
##  - Every type has an empty value, this is equivalent to False.
##  - Every other value is equivalent to True.
##  - False value in various type:
##      => o in int
##      => 0.0 in float
##      => "" in str

## Short-Circuiting


## "and" has higher precedence than "or"




################################################################
## Selection (Decision)
##
##   if boolean_expression :
##      suite (statements)


##  another example


##  Selection with if..else
##
##    if boolean_expression:
##       suite 1 (True)
##    else:
##       suite 2 (False)



##    if boolean_expression1:
##       suite 1 
##    elif boolean_expression2:
##       suite 2
##    elif boolean_expression3:
##       suite 3
##    else:
##       suite last



##  Nested if





################################################################
## Repetition using while
##
##   while boolean_expression:
##      suite (statements)



##  Factorial example
##     n! =  1            when n=0
##        =(n-1)!*n       whne n>0



##  Compound assignment, += and their friends



##  while loop with else
##   - The else clause id work being done as the loop finishes normally


##  Early exit - break
##   - Skips all remaining loop statements and immediately halts the loop
##   - Skips any else statements as part of the loop


##  Changing iteration - continue
##   - Cause the current iteration of the loop to end early, it will
##      => Skip any remaining lines in the while suite
##      => Goes to the top of the loop and re-evaluate the boolean

##    while boolean1:
##        stmt1
##        stmt2
##        if boolean2:
##            break            ## Leave the loop suite, skip the else
##        if boolean3:
##            continue         ## Stop this iteration, go to boolean1
##        stmt3
##        stmt4
##    else:
##        else-suite
##    print("Moving on")



##  Nested while loop
##   - A while loop inside another while loop

##   - It is important when you initialize the variable (inner=0)
##   - If break were executed in the inner loop, it would only break
##     out that particular suite, namely back to the outer loop suite.




################################################################
## Example using if and while
##
##   Solve the puzzle substituting unique, non-zero integers
##     for each letter.
##
##         HERE
##       +  SHE
##      --------
##        COMES

## Using Brute-Force to solve the problem.

## <1> Try to generate all possible digits for 3-digit => A, B, C
##     - Make sure they are unique

    
## <2> Apply the idea to solve the problem


    
    
##################################################################
## fizzbuzz problem
##
##  - Write a program that prints the numbers from 1 to 100.
##  - But for multiples of three print “Fizz” instead of the number and
##      for the multiples of five print “Buzz”.
##  - For numbers which are multiples of both three and five print “FizzBuzz”

























