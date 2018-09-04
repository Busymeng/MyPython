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
     > When you open for writing.
       >> If the file does not exist, it is created in the same place as the
          Python program that is running.
       >> If it does exist, the file's present contenta are wiped. 
          So be careful.
"""



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




## Close Your Files
"""
   * When you are finished wih a file, you should close the file object.
     This makes sure that the information on the file and in your program
     are in sync.
"""



## Demo Example





