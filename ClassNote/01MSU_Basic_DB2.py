################################################################
##  Basics
################################################################

################################################################
## Program Elements
"""
   * What is a type? It is a form of data that defines two things:
     > the internal structure of data
     > the operation that you can perform on the data
     
   * Four simple types:
     > integers
     > floating point numbers
     > strings
     > boolean
     
   * Integers
     > Numbers without decimal points
     > Offical name: int
     > An integer has no limit on its size.
     
   * Float
     > Numbers with decimal points
     > Offical name: float
     > A floating point number is not an exact representation, 
       but an approximation.
       
   * Strings
     > strings are asequence of characters, with delimiters either 
       double quotes "" or single quotes ''
     > Offical name: str
     > Need the pair of same delimiters
   
"""
type(10)
type(10.0)
type("abc")
type('123.0')
type(True)

## Converting between different data types
## Using int(), float(), str()
a = int('10')
b = float('10')
b = float("10.2') # Wrong!
b = float(20)
a = int(22.1)
a1 = int("22.1")  # Wrong!

n = str(20)
type(n)
n = str(56.90)

################################################################
## Functions
"""
   * It can perform a side-effect.
   * It can provide a return value.
"""

int(21)
print(21)

a = int(90.8)
c = print(90)

################################################################
## Assignment
"""
   * Assignment operator ( = ): associate a name with a value
   * The use of equal sign doen not signify equality.
"""
a = 2
a = a + 1

d = d + 1

################################################################
## Namespace
"""
   * Assignment creates a data structure called a namespace.
          my_int = 7  ==>  Name   -> my_int
                           Value  -> 7
"""


################################################################
## Python name rules
##  1. First letter > a-z, A-Z
##  2. Other letters > a-z, A-Z, 0-9, _
##  3. Case sensitive
##  4. No keywords

1a = 10
a1 = 10
a12 = 10
a12_ = 90
a12-u = 90

print(10)
f = print
f(90)
print(123)


## Other name rule
##  1. lower with under  > my_name
##  2. under with type   > my_int


################################################################
## Math operators
##  +, -, *, /, 



## Special operators
##  1. // > Integer division



##  2. %  > Modulus - Remainder operator




## Floating-point operation




## Mixed numeric types
##  - Python only works for same types



## Order of operation




## The math module
##  - A module is a Python file and its associated operators and variables.



## Continuation
##  - Continue a single line across multiple lines using the backslash (\)



## Some codes
##  - round()



## work with math operators



















