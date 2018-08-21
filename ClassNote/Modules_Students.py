# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:48:41 2018

@author: Michael Meng
"""


## Obtain a list of everything built into Python


## In the following, the integer variable z and the function f() are defined. 
## When the dir() function is called with no arguments, we see these together 
## with various items Python provides. Calling dir() with an argument of 
## builtins provides a list of all the functions built into Python.


## Use of an import statement to gain access to the methods and attributes of 
## the math module.
"""
    > By issuing import math statement we create a module object named math. 
      The “functions” we want to use are really methods of this object.
    > Technically a module is a single Python .py file while a package is 
      a directory containing multiple modules. To the programmer wishing to 
      use the module or package, the distinction between the two is 
      inconsequential.
"""



##########################################################################
## Introduction to Complex Numbers
##
"""
   > Complex numbers are extremely important in a wide range of problems in 
     math, science, and engineering.
"""

## Demonstration of the use of complex numbers.
## Create complex number z1.


## Check z1’s type.


## Check z1.


## Set j to 10.


# Create integer z2 -- not complex!


## Check z2.


## Attempt to create complex number z3.


## Correct way to create complex number z3.


## Sum of complex numbers.


## Product of complex numbers.




## The methods and attributes associated with a complex number.


# The real part of z.


# The real imaginary part of z.


# Magnitude of z.


# Simpler way to obtain magnitude.


##########################################################################
## Complex Numbers and the cmath Module
##
"""
   > How do we calculate the square root or cosine of a complex number?
   > If a programmer needs to have complex functions at his or her disposal, 
     they should import the cmath module.
   > If one needs to import multiple modules, one either writes multiple 
     import statements or writes a single import statement with the modules 
     separated by commas.
     >> import math, cmath
     or
     >> import math
        import cmath
   > We can import a module as some other identifier.
     >> import math as realmath
"""

## Attempt to use complex numbers with functions from the math module.


# z1 has zero real part and imaginary part of 1.

 
# z1 squared is negative 1.



# Cannot use math.sqrt() on a complex number.



# Cannot use math.cos() on a complex number.



## Demonstration of the cmath module which provides support for complex 
## numbers.



## Example of importing multiple modules with a single statement and using 
## alternate identifiers for the modules.


# Real function, integer argument.

 
# Complex function, integer argument





##########################################################################
## Importing Selected Parts of a Module
##
"""
   > Often there is no reason to import all the methods and attributes 
     contained in a module.
   > Import a single object.
     >> from <module> import <object>
   > Import a single object and assign to an alternative name.
     >> from <module> import <object> as <ident>
   > Import multiple objects.
     from <module> import <object1>, <object2>, ..., <objectN>
   > Import multiple objects and assign to alternative names. The as qualifier 
     may be omitted as appropriate.
     >> from <module> import <object1> as <ident1>, ..., <objectN> as <identN>
"""

## Demonstration of an import statement that employs from to select 
## individual objects for importation.




## Attempt to import the sqrt() function from both the math and cmath modules.


## Right way to import with from





##########################################################################
## Importing an Entire Module Using *
##
"""
   > Python allows you to import everything from a module if, in a from-import 
     statement, you simply write an asterisk for the object you want to import. 
     The asterisk serves as a “wildcard,” meaning everything.
"""

# Import everything from the math module.



# Cosine of pi / 2 is zero. But, because of finite precision, the
# result isn’t exactly zero (but it’s close!).





##########################################################################
## Importing Your Own Module
##
"""
   > A module is simply a .py file. 
   > We can easily create our own modules that contain a collection of 
     functions or other objects.
"""

## Code used to demonstrate importing a module of our own.
"""
This module contains two functions and one globally defined
integer.
Sae the file as "my_mod.py"
"""





## Importation and use of the module
"""
    > Python needs to find your module in order to import it.
    > On Windows machine:
        C:\Python32\Lib\site-packages
    > On Mac machine:
        /Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/
        site-packages
    > On Debian/Ubuntu Linux machine:
        /usr/lib/python3.2/dist-packages
"""




"""
    > Alternatively, one can modify where Python searches for modules. 
    > The directories where Python searches for modules are collectively 
      known as the path. One of the places Python always looks is what 
      is known as the “current working directory” (cwd).
"""





## Rather than changing the working directory, one can modify the path over 
## which Python searches for modules.

