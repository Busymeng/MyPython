##############################################################################
##  Control Examples
##############################################################################

####################################################################
##  Leap Year
"""
   * A leap year is exactly divisible by 4 except for century years 
     (years ending with 00). 
   * The century year is a leap year only if it is perfectly divisible by 400.
"""


   
   
####################################################################
##  Find the Largest Among Three Numbers
"""
   * Find the largest number among the three input numbers
"""



####################################################################
##  Finding Perfect Numbers
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


    
    
####################################################################    
##  Classifying Numbers
##
##    Classify a range of numbers with respect to perfect , adundant or 
##    deficient unless otherwise stated , variables are assumed to be 
##    of type int. 
    

    
    
####################################################################    
##  Simple guessing game  
##    It starts with a random number and guess with hints until :
##      guess is correct or 
##      the guess is out of range indicating the user is quitting
##    All non−typed variables are integers.

import random   ## get the random number module
number = random.randint(0,100)   ## get a random number
                                 ## between 0 and 100 inclusive

    
    
    
#########################################################################    
##  Hailstone Sequence
"""
   * The Collatz conjecture is an unsolved mathematical conjecture from 1937 
     that makes for an interesting programming example. 
   * The conjecture is that given the following formula and an initial 
     positive integer, the generated sequence always ends in 1. 
   * Although this has been shown to be true for large initial integers 
     (approximately 2.7 × 10e16), it has not yet been proven true for all.
   * The hailstone formula is as follows:
     > If the number is even, divide it by 2.
     > If the number is odd, multiply by 3 and add 1.
     > When the number reaches 1, quit.
"""
    

    
    
    
    
    
    
    
    
