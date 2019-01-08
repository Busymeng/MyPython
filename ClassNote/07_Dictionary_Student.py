################################################################
##  Dictionaries
################################################################

################################################################
## Dictionary
"""
   * A dictionary is a data structure that is also referred to as a map or 
     an associative array.
     > The basic idea is that a dictionary records a pair of elements called 
       a key:value pair.
       
   * A dictionary function will use the key as a way to lookup the associated 
     value.
     
   * Stuff about the dictionary:
     > A Python dictionary is like a paper dictionary. You can search for 
       a key (the word) and find the associated value (the definition).
     > However, you can NOT search for value only.
     > A dictionary is a collection but not a sequence. 
       - There is no order to a dictionary.
       - There is no index to find an element at a particular 
         sequence location.
     > A dictionary is a mutable data structure. You can change it in place.
     > Dictionaries are work with any combination of types except 
       for one restriction.
       - The key must be an immutable datatype (string, tuple).
"""


################################################################
## Making Dictionaries
"""
   * Use {} to enclose key:value pair.
   
   * Use the dict() function to record a sequence of tuples, particularly
     with the zip() function.
     > The zip() function takes two iterables and interleaves them as a tuple.
     > The result is an iteration object which we can use as an argument
       to list to see the result.
       
   * Use the dict() function with named arguments.
     > If we use keyword arguments, the key is the argument and the assigned
       value is the key value.
"""



################################################################
## Accessing/Assignment Keys from a  Dictionary
"""
   * We do use square brackets with dictionaries, but the index value
     is a key, not a sequence number.
     > The result of a key index is the associated value of the pair, or
       a KeyError if the key does not exist.
       
   * Dictionaries are mutable and we can assign a value to a key via 
     key index:
     > if the key exists, its value is updated and the dictionary is change 
       in place
     > if the key does not exist, the key is added to the dictionary with
       the specified value
"""



## Special Dictionary Methods
"""
   * Theses methods return a special type, a view of the dictionary.
   * They can be used to iterate over the dictionary or can be shown
     explicitly with a list.
"""    



    
## Multiple Assignment




################################################################
## Dictionary Application: Word Frequency
"""
   * Main Ideas:
     The dictionary will store words as keys and counts as values.
     > We will process each word of the file and use it as a key in the
       dictionary.
       - Processing of the word means that we need to convert each word to
         lower case and strip any punctuation from the word so that we can
         compare like words.
       - It should be the case that 'it', 'It' and 'it,' count as the
         same word.
     > We will use each word as a key in the dictionary.
       - If the key/word does not exist in the dictionary, we will give
         is a value count of 1
       - If the key/words does not exist in the dictionary, we will increase
         its count by 1
     > At the end, we will print out the frequency list in both alphabetic
       and frequency order.
       
   * Supplement file: "gburg.txt"
"""

## Main function
"""
   * Open a file for reading.
   * Fill the dictionary with the words by calling a function.
   * Print out the dictionary in alphabetic order by calling two functions
"""



## get_words() function


    
## print_alphabetic() function
"""
   * Takes in the updated dictionary and prints out the words in alphabetic
     order
   * Return nothing
   
   * Essential ideas:
     > We can not sort a dictionary but we can sort a list.
     > We collect all the key:value pairs as a list of tuples
     > Sort the list.
     > Print it out in columns.
     > Could the sorted() function help us?
"""
    

    
    
################################################################
## Dictionary Example
"""
   * Benford's law: (first-digit law)
     - It refers to the frequency distribution of digits in many real-life
       sources of data.
     - In the distribution, the number 1 occurs as the leading digit about
       30% of the time, while larger number occur in that position less
       frequently.
     - 9 as the first digit is less than 5% of the time.
     
   * Use "population_data.txt"
"""    

