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

str1 = str(123)



## Escape sequences:
"""
   * \n : carriage return or new line
   * \t : tab
   * \' : single quote
"""

"I'm a boy."
'I like that "dog".'

## Some string methods:
"""
   * length : len()
   * + and *
   * Membership : in
"""

print(dir(""))
len("abcd")
"abc".upper()

x = 12
"abc" + "cd"
"abc" + str(x)

"abc" * 3

"a" in "abc"
"ab" in "abcd"




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
"abc"[0]
"abcd"[0:2]
"abcdefg"[0:5:2]

"abcd"[:2]
"abcdefg"[0::2]

"abcd"[-1]
"abcd"[-2]
"abcd"[-1:-5:-1]
"abcd"[::-1]


## Strings are immutable.
"""
   * Collections can be nutable and immutable.
     > Immutable - you can NOT change any element
     > Mutable - you CAN change any element
   * You can create a new string to include the change.
"""
s = "abcd"
s[0] = "A"

s.upper()
s


s = s.upper()
s


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

"a" < "b"
"Roger" < "robert"





## String Format
## "a string here with some {}".format()

"Sorry, is this the {0} minute {0}?".format(5,"talk")
"Sorry, is this the {1} minute {1}?".format(5,"talk")
"Sorry, is this the {1} minute {0}?".format(5,"talk")
"Sorry, is this the {p} minute {p}?".format(p=5,d="talk")


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
"{}-{}-{}".format(12,23,45)
"{:>10}-{:>10}-{:>10}".format(12,23,45)

## Floating-point specification
##   {:totalspace.precisionf}  ==> {:8.2f}
##
## Reference: https://pyformat.info/

import math

"{0} or {0} or {0}".format(math.pi)
"{0:<8.2f} or {0:^10.4f} or {0:>1.2f}".format(math.pi)

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

for ch in "abcdefg":
    print(ch)
    
s = "abcdefghijk"
for i in s:
    print(i + " ",end="")    

ind = 0
for i in s:
    print(ind,i)
    ind += 1


## A range of integers
"""
   * We can generate a second sequence, a seuence of integers, using the 
     range() function.
   * range() takes 3 arguments:
     > A start integer. If omitted it is assumed to be 0.
     > An end integer. This is required.
     > A step integer. If omitted, it is assumed to be 1.
"""    

for i in range(len(s)):
    print(i, s[i])


for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i)


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

for i, ch in enumerate("abcdefg"):
    print(i,ch)
    
s1 = "abcd"
s2 = "1234"
zip(s1,s2)
list(zip(s1,s2)) 

for i1,i2 in zip(s1,s2):
    print(i1,i2)

ord("A")
ord("a")
chr(65)
chr(97)


loud = "SCREAM"
soft = ""
for ch in loud:
    soft += chr(ord(ch)+32)
print(soft)
   
    
################################################################
## Text encryption and decryption 
##   Using ord(), chr() and zip()

## Version 1: key list
message = "CLEARLY"
keys = [5,8,27,45,17,31,5]   

emessage = ""

for i, ch in zip(keys,message):
    emessage += chr(ord(ch)+i)
    print(ch,i,emessage)

emessage = "HT`nck^"
keys = [5,8,27,45,17,31,5]

message = ""
for i, ch in zip(keys,emessage):
    message += chr(ord(ch)-i)
    print(ch,i,message)
   
## Version 2: Clear words

message = "CLEARLY"
keys = "The 19 century psychologist William James once said"   
emessage = ""

for kch, ch in zip(keys,message):
    emessage += chr(ord(ch)+ord(kch)%37)
    print(ch,kch,emessage)

emessage = "Mj`a^`y"
keys = "The 19 century psychologist William James once said"

message = ""
for kch, ch in zip(keys,emessage):
    message += chr(ord(ch)-ord(kch)%37)
    print(ch,kch,message)



################################################################
## Examples using string and for
"""
   (1) Let's SHOUT!
       Write a program that converts every lowercase character to an 
       upperase character.
"""
s = "I am really, really mad!"

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lowercase.find("d")
lowercase.index("d")

lowercase.find("A")
lowercase.index("A")

for ch in s:
    if ch in lowercase:
        print(uppercase[lowercase.find(ch)],end="")
    else:
        print(ch,end="")


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
import string
string.ascii_lowercase
string.punctuation
string.digits
string.whitespace

## Find the "good " characters
test = "Madam, I'm Adam"
newStr = ""
test = test.lower()
for ch in test:
    if ch in string.ascii_lowercase or ch in string.digits:
        newStr += ch
print(newStr)




## Another way: Dump the "bad" characters

test = "Madam, I'm Adam"
test = test.lower()
print(test)
for ch in string.punctuation + string.whitespace:
    test = test.replace(ch,"") 
print(test)



## Palindrome check!
"""
   (1) Index method
       > Compare the first and last character using indices.
       > If they are not the same, not a palindrome.
       > If they are the same, then move up one index from front, and
         dwon one index from the back, and repeat.
       > Done when we get to the middle.
"""
front = 0
end = len(test)-1
mid = len(test)/2
while end>=mid:
    if test[front]!=test[end]:
        print(test,"is not a palindrome")
        break
    end -= 1
    front += 1
else:
    print(test,"is a palindrome")
    
    
"""
   (2) Slice method
       > Compare the first and last character using indices.
       > Then use slicing to move those characters if they match.
       > Keep going untile a difference occurs or you run out of string.
"""
checkStr = test
while checkStr:
    if checkStr[0]!=checkStr[-1]:
        print(test,"is not a palindrome")
        break
    checkStr = checkStr[1:-1]
else:
    print(test,"is a palindrome")



"""
   (3) Reverse way
       > Reverse the string and compare it to the converted string.     
"""
if test == test[::-1]:
    print(test,"is a palindrome")
else:
    print(test,"is not a palindrome")

        
