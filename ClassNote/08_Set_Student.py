################################################################
##  Sets
################################################################

################################################################
## Essential ideas about set
"""
   * Two interesting features of a set
     - You can store only one example of an element in a set. No duplicates
       are allowed. Attemps to store a duplicate is ignored.
     - Special set operators (like union, intersection, etc) are possible
       on a set.
"""


################################################################
## Creating a set
"""
   * Use {} like a dictionary, but only if the values are not key:value pairs
     (no colon in the elements).
   * The set() constructor can create a set from any iterable. 
"""



## Empty set is essential
"""
   * You can't create an empty set with {}, as that is an empty dictionary.
   * Empty set is made with set()
"""




################################################################
## Basic Features about Set
"""
   * It is a mutable data structure.
   * It allows for storage of mixed types.
   * It likes a dictionary that is not a sequence.
     - There is no order to a set.
     - Unlike a dictionary, there is no [] operation of any kind on a set.
"""


################################################################
## Set Operations
"""
   * len() for length
   * in: membership
   * Intersection: &
   * Union: |
   * Difference: - (order is important)
   * Symmetric difference: ^ (opposite of intersection)
   * Subset: <
   * Superset: >
   * Others: add(), discard(), clear(), remove()
"""


################################################################
## Set Application: Common and Unique Words in Documents
"""
   * Lets' look at two documents, the Gettysburg Address and the Declaration
     of Independence and look for:
     - common words in both documents
     - unique words in both documents
     - maybe some other fun stuff
"""

##  Recycling get_words() from the word frequency example
"""
   * We wrote a function get_words() that collected the words of a text file
     into a dictionary.
   * We are going to use that code and change it slightly to gather sets of
     unique file words.
"""


################################################################
## More about Comprehension
"""
   * Comprehensions are a convenient way to build collections.
   
   * One of the most common tasks we as Python programmers need to do is:
     - examine every element of a data structure (a list, a dictionary, a set)
     - perform some operation on each element
     - collect the resulting elements together into another data structure
     
   * Python has a group of shortcuts called comprehension which make the 
     process easier.
     - while shortcuts are short, they can make things more difficult to read
     - if you do things the long way, that's fine. Shortcuts are something
       you can pick up as you become more experienced.
     - One good thing about comprehensions. They are fast. If performance ever 
       become an issue, a comprehension version of the same code is typically
       a lot faster.
   
"""

################################################################
## General Comprehension
"""
   * A Comprehension has 4 parts:
     - what kind of data structure is going to be generated (indicated by the
       enclosing elements).
     - what expression is being collected.
     - what is being iterated over.
     - an optional condition that determines if an element is collected.   
     
     [element**2 for element in my_list if element%2==0]
     
"""



################################################################
## Set and Dictionary Comprehension
"""
   * Enclose the comprehension in curly braces {}.
     - You make a dictionary if the elements are key:value pairs.
     - You make a set if you just collection elements.
     
"""




################################################################
## Ternary operator
"""
   * The expressions you collect in your comprehensions have to be just 
     expressions.
     - These are Python statements r=that return a value. That exclude control
       statements as things to collect.
       
   * However, at least for very simple selection alternatives, there is a
     special form of an if expression called a ternary (meaning three parts)
     expression.
     - It is in fact an expression and returns one of two values depending
       on the condition.
       
       "Hi Mother" if age_int > 18 else "Hi Mom"
     
"""


