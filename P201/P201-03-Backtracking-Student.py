##############################################################################
##  Backtracking Algorithm
##############################################################################

##############################################################################
##  Generate all permutations of a string that follow given constraints
##----------------------------------------------------------------------------
"""
   * Given a string, generate all permutations of it that do not 
     contain ‘B’ after ‘A’, i.e., the string should not contain “AB” as 
     a substring.
     
   * Input : str = “ABC”
   * Output : ACB, BAC, BCA, CBA
              Out of 6 permutations of “ABC”, 4 follow the given constraint 
              and 2 (“ABC” and “CAB”) do not follow.
   * Input : str = “BCD”
   * Output : BCD, BDC, CDB, CBD, DCB, DBC
"""

##----------------------------------------------------------------------------
# Simple Python3 program to print all permutations of a string that follow 
# given constraint 
"""
   * The following solution first generates all permutations, then for every 
     permutation it checks if it follows given constraint or not.
"""



##----------------------------------------------------------------------------
# An efficient solution is to use Backtracking.  
"""
   * We cut down the recursion tree whenever we see that substring “AB” is 
     formed. 
   * How do we do this? 
     - we add a isSafe() function. 
     - Before doing a swap, we check if previous character is ‘A’ and 
       current character is ‘B’.
"""






##############################################################################
##  Maze Problem 
##----------------------------------------------------------------------------      
"""
   * A Maze is given as N*N binary matrix of blocks where source block is 
     the upper left most block i.e., maze[0][0] and destination block is 
     lower rightmost block i.e., maze[N-1][N-1]. 
     - A rat starts from source and has to reach the destination. 
     - The rat can move only in two directions: forward and down.
     - In the maze matrix, 0 means the block is a dead end and 1 means the 
       block can be used in the path from source to destination. 
     
   * Note that this is a simple version of the typical Maze problem. 
"""    




##############################################################################
##  N-Queen Problem
##----------------------------------------------------------------------------
"""
   1) Start in the leftmost column
   2) If all queens are placed
         return true
   3) Try all rows in the current column. 
         Do following for every tried row.
         a) If the queen can be placed safely in this row 
            then mark this [row, column] as part of the 
            solution and recursively check if placing
            queen here leads to a solution.
         b) If placing the queen in [row, column] leads to
            a solution then return true.
         c) If placing queen doesn't lead to a solution then
            unmark this [row, column] (Backtrack) and go to 
            step (a) to try other rows.
   4) If all rows have been tried and nothing worked,
      return false to trigger backtracking.
"""



##############################################################################
##  Sudoku Problem
##----------------------------------------------------------------------------
"""
   * Algorithm:
     (1) Create a function that checks after assigning the current index 
         the grid becomes unsafe or not. 
         - Keep Hashmap for a row, column and boxes. 
         - If any number has a frequency greater than 1 in the hashMap 
           return false else return true; hashMap can be avoided by 
           using loops.
     (2) Create a recursive function which takes a grid.
     (3) Check for any unassigned location. 
         - If present then assign a number from 1 to 9, check if assigning 
           the number to current index makes the grid unsafe or not, if safe 
           then recursively call the function for all safe cases from 0 to 9. 
         - If any recursive call returns true, end the loop and return true. 
         - If no recursive call returns true then return false.
     (4) If there is no unassigned location then return true.
"""

    