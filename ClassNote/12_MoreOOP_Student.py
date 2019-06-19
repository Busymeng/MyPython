##############################################################################
##  More OOP
##############################################################################

##############################################################################
## Class Standard Methods
"""
   * Encapsulation with classes
     - Classes allow us to hide details from a programmer.
     - Classes are modular/portable as they are self-contained.
     - Classes provide an interface for their use, the methods defined in 
       the class.
       
   * Add the idea of consistency:
     - a new class should be consistent with the rules and syntax of the 
       language
     - a new class should respond to standard methods
"""
##  Import all the names in the Rational module to the main namespaces

# simple rationalNumber class
# wfp, 10/20/07
# wfp updated Py3, naming 4/2/13




##from Rational import *


##############################################################################
## Introspection
"""
   * Concept of overloaded operator
"""
# Addition for integers


# Concatenation for strings



"""
   * type vs isinstance
     - Python provides two operators for determining the type associated
       with a variable: type() or isinstance()
"""



"""
   * Write a simple function that we can use to decide what operation to 
     perform based on type.
"""



##############################################################################
##  Standard Operators
"""
   * Python has two classes of standard operators
     (1) Math operators (+, -, *, /, etc)
     (2) Collection operators ([], iteration, etc)
     
   * How does Python mat "+" to a method?
         V1  +  V2  <===>  V1.__add__(V2)
         
   * Every operator has an associated method as provided by Python. 
     For example:
     - +  :  __add__()
     - -  :  __sub__()
     - All begin and end with two underlines
     - You can only connect an operator to one of the existing methods
     
   * In the calling sequence, the lhs of the operator is used to call 
     the method and the rhs is passed as anoperator
     - Python does this translation automatically.
     - Both forms are exactly equivalent, but the binary operator form
       is more convenient.
       
   * We will be able to initialize, add and print a clock.
     - The __init__() method is for construction.
     - The __add__() allows adding via the + operator.
     - The __str__() operator returns a string from an instance.
       > When a print is called, Python looks for a way to convert the 
         instance to a string, the __str__() method.
     
"""



##############################################################################
##  Introspection and Commutativity
"""
   * Some thing don't quite work with our Clock class.   
"""


"""
   * First Case: c1 + 1
        __add__(self,rhs_clock):
            .....
            ......
            
     The variable rhs_clock is associated with the integer 1.
     When executing rhs_clock.hours, there is no such attribute in an integer.
     We need to fix it.
"""



"""
   * Second Case: 1 + c1
     It is actually:   1.__add__(c1):
     There is no such method in the integer class.
            
     - For every numeric method, there is a method with an "r" prepended
       to the method name: __radd__(), __rsub__(), etc.
     - These "r" methods, "r" is short for reverse argument, are meant to
       handle a case such as this.
       
     - When the initial call, 1.__add__(c1) fails, Python looks to see if
       there exist a method of the form c1.__radd__(1).
       That is, it reverses the arguments and then makes a calls to the
       method.
       
     - If the method does not exist, failure as before.
       If it does exist, the call is made the __radd__() method is invoked
       with arguments already reversed.
       
                                  1.__add__(c1)   --->Fails
         Python will try              X X
         to switch                     X
                                      X X        
         call __radd__()          c1.__radd__(1)         
                        
"""
