##########################################################################
##  BunnyEars
##------------------------------------------------------------------------
"""
We have a number of bunnies and each bunny has two big floppy ears. 
We want to compute the total number of ears across all the bunnies 
recursively (without loops or multiplication).
"""

def bunnyEars(n):
    pass


bunnyEars(0) # 0
bunnyEars(1) # 2
bunnyEars(2) # 4
bunnyEars(3) # 6
bunnyEars(4) # 8
bunnyEars(5) # 10
bunnyEars(12) # 24
bunnyEars(50) # 100	
bunnyEars(234) #468


##########################################################################
##  BunnyEars2
##------------------------------------------------------------------------
"""
We have bunnies standing in a line, numbered 1, 2, ... 
The odd bunnies (1, 3, ..) have the normal 2 ears. 
The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have 
a raised foot. Recursively return the number of "ears" in the bunny 
line 1, 2, ... n (without loops or multiplication).
"""

def bunnyEars2(n):
    pass


bunnyEars2(0) # 0
bunnyEars2(1) # 2
bunnyEars2(2) # 5
bunnyEars2(3) # 7
bunnyEars2(4) # 10	
bunnyEars2(5) # 12
bunnyEars2(6) # 15
bunnyEars2(10) # 25


##########################################################################
##  Triangle
##------------------------------------------------------------------------
"""
We have triangle made of blocks. The topmost row has 1 block, the next row 
down has 2 blocks, the next row has 3 blocks, and so on. 
Compute recursively (no loops or multiplication) the total number of blocks 
in such a triangle with the given number of rows.
"""

def triangle(rows):
    pass


triangle(0) # 0
triangle(1) # 1
triangle(2) # 3
triangle(3) # 6
triangle(4) # 10	
triangle(5) # 15		
triangle(6) # 21		
triangle(7) # 28


##########################################################################
##  SumDigits
##------------------------------------------------------------------------
"""
Given a non-negative int n, return the sum of its digits recursively 
(no loops). Note that mod (%) by 10 yields the rightmost digit 
(126 % 10 is 6), while divide (/) by 10 removes the rightmost digit 
(126 / 10 is 12).
"""

def sumDigits(n):
    pass


sumDigits(126) # 9
sumDigits(49) # 13
sumDigits(12) # 3
sumDigits(10) # 1
sumDigits(1) #1	
sumDigits(0) # 0		
sumDigits(730) # 10
sumDigits(1111) # 4	
sumDigits(11111) # 5		
sumDigits(10110) # 3	
sumDigits(235) # 10


##########################################################################
##  Count7
##------------------------------------------------------------------------
"""
Given a non-negative int n, return the count of the occurrences of 7 as a 
digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 
yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes 
the rightmost digit (126 / 10 is 12).
"""

def count7(n):
    pass
    


count7(717) # 2
count7(7) # 1	
count7(123) # 0	
count7(77) # 2
count7(7123) # 1	
count7(771237) # 3
count7(771737) # 4
count7(47571) # 2
count7(777777) # 6
count7(70701277) # 4	
count7(777576197) # 5	
count7(99999) # 0	
count7(99799) # 1



##########################################################################
##  Count8
##------------------------------------------------------------------------
"""
Given a non-negative int n, compute recursively (no loops) the count of the 
occurrences of 8 as a digit, except that an 8 with another 8 immediately to 
its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the 
rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost 
digit (126 / 10 is 12).
"""

def count8(n):
    pass


count8(8) # 1
count8(818) # 2
count8(8818) # 4
count8(8088) # 4	
count8(123) # 0
count8(81238) # 2
count8(88788) # 6
count8(8234) # 1	
count8(2348) # 1
count8(23884) # 3
count8(0) # 0
count8(1818188) # 5	
count8(8818181) # 5
count8(1080) # 1	
count8(188) # 3	
count8(88888) # 9		
count8(9898) # 2	
count8(78) # 1


##########################################################################
##  PowerN
##------------------------------------------------------------------------
"""
Given base and n that are both 1 or more, compute recursively (no loops) 
the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
"""

def powerN(base,n):
    pass


powerN(3, 1) # 3	
powerN(3, 2) # 9	
powerN(3, 3) # 27
powerN(2, 1) # 2	
powerN(2, 2) # 4	
powerN(2, 3) # 8
powerN(2, 4) # 16
powerN(2, 5) # 32
powerN(10, 1) # 10
powerN(10, 2) # 100
powerN(10, 3) # 1000



##########################################################################
##  CountX
##------------------------------------------------------------------------
"""
Given a string, compute recursively (no loops) the number of lowercase 'x' 
chars in the string.
"""

def countX(s):
    pass


countX("xxhixx") # 4		
countX("xhixhix") # 3
countX("hi") # 0		
countX("h") # 0
countX("x") # 1
countX("") # 0
countX("hihi") # 0
countX("hiAAhi12hi") # 0


