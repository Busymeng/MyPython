##############################################################################
##  Python Decorator
##############################################################################

##############################################################################
##  What is a Decorator?
##############################################################################
"""
   * A typical decorator is a function that takes a function as an argument, 
     and returns another function. 
     
   * Python has a special syntax to apply decorators to functions, through 
     a @my_decorator line above the function def.
"""



##----------------------------------------------------------------------------


##----------------------------------------------------------------------------




##############################################################################
##  A typical decorator with an inner() function
##############################################################################
"""
   * Typically, a decorator has an inner() function that is defined inside it. 
   
   * This inner() function then calls the original, decorated function, 
     and adds some functionality to it.
     
   * To illustrate this concept, let's define a @mapper decorator that changes 
     a function that takes a single value into a function that takes a list 
     (or other iterable) of values, applies the original function to each of 
     the values, and returns the result as a list.
     
   * Because a decorator replaces the decorated function by another function,
     the docstring and other properties of the original function are lost. 
     
   * To avoid this, you can decorate the inner() function using functools.wraps.
"""


##----------------------------------------------------------------------------


##----------------------------------------------------------------------------


##----------------------------------------------------------------------------



##############################################################################
##  Reusing Decorators
##----------------------------------------------------------------------------
"""
   * A decorator is just a regular Python function. We can move the decorator 
     to its own module that can be used in many other functions.
"""
##  Put the following function in a "decorator.py" file

##----------------------------------------------------------------------------


##############################################################################
##  Using built-in decorators in functools module 
##----------------------------------------------------------------------------



##############################################################################
##  Decorator with arguments
##############################################################################
"""
   * In some cases, you want the decorator itself (rather than the decorated 
     function) to accept arguments.

   * To create a decorator that accepts arguments, you need to create a 
     'meta-decorator' function that takes arguments and returns a regular 
     decorator, which in turns returns a function. 
     
   * So there are three layers of functions!

   * To create a decorator that can accept arguments, but also works without, 
     you have to inspect whether the first argument to the decorator is a 
     callable (e.g. a function); if so, then act as regular decorator; 
     if not, then act as a meta-decorator.
     
   * All of this sounds more complicated then it is.
"""
##  What is happening?



##----------------------------------------------------------------------------
##  We need to modify the do_twice() in decoDemo module

##----------------------------------------------------------------------------



##############################################################################
##  Other example 
##----------------------------------------------------------------------------


##---------------------------------------------------------------------------
##  Add decorator
##---------------------------------------------------------------------------




##---------------------------------------------------------------------------
##  Add decorator with arguments
##---------------------------------------------------------------------------




##---------------------------------------------------------------------------





##############################################################################
##  Returning Values from Decorated Functions
##############################################################################
"""
   * What happens to the return value of a decorated functions? It's up to 
     the decorator to decide.
"""
