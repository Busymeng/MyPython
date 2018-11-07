##from random import randint  # the real Python random
from craps_random import randint  # Use this randint() for testing purpose

def display_game_rules():
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your point." 
          The player loses by rolling a 7 before making the point.''')

def get_bank_balance():
    '''Insert docstring here.'''
    pass  # replace this line with your code

def add_to_bank_balance(balance):
    '''Insert docstring here.'''
    pass  # replace this line with your code

def get_wager_amount():
    '''Insert docstring here.'''
    pass  # replace this line with your code

def is_valid_wager_amount(wager, balance):
    '''Insert docstring here.'''
    pass  # replace this line with your code

def roll_die():
    '''Insert docstring here.'''
    pass  # replace this line with your code

def calculate_sum_dice(die1_value, die2_value):
    '''Insert docstring here.'''
    pass  # replace this line with your code

def first_roll_result(sum_dice):
    '''Insert docstring here.'''
    pass  # replace this line with your code
    
def subsequent_roll_result(sum_dice, point_value):
    '''Insert docstring here.'''
    pass  # replace this line with your code

def main():    
    '''Insert docstring here.'''
    pass  # replace this line with your code

if __name__ == "__main__":
    main()
