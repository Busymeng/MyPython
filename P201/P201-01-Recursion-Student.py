##############################################################################
##  Introduction to Recursion
##############################################################################

##############################################################################
##  Calculating the Sum of a List of Numbers
##----------------------------------------------------------------------------
"""
   * An iterative function that computes the sum.
     - The function uses an accumulator variable (theSum) to compute a 
       running total of all the numbers in the list by starting with 0 
       and adding each number in the list.
"""



##----------------------------------------------------------------------------
"""
   * We can use the following sequence of simplifications to compute a 
     final sum.
     
     total= (1+(3+(5+(7+9))))
        total= (1+(3+(5+16)))
            total= (1+(3+21))
                total= (1+24)
                    total= 25
                    
   * We might say the the sum of the list numList is the sum of the first 
     element of the list (numList[0]), and the sum of the numbers in the 
     rest of the list (numList[1:]).
     
     listSum(numList) = first(numList) + listSum(rest(numList))
"""


##############################################################################
##  Three Laws of Recursion
##----------------------------------------------------------------------------
"""
   * all recursive algorithms must obey three important laws:
     - A recursive algorithm must have a base case.
     - A recursive algorithm must change its state and move toward the 
       base case.
     - A recursive algorithm must call itself, recursively.
"""

##############################################################################
## Recursion vs Iteration
"""
   * Factorial: 4! = 4 * 3 * 2 * 1  (Iterative thinking)
   
   * Factorial: (Recursive thinking)
       4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! = 4 * 3 * 2 * 1
"""
##----------------------------------------------------------------------------



##############################################################################
##  Converting an Integer to a String in Any Base
##----------------------------------------------------------------------------





##############################################################################
##  Head and Tail Recursion
##----------------------------------------------------------------------------
"""
   * Tail recursion is memory efficiency.
   
   * Head recursion is NOT memory efficient.
     - Recursive call is not finished so we stack memory to hold the states.
"""



## Example using tail and head recursion together


##############################################################################
##  Factorial and Stack Memory
##----------------------------------------------------------------------------
"""
   * Tail recursion is memory efficiency.
   
   * Head recursion is NOT memory efficient.
     - Recursive call is not finished so we stack memory to hold the states.
"""





##############################################################################
##  Fibonacci Problem
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






print(gcd(500, 420)) # 20


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



print(rangeSum(10,15)) # 75


##----------------------------------------------------------------------------
## listSum()
##----------------------------------------------------------------------------



print(listSum([2,3,5,7,11])) # 28


##----------------------------------------------------------------------------
## power()
##----------------------------------------------------------------------------



print(power(2,5)) # 32


##----------------------------------------------------------------------------
## interleave()
##----------------------------------------------------------------------------



print(interleave([1,2,3],[4,5,6]))  # [1,4,2,5,3,6]



##############################################################################
## Divide-and-Conquer Examples
##----------------------------------------------------------------------------
##----------------------------------------------------------------------------
## rangeSum()
##----------------------------------------------------------------------------



print(rangeSum(10,15)) # 75


##----------------------------------------------------------------------------
## listSum()
##----------------------------------------------------------------------------



print(listSum([2,3,5,7,11])) # 28



##############################################################################
## Multiple Base/Recursive Case Examples
##----------------------------------------------------------------------------
##----------------------------------------------------------------------------
## power()
##----------------------------------------------------------------------------



print(power(2,5)) # 32
print(power(2,-5)) # 1/32 = 0.03125


##----------------------------------------------------------------------------
## interleave()
##----------------------------------------------------------------------------



print(interleave([1,2],[3,4,5,6])) # [1,3,2,4,5,6]




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



print(rangeSum(10, 15))




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





luhn_sum(2)
luhn_sum(12)
luhn_sum(42)
luhn_sum(138743)
luhn_sum(5105105105105100)
luhn_sum(4012888888881881)
luhn_sum(79927398713) 



##----------------------------------------------------------------------------
"""
   * Permutations
"""
##----------------------------------------------------------------------------


 
print(permutations([1,2,3]))




##############################################################################
## Recursive Tree
##----------------------------------------------------------------------------





##############################################################################
## Sierpinski Triangle
##----------------------------------------------------------------------------


