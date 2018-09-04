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
## Build the basic structure the open a file with exception.




## We can try to add loops to make user enter the right file name




## Now do the work.
## Check the file can be read correctly.



## Do the REAL work




## Write the final result to a file


        
 