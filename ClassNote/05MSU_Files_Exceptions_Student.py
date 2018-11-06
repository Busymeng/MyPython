################################################################
##  Files
################################################################

## What is a File?
"""
   * A file is data stord on some media (hard disk, DVD, USB, "cloud").
   * It is usually perminent (or at least long standing) and generally slow 
     to get to.
   * Files generally come in two "flavors":
     > Text files: Files whose contents we can turn into strings using UTF-8
                   or ASCII.
     > Binary files: File with data that are not strings. (game file)
"""

## Connection Programs to the World: Streams
"""
   * We need to create a connection between our program and some external 
     device (file, console, network, etc.) so we can read and write 
     information.
   * These connections are often called streams. 
   * The open() function create a file object representing the connection to 
     a file. It has two mode: "r" for reading, "w" for writing.
     > When opening for reading.
       >> the file is assumed in the same place that you store the 
          Python program. 
       >> If Python cannot find the file it is an error.
       >> Use read(), readline(), readlines() to read the file.
     > When you open for writing.
       >> If the file does not exist, it is created in the same place as the
          Python program that is running.
       >> If it does exist, the file's present contenta are wiped. 
          So be careful.
"""

## Usually, make sure the data files are in the same directory with program



## If the data file is not in the same folder


## Different ways to read the file contents
##  - read(): read the whole contents as a string
##  - tell(): stream position
 


##    - readline(): read the file contents line by line


##    - readlines(): read the file contents as a list


## All strings for Text Files
"""
   * All access, both reading and writing of text files, is via strings
     through the created file object.
   * line_str is a string end with "\n" character.
"""



## The String .strip() Method
"""
   * The .strip() method removes whitespace ('\n','\t',etc) at either end
     of a string.
"""



## Write to the file


## Close Your Files
"""
   * When you are finished wih a file, you should close the file object.
     This makes sure that the information on the file and in your program
     are in sync.
"""



## Demo Example




################################################################
##  Exceptions
################################################################

## What is Exception?
"""
   * Exceptions provide a new type of control that is useful for checking the
     validity of input, e.g., valid filename, valid floating-point number,...
   * You try some code and if a particular error is raised, you handle it
     (in the except suite).
     
          try:
              suite of statements
          except ErrorType1:
              suite of statements
          except ErrorType2:
              suite of statements
              
   * Python's default behavior is to stop processing when an error occurs
     and indicate something about the error.  
   * It would be better if we, as programmers, could "catch" these errors
     when they occur and if possible, handle them (instead of quitting).
   * If we can "fix" the error and continue the program, that would be 
     much better.
"""


## Errors
"""
   * Python has a list of errors, with very particular names, that indicate
     the kind of failure that migh have occurred.
   * Error names are formatted in "CamelCase".
     - Exception: A base class for most error types
     - AttributeError: Raised by syntax obj.foo, if obj has no member named foo
     - EOFError: Raised if “end of file” reached for console or file input
     - IOError: Raised upon failure of I/O operation (e.g., opening file)
     - IndexError: Raised if index to sequence is out of bounds
     - KeyError: Raised if nonexistent key requested for set or dictionary
     - KeyboardInterrupt: Raised if user types ctrl-C while program is 
       executing
     - NameError: Raised if nonexistent identifier used
     - StopIteration: Raised by next(iterator) if no element
     - TypeError: Raised when wrong type of parameter is sent to a function
     - ValueError: Raised when parameter has invalid value (e.g., sqrt(−5))
     - ZeroDivisionError: Raised when any division operator used with 0 
       as divisor
"""



## try-except information flows
"""
   * If try block completes (no errors), skip all the excepts and carry on
     with rest of the program.
   * If an error occurs in the try block. Stop processing at the offending
     line and look for an except of correct error type.
     > Error type exists --> run the code
     > Not exist --> do the normal Python action.
"""


    


## Example:
"""
   * Read the file "tobe.txt", count the words, and then write the count to
     the file "tobeOut.txt"
"""
## Build the basic structure to open a file with exception




## We can try to add loops to make user enter the right file name



## Now do the work.
## Check the file can be read correctly.



## Do the REAL work




## Write the final result to a file



##################################################################
##  Poker Hands Example
"""
   * C1-suit, C1-rank, C2-suit, C2-rank, C3-suit, C3-rank, C4-suit, C4-rank, 
     C5-suit, C5-rank, hand rank
   * Rank Name                    Description
      9   Royal flush       {Ace, king, queen, jack, ten} + flush
      8   Straight flush    Straight + flush
      7   Four of a kind    Four equal ranks within five cards
      6   Full house        Pair + different rank three of a kind
      5   Flush             Five cards with the same suit
      4   Straight          Five cards, sequentially ranked with no gaps
      3   Three of a kind   Three equal ranks within five cards
      2   Two pairs         Two pairs of equal ranks within five cards
      1   One pair          One pair of equal ranks within five cards
      0   Nothing in hand
"""

## Checking total number of hands


## Checking total number of pairs and add percent format



## Add Error Checking Codes



## All Together