##########################################################################
##  countHi
##------------------------------------------------------------------------
"""
Given a string, compute recursively (no loops) the number of times 
lowercase "hi" appears in the string.
"""

def countHi(s):
    pass


countHi("xxhixx") # 1
countHi("xhixhix") # 2
countHi("hi") # 1
countHi("hihih") # 2	
countHi("h") # 0	
countHi("") # 0
countHi("ihihihihih") # 4
countHi("ihihihihihi") # 5	
countHi("hiAAhi12hi") # 3
countHi("xhixhxihihhhih") # 3
countHi("ship") # 1


##########################################################################
##  changeXY
##------------------------------------------------------------------------
"""
Given a string, compute recursively (no loops) a new string where all the 
lowercase 'x' chars have been changed to 'y' chars.
"""

def changeXY(s):
    pass


changeXY("codex") # "codey"
changeXY("xxhixx") # "yyhiyy"
changeXY("xhixhix") # "yhiyhiy"
changeXY("hiy") # "hiy"
changeXY("h") # "h"
changeXY("x") # "y"
changeXY("") # ""
changeXY("xxx") # "yyy"
changeXY("yyhxyi") # "yyhyyi"
changeXY("hihi") # "hihi"



##########################################################################
##  changePi
##------------------------------------------------------------------------
"""
Given a string, compute recursively (no loops) a new string where all 
appearances of "pi" have been replaced by "3.14".
"""

def changePi(s):
    pass


changePi("xpix") # "x3.14x"	"x3.14x"	OK	
changePi("pipi") # "3.143.14"	"3.143.14"	OK	
changePi("pip") # "3.14p"	"3.14p"	OK	
changePi("pi") # "3.14"	"3.14"	OK	
changePi("hip") # "hip"	"hip"	OK	
changePi("p") # "p"	"p"	OK	
changePi("x") # "x"	"x"	OK	
changePi("") # ""	""	OK	
changePi("pixx") # "3.14xx"	"3.14xx"	OK	
changePi("xyzzy") # "xyzzy"


##########################################################################
##  noX
##------------------------------------------------------------------------
"""
Given a string, compute recursively a new string where all the 'x' chars 
have been removed.
"""

def noX(s):
    pass


noX("xaxb") # "ab"
noX("abc") # "abc"
noX("xx") # ""
noX("") # ""	
noX("axxbxx") # "ab"	
noX("Hellox") # "Hello"



##########################################################################
##  array6
##------------------------------------------------------------------------
"""
Given an array of ints, compute recursively if the array contains a 6. 
We'll use the convention of considering only the part of the array that 
begins at the given index. In this way, a recursive call can pass index+1 
to move down the array. The initial call will pass in index as 0.
"""

def array6(nums,index):
    pass


array6([1, 6, 4], 0) # true	
array6([1, 4], 0) # false
array6([6], 0) # true
array6([], 0) # false
array6([6, 2, 2], 0) # true
array6([2, 5], 0) # false
array6([1, 9, 4, 6, 6], 0) # true
array6([2, 5, 6], 0) # true



##########################################################################
##  array11
##------------------------------------------------------------------------
"""
Given an array of ints, compute recursively the number of times that the 
value 11 appears in the array. We'll use the convention of considering only 
the part of the array that begins at the given index. In this way, 
a recursive call can pass index+1 to move down the array. The initial call 
will pass in index as 0.
"""

def array11(nums,index):
    pass


array11([1, 2, 11], 0) # 1
array11([11, 11], 0) # 2	
array11([1, 2, 3, 4], 0) # 0	
array11([1, 11, 3, 11, 11], 0) # 3
array11([11], 0) # 1	
array11([1], 0) # 0
array11([], 0) # 0
array11([11, 2, 3, 4, 11, 5], 0) # 2
array11([11, 5, 11], 0) # 2


##########################################################################
##  array220
##------------------------------------------------------------------------
"""
Given an array of ints, compute recursively if the array contains somewhere 
a value followed in the array by that value times 10. We'll use the 
convention of considering only the part of the array that begins at the 
given index. In this way, a recursive call can pass index+1 to move down 
the array. The initial call will pass in index as 0.
"""

def array220(nums,index):
    pass


array220([1, 2, 20], 0) # true	
array220([3, 30], 0) # true	
array220([3], 0) # false	
array220([], 0) # false
array220([3, 3, 30, 4], 0) # true
array220([2, 19, 4], 0) # false	
array220([20, 2, 21], 0) # false	
array220([20, 2, 21, 210], 0) # true	
array220([2, 200, 2000], 0) # true	
array220([0, 0], 0) # true	
array220([1, 2, 3, 4, 5, 6], 0) # false
array220([1, 2, 3, 4, 5, 50, 6], 0) # true
array220([1, 2, 3, 4, 5, 51, 6], 0) # false
array220([1, 2, 3, 4, 4, 50, 500, 6], 0) # true



