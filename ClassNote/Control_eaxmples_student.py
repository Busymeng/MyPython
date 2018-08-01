# -*- coding: Contrl Examples -*-
"""
Created on Mon Jul 30 00:12:57 2018

@author: Michael Meng
"""

### Finding Perfect Numbers
##    
##   A perfect number is an integer whose sum of integer divisors 
##   (excluding the number itself ) add up to the number.
##   
##   e.g.  6 = 1 + 2 + 3
##        28 = 1 + 2 + 4 + 7 + 14
##       496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248

##   1. Get the number we are going to evaluate. Let us call it number_int.
##   2. Find all the integer divisors of number_int.
##   3. For each of those integer divisors, add that divisor to 
##      a sum_of_divisors_int value. The sum_of_divisors_int should start at 0 
##      (0 is the additive identity: 0 + x = x ).
##   4. Based on the values associated with sum_of_divisors_int and the 
##      number itself (number_int), we need to decide whether the number 
##      is perfect (we can classify it as deficient or abundant later).

##  get a number to check


##  find and sum up the divisors

    
##  classify the resul t

    
    
    
### Classifying Numbers
##
##    Classify a range of numbers with respect to perfect , adundant or 
##    deficient unless otherwise stated , variables are assumed to be 
##    of type int. 
    

    
    
    
### Simple guessing game  
##    It starts with a random number and guess with hints until :
##      guess is correct or 
##      the guess is out of range indicating the user is quitting
##    All non−typed variables are integers.

import random   ## get the random number module
number = random.randint(0,100)   ## get a random number
                                 ## between 0 and 100 inclusive
print("Hi-Lo Number Guessing Game: between 0 and 100 inclusive.")
print()    
    
## get an initial guess


## while guess i s range , keep asking

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    