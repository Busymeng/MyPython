################################################################
##  Functions
################################################################

## Functions
"""
   * A function perform a task and often returns a value.
   * The function details are hidden from us.
     > We can reuse the operation easily, without re-entering a lot of 
       complex code.
     > It makes our code easier to read.
     > Once it is proven correct we can reuse it with confidence.
"""




## Example: Celsius to Farenheit conversion function

## 1. Define a function


## 2. Call/Invoke a function


## 3. Flow of information
"""
   1> Call associates argument a_temp with parameter temp
   2> Control transfers to c2f()
   3> Suite of function is evaluated, stops with return
   4> result returned, function ends, control pass back to caller
"""

## Full Example
## Convert and return


## Make a pretty display

    
## Run everything



#################################################################
## Example: Make changes
"""
   Calculate the change in terms of dollars, quarters, dimes, nickels, 
   and pennies in ’total’ pennies.
"""






################################################################
##  Passing: Argument to Parameter
"""
   * Arguments are passed to parameters in sequence
   * But what exactly get 'passed' - it's passing by value.
"""





"""
   * Default parameter value
"""



################################################################
##  Function Namespace
"""
   * Every function defines its own namespace when it runs.
   * A namespace is an association between names and objects.
   * Passing associates an argument and a parameter with the same object
     through two namespaces: the calling namespace and the function namespace
   * If you update a parameter locally, you only update it in the 
     local namespace.
"""



################################################################
##  Palindrome Function
"""
   * In Python, we use time module to measure the running time of a program.
   * It will return the current time in seconds since the Epoch.
   * Epoch is a fancy way of saying a measurement of time from some fixed
     point: January 1st, 1970 at hour 0
   * Though the result may come in 1/100000 of a second, the accuracy is 
     probably 1/10 of a second.
"""



## Make Palindrome Functions
"""
   * We need to make some palindromes to test the efficiency of functions.
     1> Generating a big string. Make multiple copies of string.ascii_letters
     2> Make a reverse copy of the string.
     3> Concatenate the forward and reverse version to guaranteed 
        a palindrome.
"""


## Palindrome checking functions
"""
   (1) Walker
   (2) Slicer
   (3) Reverser
"""




################################################################
##  Example: Palindrome Odometer
"""
   * Driving along, Terry notices that the last 4 digits on the odometer are
     palindrome.
     > A mile later, the last 5 digits are palindrome.
     > A mile later, the middle 4 digits are palindrome.
     > One mile after that, all 6 digits are palindrome.
     What was the odometer reading when Terry first looked at it?
"""

## Create the right 6 digits format
## "123" --> "000123"





## Make it more readable by making a new function