##########################################################################
##  allStar
##------------------------------------------------------------------------
"""
Given a string, compute recursively a new string where all the adjacent chars 
are now separated by a "*".
"""

def allStar(s):
    pass


allStar("hello") # "h*e*l*l*o"	
allStar("abc") # "a*b*c"	
allStar("ab") # "a*b"
allStar("a") # "a"
allStar("") # ""	
allStar("3.14") # "3*.*1*4"	
allStar("Chocolate") # "C*h*o*c*o*l*a*t*e"
allStar("1234") # "1*2*3*4"



##########################################################################
##  pairStar
##------------------------------------------------------------------------
"""
Given a string, compute recursively a new string where identical chars that 
are adjacent in the original string are separated from each other by a "*".
"""

def pairStar(s):
    pass


pairStar("hello") # "hel*lo"	
pairStar("xxyy") # "x*xy*y"
pairStar("aaaa") # "a*a*a*a"	
pairStar("aaab") # "a*a*ab"	
pairStar("aa") # "a*a"	
pairStar("a") # "a"
pairStar("") # ""
pairStar("noadjacent") # "noadjacent"	
pairStar("abba") # "ab*ba"	
pairStar("abbba") # "ab*b*ba"



##########################################################################
##  endX
##------------------------------------------------------------------------
"""
Given a string, compute recursively a new string where all the lowercase 'x' 
chars have been moved to the end of the string.
"""

def endX(s):
    pass


endX("xxre") # "rexx"
endX("xxhixx") # "hixxxx"
endX("xhixhix") # "hihixxx"
endX("hiy") # "hiy"	
endX("h") # "h"	
endX("x") # "x"	
endX("xx") # "xx"
endX("") # ""
endX("bxx") # "bxx"	
endX("bxax") # "baxx"
endX("axaxax") # "aaaxxx"
endX("xxhxi") # "hixxx"



##########################################################################
##  countPairs
##------------------------------------------------------------------------
"""
We'll say that a "pair" in a string is two instances of a char separated by 
a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" 
contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number 
of pairs in the given string.
"""

def countPairs(s):
    pass


countPairs("axa") # 1
countPairs("axax") # 2	
countPairs("axbx") # 1
countPairs("hi") # 0	
countPairs("hihih") # 3
countPairs("ihihhh") # 3
countPairs("ihjxhh") # 0	
countPairs("") # 0	
countPairs("a") # 0	
countPairs("aa") # 0	
countPairs("aaa") # 1


##########################################################################
##  countAbc
##------------------------------------------------------------------------
"""
Count recursively the total number of "abc" and "aba" substrings that appear 
in the given string.
"""

def countAbc(s):
    pass


countAbc("abc") # 1		
countAbc("abcxxabc") # 2	
countAbc("abaxxaba") # 2	
countAbc("ababc") # 2
countAbc("abxbc") # 0
countAbc("aaabc") # 1
countAbc("hello") # 0
countAbc("") # 0	
countAbc("ab") # 0
countAbc("aba") # 1
countAbc("aca") # 0
countAbc("aaa") # 0



##########################################################################
##  count11
##------------------------------------------------------------------------
"""
Given a string, compute recursively (no loops) the number of "11" substrings 
in the string. The "11" substrings should not overlap.
"""

def count11(s):
    pass


count11("11abc11") # 2
count11("abc11x11x11") # 3
count11("111") # 1
count11("1111") # 2	
count11("1") # 0	
count11("") # 0		
count11("hi") # 0
count11("11x111x1111") # 4
count11("1x111") # 1	
count11("1Hello1") # 0
count11("Hello") # 0



##########################################################################
##  stringClean
##------------------------------------------------------------------------
"""
Given a string, return recursively a "cleaned" string where adjacent chars 
that are the same have been reduced to a single char. So "yyzzza" yields "yza".
"""

def stringClean(s):
    pass



stringClean("yyzzza") # "yza"	
stringClean("abbbcdd") # "abcd"	
stringClean("Hello") # "Helo"
stringClean("XXabcYY") # "XabcY"	
stringClean("112ab445") # "12ab45"	
stringClean("Hello Bookkeeper") # "Helo Bokeper"



##########################################################################
##  countHi2
##------------------------------------------------------------------------
"""
Given a string, compute recursively the number of times lowercase "hi" 
appears in the string, however do not count "hi" that have an 'x' immedately 
before them.
"""

def countHi2(s):
    pass



