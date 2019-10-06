#Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

human = True

play_str=input("Would you like to play? (0=no, 1=yes) ")

hwin = 0
cwin = 0

while int(play_str) != 0:
    pile1 = 5
    pile2 = 15
    
    game = True
    print("Start --> Pile1:",pile1,"    Pile2:",pile2)
    while game:
        
        if human:
            pile = int(input("Choose a pile (1 or 2): "))
                
            if pile == 1:
                stone = int(input("Choose stones to remove from pile: "))
                while not(1<=stone<=3 and stone<=pile1):
                    stone = int(input("Choose stones to remove from pile: "))
                
                pile1 -= stone
            
            if pile == 2:
                stone = int(input("Choose stones to remove from pile: "))
                while not(1<=stone<=3 and stone<=pile2):
                    stone = int(input("Choose stones to remove from pile: "))
                pile2 -= stone
                
            print("Player -> Remove",stone,"stones from pile",pile)
            print("Pile1:",pile1,"    Pile2:",pile2)
            human = False
        else:
            if pile == 1:
                if pile2 != 0:
                    pile2 -= 1
                    cpile = 2
                else:
                    pile1 -= 1
                    cpile = 1
                
            if pile == 2:
                if pile1!=0:
                    pile1 -= 1
                    cpile = 1
                else:
                    pile2 -= 1
                    cpile = 2
                    
                    
            print("Computer -> Remove 1 stone from pile",cpile)
            print("Pile1:",pile1,"    Pile2:",pile2)
            
            human = True
            
        if pile1==0 and pile2==0:
            game = False
            
            if human:
                print("Computer wins")
                cwin +=1
            else:
                print("Human wins")
                hwin += 1
                
            print("Score -> human:",hwin," ; computer:",cwin)
    
    
    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")

else:
   print("\nThanks for playing! See you again soon!")


