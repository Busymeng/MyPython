#####################################################################
##  Ch9 Quiz
##
"""
   1.   Python lists are indexed using integers and dictionaries can use 
        strings as indexes
   2.   Associative arrays
   3.   The program would fail with a traceback
   4.   -1
   5.   False
   6.   Building a histogram counting the occurrences of various strings in 
        a file 
   7.   counts[key] = counts.get(key,0) + 1
   8.   It loops through the keys in the dictionary
   9.   values()
   10.  To provide a default value if the key is not found
    
"""

#####################################################################
##  Assignment 9.4
##

"""
   * Write a program to read through the mbox-short.txt and figure out who 
     has sent the greatest number of mail messages. The program looks for 
     'From ' lines and takes the second word of those lines as the person who 
     sent the mail. The program creates a Python dictionary that maps the 
     sender's mail address to a count of the number of times they appear in 
     the file. After the dictionary is produced, the program reads through 
     the dictionary using a maximum loop to find the most prolific committer.
     
"""



