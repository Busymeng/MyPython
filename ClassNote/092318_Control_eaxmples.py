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
year = int(input("Enter a year to test: "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(year,"is a leap year")
        else:
            print(year,"is NOT a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is NOT a leap year")

   
   
####################################################################
##  Find the Largest Among Three Numbers
"""
   * Find the largest number among the three input numbers
"""
# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)



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

#num = int(input("Enter a number: "))

num = 6990
while num<=10000:
 
    divisor = 1
    sum = 0
    while divisor <= num/2:
        if num % divisor == 0:
            # Found the divisor
            sum = sum + divisor
        divisor += 1
        
    if num == sum:
        print(num,"is a perfect number")
    #else:
        #print(num,"is NOT a perfect number")
        
    num += 1
    
    
    
    
####################################################################    
##  Classifying Numbers
##
##    Classify a range of numbers with respect to perfect , abundant or 
##    deficient unless otherwise stated , variables are assumed to be 
##    of type int. 
##       abundant --> number < sum of  divisors
##       deficient -->  number > sum of  divisors  
    
top_num_str = input("What is the upper number for the range:")
top_num = int(top_num_str)
number = 2

while number <= top_num:
    # sum up the divisors
    divisor = 1
    sum_of_divisors = 0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
        divisor = divisor + 1
        
    # classify the number based on its divisor sum
    if number == sum_of_divisors:
        print(number,"is perfect")
    if number < sum_of_divisors:
        print(number,"is abundant")
    if number > sum_of_divisors:
        print(number,"is deficient")
    number += 1    
    
    
####################################################################    
##  Simple guessing game  
##    It starts with a random number and guess with hints until :
##      guess is correct or 
##      the guess is out of range indicating the user is quitting
##    All non−typed variables are integers.

## Version 1
import random   ## get the random number module
number = random.randint(0,100)   ## get a random number
                                 ## between 0 and 100 inclusive

guess = int(input("Guess a nummber (0~100): "))  

while guess != number:
    if guess > number:
        print("Too high!!")
    else:
        print("Too low!!")
    guess = int(input("Please guess again: "))
else:
    print("You guess right. The number is",number)
    
    
    
## Version 2

import random   ## get the random number module
lo = 100
hi = 500
number = random.randint(lo,hi)   ## get a random number
                                 ## between 0 and 100 inclusive

guess = int(input("Guess a nummber (" + str(lo) + "~" +str(hi)+"): "))  

while guess != number:
    if guess > number:
        print("Too high!!")
        hi = guess - 1
        print("guess",lo,"to",hi)
    else:
        print("Too low!!")
        lo = guess + 1
        print("guess",lo,"to",hi)
    guess = int(input("Please guess again: "))
else:
    print("You guess right. The number is",number)
    
    
## Version 3  
    
import random   ## get the random number module
lo = 100
hi = 500
number = random.randint(lo,hi)   ## get a random number
                                 ## between 0 and 100 inclusive
guess = -1
while not lo<= guess <=hi:
    guess = int(input("Guess a nummber (" + str(lo) + "~" +str(hi)+"): "))  

while guess != number:
    if guess > number:
        print("Too high!!")
        hi = guess - 1
        print("guess",lo,"to",hi)
        guess = int(input("Please guess again: "))
        while not lo<= guess <=hi:
            print("Please guess between",lo,'and',hi)
            guess = int(input("Please guess again: "))
    else:
        print("Too low!!")
        lo = guess + 1
        print("guess",lo,"to",hi)
        guess = int(input("Please guess again: "))
        while not lo<= guess <=hi:
            print("Please guess between",lo,'and',hi)
            guess = int(input("Please guess again: "))
else:
    print("You guess right. The number is",number)

## Version 4: Count the number of guesses.
    
    
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
    
number_str = input("Enter a positive integer:")
number = int(number_str)
count = 0

print("Starting with number:",number)
print("Sequence is: ", end=' ')

while number > 1: # stop when the sequence reaches 1
    if number%2: # number i s odd
        number = number*3 + 1
    else: # number i s even
        number = number//2
        print(number,",", end=' ') # add number to sequence

    count +=1 # add to the count

else:
    print() # blank line for nicer output
    print("Sequence is ",count," numbers long")   
    
    
    
    
    
    
    
    