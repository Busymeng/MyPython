##############################################################################
##  Recursion
##############################################################################

##############################################################################
## What is Recursion?
"""
   * "A journey of a thousand miles begins with a single step." Lao Tzu
   
   * Recursion examples:
     - Droste Effect: 
       > https://en.wikipedia.org/wiki/Droste_effect
       > https://www.google.com/search?q=droste+effect&tbm=isch
     - Fractals:
       > https://en.wikipedia.org/wiki/Fractal
       > https://www.google.com/search?q=fractal&tbm=isch
       > https://www.youtube.com/watch?v=G_GBwuYuOOs&feature=youtu.be
   
   * Recursion is simple: it is a function that calls itself.
        def f(n):
            ......
            f(n-1)
            
   * Understanding recursion implies understanding two parts of your problem:
     - How to break your problem into smaller pieces, each of which can be 
       addressed by your function and then “put back together”
     - Determining when the recursive invocation of a function ends, when the 
       recursion “bottoms out”
       
   * Correctly controlling recursion requires dealing with two different cases. 
     - The first case terminates a recursive sequence and is known as the 
       base case. 
       > If the base case is missing, the recursive function calls go on 
         forever. 
     - The second case is the recursive step. 
       > It both breaks the problem down and reassembles the partial solutions.
"""

##############################################################################
## General Recursive Form
"""
   def recursiveFunction():
       if (this is the base case):
           # no recursion allowed here!
           do something non-recursive
       else:
           # this is the recursive case!
           do something recursive
           
"""

##############################################################################
## Recursion vs Iteration
"""
   * Factorial: 4! = 4 * 3 * 2 * 1  (Iterative thinking)
   
   * Factorial: (Recursive thinking)
       4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! = 4 * 3 * 2 * 1
"""
##----------------------------------------------------------------------------



##----------------------------------------------------------------------------
"""
   * Find the reverse of a string.
     - Show how to trace a recursive function.
       1. Python Tutor
       2. Handwritten work.
"""
##----------------------------------------------------------------------------





##----------------------------------------------------------------------------
"""
   * Find the Greatest Common Divisor between 2 integers.
"""
##----------------------------------------------------------------------------



##----------------------------------------------------------------------------
"""
   * Find the sum of any digit number.
     - 2016 = 2 + 1 + 0 + 6 = 9
"""
##----------------------------------------------------------------------------




##############################################################################
## Basic Recursion Examples
##----------------------------------------------------------------------------
##----------------------------------------------------------------------------
## rangeSum()
##----------------------------------------------------------------------------



##----------------------------------------------------------------------------
## listSum()
##----------------------------------------------------------------------------



##----------------------------------------------------------------------------
## power()
##----------------------------------------------------------------------------



##----------------------------------------------------------------------------
## interleave()
##----------------------------------------------------------------------------
 


##############################################################################
## Divide-and-Conquer Examples
##----------------------------------------------------------------------------
##----------------------------------------------------------------------------
## rangeSum()
##----------------------------------------------------------------------------



##----------------------------------------------------------------------------
## listSum()
##----------------------------------------------------------------------------




##############################################################################
## Multiple Base/Recursive Case Examples
##----------------------------------------------------------------------------
##----------------------------------------------------------------------------
## power()
##----------------------------------------------------------------------------


##----------------------------------------------------------------------------
## interleave()
##----------------------------------------------------------------------------





##############################################################################
## Recursive Debugging
##----------------------------------------------------------------------------
"""
   * Debugging recursive code can get tricky! 
     - We can make it easier by keeping track of the recursion depth 
       using a parameter, then adjusting the print based on that depth.
     - We'll make the parameter optional (giving it a starting value) 
       so that it doesn't need to be included when the function is called.
"""





##############################################################################
## Using Multiple Recursive Calls
##----------------------------------------------------------------------------
"""
   * fibonacci
"""
## First Attemp
##    Note: as written, this function is very inefficient!
##    (We need to use "memoization" to speed it up! See below for details!)



## Once again, printing call stack using recursion depth.



## Finally, not duplicating code




##############################################################################
## Mutual Recursion
"""
   * Functions call each other.
   * Luhn Algorithm:
     - Used to verify credit card numbers.
     - https://en.wikipedia.org/wiki/Luhn_algorithm
     - First:
       > From the rightmost digit, which is the check digit, moving left,
         double the value of every second digit; if product of this doubling 
         operation is greater than 9 (e.g., 7*2 = 14), then sum the digits
         of the products (e.g. 10 = 1+0 = 1, 14 = 1+4 = 5)
       > Second: Take the sum of all digits. The Luhn sum of a valid credit
         card number is multiple of 10.
"""
##----------------------------------------------------------------------------





##----------------------------------------------------------------------------
"""
   * Permutations
"""
##----------------------------------------------------------------------------





##############################################################################
## Recursive Tree
##----------------------------------------------------------------------------



##############################################################################
## Sierpinski Triangle
##----------------------------------------------------------------------------


