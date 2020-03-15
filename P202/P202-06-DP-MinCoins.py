#############################################################################
##  Minimum Coin Change Problem
#############################################################################

def min_coins(coins,total):
    cols = total + 1
    rows = len(coins)
    
    T = [[0 if col==0 else float('inf') for col in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(1,cols):
            if j<coins[i]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = min(T[i-1][j], 1 + T[i][j-coins[i]])
                
    return T[rows-1][cols-1]


def min_coins2(coins,total):
    cols = total +1
    T = [0 if i==0 else float('inf') for i in range(cols)]
    R = [-1 for i in range(cols)]
    
    for j in range(len(coins)):
        for i in range(1,cols):
            coin = coins[j]
            if i>=coins[j]:
                if T[i]>1+T[i-coin]:
                    T[i] = 1 + T[i-coin]
                    R[i] = j
                    
    print_coins(R,coins)
    print()
                    
    return T[cols-1]


def print_coins(R,coins):
    
    start = len(R)-1
    
    if R[start]==-1:
        print("No solution")
        return
    
    print("Coins: ", end = "")
    while start!=0:
        coin = coins[R[start]]
        print("{} ".format(coin),end="")
        start = start - coin
        
        
def min_coins_TD(coins,total,memo=dict()):
    
    if total ==0:
        return 0
    
    if total in memo:
        return memo[total]
    
    min_val = float('inf')
    
    for i in range(len(coins)):
        coin = coins[i]
        if coin > total:
            continue
        val = min_coins_TD(coins,total-coin,memo)
        min_val = min(min_val,val)
        
    min_val += 1
    
    memo[total] = min_val

    return min_val        

    


coins = [1,5,6,8]
total = 11
print(min_coins(coins,total))
print(min_coins2(coins,total))
print("Coin Change TD result:",min_coins_TD(coins,total))