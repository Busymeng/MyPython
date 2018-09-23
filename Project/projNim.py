#Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

play_str=input("Would you like to play? (0=no, 1=yes) ")

while int(play_str) != 0:
    # initialize state, pile_1, pile_2, player_true
    pile_1 = 5
    pile_2 = 5
    player_true = True
    game_over = False
    
    while not game_over:
        # if player_true
        
        # prompt for pile
        
        # prompt for number of stones
        
        # remove stones from pile
        
        # if computer's trun "else"
        
        # .....
        
        # determine if game is over
        
        #   if not switch players
        
        # determine who won the game and print victor (winner)
    
    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")

else:
   print("\nThanks for playing! See you again soon!")


