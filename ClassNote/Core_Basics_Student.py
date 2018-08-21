# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:56:27 2018

@author: Michael Meng
"""

###############################################################
##  Literals and Types
"""
    + int literal - 23
    + float literal - 34.8, 1e0
    + string literal - "abc", 'ABC'
    + bool literal - True, False
    
    + ints are stored exactly in the computer 
    + floats are only stored approximately
    + Using the type() function to determine the type of various literals. 
"""


###############################################################
##  Expressions, Arithmetic Operators, and Precedence
"""
    > 5 + 4 => 
    > 5 + 4. => 
    > 2 % 5 => 
    > 2 // 5 => 
"""


###############################################################
##  Statements and the Assignment Operator
"""
    > The equal sign in Python does not mean the same thing as in math!
    > x = 7
    > y = x
    > x = 9   ==> y = ?
    
    > x = 10
    > x = x + 1
    
    > x = 7
    > y = " abc"
    > type(x), type(y)  ==> ?
    > x = x + 3.14
    > y = 12 * 2
    > type(x), type(y)  ==> ?
"""


###############################################################
##  Cascaded and Simultaneous Assignment
"""
    > z = y = x = 2 + 7 + 2
    > x, y , z   ==> ?
    > Cascaded assignments can make the code somewhat harder to read 
      and thus should be used sparingly.
      
    > Simultaneous assignment can change the way we implement an algorithm.
    > x , y = 10, "I am John"
    > x, y = y, x    ==> x=? y=?
"""


###############################################################
##  Multi-Line Statements and Multi-Line Strings
"""
    > Constructing multi-line statements by either escaping the 
      newline character at the end of the line or by using parentheses.
    > x = 3 + \
          4
    > y = ( 3 + 4 *
            12 + 5)
    
"""



###############################################################
##  Identifiers and Keywords
"""
    > A valid identifier starts with a letter or an underscore
      and then is followed by any number of letters, underscores, and digits. 
    > No other characters are allowed. 
    > Identifiers are case sensitive.
    
    > There are also keywords (sometimes called reserved words) 
      that have special meaning and cannot be used as an identifier.
      
    > Only in the interactive environment, a single underscore (_) 
      is equal to the value of the most recently evaluated expression.
    
"""


###############################################################
##  Names and Namespaces
"""
    > The assignment serves to associate the value with the name.
    > Within your computer’s memory, Python maintains what are known as 
      namespaces.
    > A namespace is used to keep track of all the currently defined names 
      (identifiers) as well as the objects associated with these names.
    > In Python a name can, at different points in a program, be associated 
      with values of different type.
    
"""


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


# Prompt for multiple values. Must separate values with a comma.


























