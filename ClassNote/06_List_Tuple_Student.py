################################################################
##  List and Tuple
################################################################

################################################################
## List
"""
   * Like strings, they are a collection of elements, in particular a sequence
     of elements, and share a number of charactistics with strings.
     
   * Making a list
     > Use the list() constructor (but only with iterables)
     > Lists the elements between square brackets, separated by commas. 
     
   * With constructor you must provide an iterable as an argument.
     > The constructor makes an list element out of each element of the 
       iterable.
     > You can do this with range() and force the generation of all the range 
       elements and place them in a list.
"""


## Error



################################################################
## What's the same as strings?
"""
   * concatenate/+ (but only on lists)
   * repeat/*
   * indexing with square bracket
   * slicing with square bracket
   * membership with the in operator
   * length using the len() operator
"""




################################################################
## What's the difference from strings?
"""
   * List can contain a mixture of any kind of elements.
   * Lists are mutable, you can change an element in place.
   * Lists have different methods than strings, and because they are mutable, 
     they typically don't return a value.
"""




################################################################
## Some list methods
##  - append(), extend(), remove(), pop(), insert()
##  - reverse(), sort()




## Index and slice assignment



""" 
   * The number of elements, either being replaced or replacing with, do not
     have to match.
   * The replacing elements must be iterable.
"""



## Use list in function


## Simultaneous assignment with list



################################################################
## Fun with the lists
"""
   * Lists are iterable.
   * Lists and the string split() method
"""





################################################################
## sorted() function
"""
   * The list sort() method changes the list (and doesn't return anything).
   * The sorted() return the sorted list and leaves the argument list alone.
"""



################################################################
## Sort a string
"""
   * You cannot directly sort a string, but you can sort a list.
     > We need to be able to convert back and forth between the two.
   * We know how to convert a string to a list, what about list to string.
   * The string join() method is nice.
     > It's a method applied to a particular string.
     > That string is what is put between each element of the list as they
       are joined together.
"""



################################################################
##  List comprehension
"""
   * We often need to iterate through the elements of a list, perform 
     operation(s) on those elements, and store the resulting values 
     in a new list, leaving the original list unchanged.
   * <accumulator> = [<expression> for <item> in <iterable>]
"""




##  List comprehension with files


################################################################
##  Example: getNames(n) enter names by user




################################################################
## Tuples
"""
   * Tuples are yet another collection. They are really a combination of
     a list and a string. 
     > like any collection, you can index, slice, iterate, test membership,
       measure length
     > like a list, a tuple can consist of any combination of data types
     > like a string, a tuple is immutable
     
   * Making a tuple
     > Like any collection, there is a constructor called tuple() which will
       take an iterable and make each element a member of tuple.
     > The shortcut is comma operator.
     > The tuple has parentheses when it is printed. However, the parens are
       not part of the construction. Commas do the construction.
"""



################################################################
## Why tuples?
"""
   * Tuples are basically a way to create a collection that connot be changed.
   * They are often used in functions to return multiple elements.
"""

################################################################
## Tuple example:
"""
   * Text file: bill 1 3 2 5 4
                tom  100 1 2
                fred 10 100 39 2
     - The numbers are all integer.
   * calculate_line: take in a line from the text file, return a tuple of
                     4 elements: name, max, min, avarage
   * Strategy:
     (1) split() the string, by whitespace into a list of strings
         - the name is the first string in the list, grab it
     (2) slice away the name, itrate over the rest and convert each to an 
         integer
         - store each one in a list using append()
     (3) sort the list
         - max is the last element
         - min is the first element
         - the sum() will sum up all elements. The average is the sum divided
           by the length of the list.
"""



## Work with text file as input





################################################################
## Perfect Number example:
"""
   * Given the divisors of an integer number, a number is perfect if 
     the sum of those divisors equals the number itself.
   * Further, if the sum is greater, the number is an abundant number,
     if the sum is smaller, the number is a deficient number.
"""

################################################################
## collect_factors() function
"""
   V1: Take in a number, return a list of its factors:
       - create a list containing one as the only element
       - for the numbers/factors in the range 2 to num-1:
         - if the number is divisible by the factor, remember that factor
           by appending to the list
       - return the factor_list    
   * Note: when the number is larger, the program become slow.
"""



"""
   V2: We only need to check as far as the square root, if we record the
       both factors.
       28 = 1 x 28                36 = 1 x 36
            2 x 14                     2 x 18
            4 x 7                      3 x 12
                                       4 x 9
                                       6 x 6
"""



################################################################
## classify_number() function
"""
   * It takes a number, calls collect_factors() on the number,
     then classifies according to the sum of factors.
   * Return a tuple of two parts: the classification and the list of factors.
   * We can write a main() that calls classify_number() for a whole range of
     numbers, printing the perfects as they occur.
"""




################################################################
## Example: Word Puzzle
"""
   * What do these words have in common?
     - pig, table, cab, real, yet and ride
       cab => 3 1 2 => 3 = 1 + 2
       table => 20 1 2 12 5 => 20 = 1 + 2 + 12 + 5
   * Strategy:
     (1) Association between letters and numbers
     (2) Make list of words in the English language
     (3) Find words that meet criteria
"""



"""
   (1) Association between letters and numbers
"""


"""
   (2) Make list of words in the English language
"""

        
## Check word_list    


"""
   (3) Find words that meet criteria
"""



## Make improvement


## Better display

