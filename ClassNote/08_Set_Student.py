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
