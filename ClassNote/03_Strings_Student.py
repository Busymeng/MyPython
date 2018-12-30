################################################################
##  Strings
################################################################

################################################################
## Introduction to Strings
"""
   * Strings
     > It is a collection type. A collection has more than one single item
       stored in it.
     > No character type in Python.
     > A string is a sequence.
       >> A sequence is a more restrictive type.
       >> Every sequence has a sequence number or index associated with each
          element.
       >> There is an ordering of the elements of a string.
     > Not all collections are sequences, but every sequence is a collection. 
"""


## Escape sequences:
"""
   * \n : carriage return or new line
   * \t : tab
   * \' : single quote
"""


## Some string methods:
"""
   * length : len()
   * + and *
   * Membership : in
"""


## String Indexing
"""
   * a_string[i] - indexing starts at 0; negative indexing starts from end
   * a_string[x:y] - a slice from index x up to but not including index y
   * a_string[x:y:z] - a slice from index x up to but not including index y
                       with step z
   * Defaults: no x , start slicing at beginning; no y, end slice at the end
   * a_string[::-1] - reverse of a_string
   * a_string[:] - the whole string
   * Elements in a string are individual characters but still treated as 
     a string.
"""



## Strings are immutable.
"""
   * Collections can be nutable and immutable.
     > Immutable - you can NOT change any element
     > Mutable - you CAN change any element
   * You can create a new string to include the change.
"""

## String Methods
"""
   * Use dir("") to see all string methods.
   * String method is invoking by calling it in the context of a string object.
     > string object
     > a "dot" (period)
     > the name of method
     > parenthesis contains any arguments or none
   * "". + tab => can see all available methods
"""



## String Comparison
"""
   * Each character has an associated integer in a particular encoding.
     > UTF-8 encodes many characters
     > ASCII table
     > (0~9) < (A~Z) < (a-z)
   * Reference: Python doc Ch4.7.1
"""


## String Format
## "a string here with some {}".format()



## More control in {}
""" 
   {format_element:align width.precision type}
   
   > format_element: could be a name or number
   > align: < (left) ^ (center) > (right)
   > width: how many spaces occupied
   > precision: for floating point number and rounding
   > type: s (sting) d (decimal integer) f (Floating-point decimal)
           e (floating-point exponential) % (floating-point as percent)

"""



## Floating-point specification
##   {:totalspace.precisionf}  ==> {:8.2f}
##
## Reference: https://pyformat.info/



## Print a pretty table




################################################################
## Iteration: repitition using for
"""
   * Use for loop for string collection.
     > The for statement iterates over all the elements of a collection,
       any collection, one at a time and sets a variable of the user's 
       choosing to each element as iteration proceeds.
       
       for item in sequence:
           statements
           
"""



## A range of integers
"""
   * We can generate a second sequence, a seuence of integers, using the 
     range() function.
   * range() takes 3 arguments:
     > A start integer. If omitted it is assumed to be 0.
     > An end integer. This is required.
     > A step integer. If omitted, it is assumed to be 1.
"""    




################################################################
## Other useful functions with for loop and string
"""
   * enumerate()
     > Enumerate was created so you don't need to worry about creating and
       updating the count variable.
   * zip()
     > Use to combine two sequences in tuples list form
     > It works based on shorter sequence
   * ord()
     > It takes a string of length one, i.e., a single character, and 
       returns the corresponding ASCII value.
   * chr()
     > It takes an integer argument and produces the corresponding character.
           
"""

    
    
################################################################
## Text encryption and decryption 
##   Using ord(), chr() and zip()

## Version 1: key list
    

   
 ## Version 2: Clear words





################################################################
## Examples using string and for
"""
   (1) Let's SHOUT!
       Write a program that converts every lowercase character to an 
       upperase character.
"""


## Do it in a program (upper.py)

        


################################################################
## Examples using string and for
"""
   (2) Palindromes
       > A palindrome is a string that is the same forwards and backwards.
       > Case is ignored as are non-alphabetic and non-numeric characters.
         "Madam, I'm Adam"  --> "madamimadam"
"""

## Ways to convert
"""
   * lower() the string. Save the original.
   * The string package has a number of pre-initialized strings in it.
     > string.ascii_lowercase and string.digits --> find "good" characters
     > string.whitespace and string.punctuation --> find "bad" characters
"""


## Another way: Dump the "bad" characters


## Palindrome check!
"""
   (1) Index method
       > Compare the first and last character using indices.
       > If they are not the same, not a palindrome.
       > If they are the same, then move up one index from front, and
         dwon one index from the back, and repeat.
       > Done when we get to the middle.
"""

    
    
"""
   (2) Slice method
       > Compare the first and last character using indices.
       > Then use slicing to move those characters if they match.
       > Keep going untile a difference occurs or you run out of string.
"""


"""
   (3) Reverse way
       > Reverse the string and compare it to the converted string.     
"""
   

        