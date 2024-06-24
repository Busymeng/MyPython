##############################################################################
##  01 - Basics
##############################################################################

##############################################################################
##  What is Python Programming Language?
"""
   * Why we call it as "Language"?
     - What do we need to create a "Language"?
       + Vocabulary
       + Grammer (Rules)
       
   * We will learn the "vocabulary" and "grammer" of Python language.
   
   * What does the program do?
     - Process Data
       + Convert Data
       + Calculate Data
       
   * What kind of data existed in the physical world?
     - Numeric data
     - Text data
     
   * All programming language will define the data types to match the physical
     world data in order to process the data.
     - In Python:
       + Nemeric Data -> int, float
       + Text Data -> str
       + Logic Data -> bool
       
   * Every thing in program always obey the following rules:
     - Define -> Use
     - How to Use depends on How to define
     - All the program statements are either "define" statement or 
       "use" statement
"""
##############################################################################
## Program Elements
"""
   * What is a data type? It is a form of data that defines two things:
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
     
   * In Python, the term “object” is quite to catch-all; including numbers, 
     strings of characters, lists, functions - a Python object is essentially 
     anything that you can assign to a variable. 
     - That being said, there are different types of objects: Python treats 
       integers as a different type of object than a string, for instance.

   * The different object types have manifestly different purposes and thus 
     have different built-in functions available to them. 
     
   * The built-in function "isinstance()" will allow us to check if an object 
     is of a given type. 
     - You can also use the built-in "type()" function to check an object’s type. 
   
"""



## Converting between different data types
## Using int(), float(), str()




##############################################################################
## Functions
"""
   * It can perform a side-effect.
   * It can provide a return value.
"""




##############################################################################
## Assignment
"""
   * Assignment operator ( = ): associate a name with a value
   * The use of equal sign doen not signify equality.
"""





##############################################################################
## Python name rules
##  1. First letter > a-z, A-Z, _
##  2. Other letters > a-z, A-Z, 0-9, _
##  3. Case sensitive
##  4. No keywords



## Other name rule
##  1. lower with under  > my_name
##  2. under with type   > my_int


##############################################################################
## Math operators (+, -, *, /)
"""
   * Python operates on the same data type data.
   
   * Note the behavior of "/".
"""




## Special operators
##  1. // > Integer division - Get Quotient


##  2. %  > Modulus - Remainder operator


## Floating-point operation


## Order of operation



## The math module
"""
   * A module is a Python file and its associated operators and variables.
"""



## Continuation
##  - Continue a single line across multiple lines using the backslash (\)


## Some codes
##  - round()
"""
   * Here are examples that illustrate how calling the round() function with 
     no second argument, it returns an int. 
   * The second argument indicates how many significant digits to the right 
     of a decimal point so a non-zero second argument will return a float. 
   * Python uses "round to nearest, ties to nearest even": When the value you 
     intend to round off is a five, you MUST look at the previous value. 
     - If it is even, you round down. 
     - If it is odd, you round up. 
     - It is called round half to even.

"""


"""
   * If precise decimal arithmetic is required, especially for financial 
     calculations, you should use the decimal module, which provides a 
     Decimal data type for decimal floating-point arithmetic with exact 
     precision.
"""


## work with math operators


###############################################################
##  Additional Arithmetic Operators
"""
    > Exponentiation: **
    > Floor division: //
    > Modulo and divmod(): %
                           divmod(x,y) ~ x // y, x % y 
    > Augmented Assignment: +=, -=, *=, /=, //=, %=
"""


 

###############################################################
##  Input and Type Coversion
"""
    > input() always returns the user’s input as a string
    > Type conversion: int(), float(), str()
    > Evaluating Strings: eval()
    > The eval() function takes a string argument and evaluates that string 
      as a Python expression.
"""



# Using eval() we can accept all kinds of input...


# Prompt for multiple values. Must separate values with a comma.