countHi2("ahixhi") # 1
countHi2("ahibhi") # 2
countHi2("xhixhi") # 0
countHi2("hixhi") # 1
countHi2("hixhhi") # 2
countHi2("hihihi") # 3	
countHi2("hihihix") # 3
countHi2("xhihihix") # 2	
countHi2("xxhi") # 0	
countHi2("hixxhi") # 1
countHi2("hi") # 1
countHi2("xxxx") # 0
countHi2("h") # 0
countHi2("x") # 0
countHi2("") # 0	
countHi2("Hellohi") # 1



##########################################################################
##  parenBit
##------------------------------------------------------------------------
"""
Given a string that contains a single pair of parenthesis, compute 
recursively a new string made of only of the parenthesis and their contents, 
so "xyz(abc)123" yields "(abc)".
"""

def parenBit(s):
    pass


parenBit("xyz(abc)123") # "(abc)"
parenBit("x(hello)") # "(hello)"	
parenBit("(xy)1") # "(xy)"	
parenBit("not really (possible)") # "(possible)"	
parenBit("(abc)") # "(abc)"	
parenBit("(abc)xyz") # "(abc)"	
parenBit("(abc)x") # "(abc)"	
parenBit("(x)") # "(x)"	
parenBit("()") # "()"
parenBit("res (ipsa) loquitor") # "(ipsa)"
parenBit("hello(not really)there") # "(not really)"		
parenBit("ab(ab)ab") # "(ab)"



##########################################################################
##  nestParen
##------------------------------------------------------------------------
"""
Given a string, return true if it is a nesting of zero or more pairs of 
parenthesis, like "(())" or "((()))". Suggestion: check the first and last 
chars, and then recur on what's inside them.
"""

def nestParen(s):
    pass


nestParen("(())") # true	
nestParen("((()))") # true	
nestParen("(((x))") # false	
nestParen("((())") # false	
nestParen("((()()") # false	
nestParen("()") # true
nestParen("") # true	
nestParen("(yy)") # false	
nestParen("(())") # true	
nestParen("(((y))") # false	
nestParen("((y)))") # false	
nestParen("((()))") # true	
nestParen("(())))") # false	
nestParen("((yy())))") # false	
nestParen("(((())))") # true



##########################################################################
##  strCount
##------------------------------------------------------------------------
"""
Given a string and a non-empty substring sub, compute recursively the number 
of times that sub appears in the string, without the sub strings overlapping.
"""

def strCount(s,sub):
    pass


strCount("catcowcat", "cat") # 2	
strCount("catcowcat", "cow") # 1	
strCount("catcowcat", "dog") # 0	
strCount("cacatcowcat", "cat") # 2
strCount("xyx", "x") # 2
strCount("iiiijj", "i") # 4	
strCount("iiiijj", "ii") # 2
strCount("iiiijj", "iii") # 1	
strCount("iiiijj", "j") # 2	
strCount("iiiijj", "jj") # 1	
strCount("aaabababab", "ab") # 4	
strCount("aaabababab", "aa") # 1	
strCount("aaabababab", "a") # 6
strCount("aaabababab", "b") # 4



##########################################################################
##  strCopies
##------------------------------------------------------------------------
"""
Given a string and a non-empty substring sub, compute recursively if at
least n copies of sub appear in the string somewhere, possibly with 
overlapping. N will be non-negative.
"""

def strCopies(s, sub, n):
    pass



strCopies("catcowcat", "cat", 2) # true	
strCopies("catcowcat", "cow", 2) # false
strCopies("catcowcat", "cow", 1) # true	
strCopies("iiijjj", "i", 3) # true	
strCopies("iiijjj", "i", 4) # false	
strCopies("iiijjj", "ii", 2) # true	
strCopies("iiijjj", "ii", 3) # false	
strCopies("iiijjj", "x", 3) # false	
strCopies("iiijjj", "x", 0) # true
strCopies("iiiiij", "iii", 3) # true	
strCopies("iiiiij", "iii", 4) # false
strCopies("ijiiiiij", "iiii", 2) # true
strCopies("ijiiiiij", "iiii", 3) # false	
strCopies("dogcatdogcat", "dog", 2) # true



##########################################################################
##  strDist
##------------------------------------------------------------------------
"""
Given a string and a non-empty substring sub, compute recursively the largest 
substring which starts and ends with sub and return its length.
"""

def strDist(s, sub):
    pass


strDist("catcowcat", "cat") # 9		
strDist("catcowcat", "cow") # 3		
strDist("cccatcowcatxx", "cat") # 9
strDist("abccatcowcatcatxyz", "cat") # 12
strDist("xyx", "x") # 3
strDist("xyx", "y") # 1		
strDist("xyx", "z") # 0	
strDist("z", "z") # 	1
strDist("x", "z") # 0
strDist("", "z") # 0	
strDist("hiHellohihihi", "hi") # 13	
strDist("hiHellohihihi", "hih") # 5	
strDist("hiHellohihihi", "o") # 1	
strDist("hiHellohihihi", "ll") # 2


















