


##----Main Program------------------------------------------------------------

b1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

print_board(b1)
solve(b1)
print("_"*27)
print_board(b1)


b2=[[3,0,6,5,0,8,4,0,0], 
    [5,2,0,0,0,0,0,0,0], 
    [0,8,7,0,0,0,0,3,1], 
    [0,0,3,0,1,0,0,8,0], 
    [9,0,0,8,6,3,0,0,5], 
    [0,5,0,0,9,0,6,0,0], 
    [1,3,0,0,0,0,2,5,0], 
    [0,0,0,0,0,0,0,7,4], 
    [0,0,5,2,0,6,3,0,0]] 

print_board(b2)
solve(b2)
print("_"*27)
print_board(b2)


b3=[[5,3,0,0,7,0,0,0,0], 
    [6,0,0,1,9,5,0,0,0], 
    [0,9,8,0,0,0,0,6,0], 
    [8,0,0,0,6,0,0,0,3], 
    [4,0,0,8,0,3,0,0,1], 
    [7,0,0,0,2,0,0,0,6], 
    [0,0,6,0,0,0,2,8,0], 
    [0,0,0,4,1,9,0,0,5], 
    [0,0,0,0,8,0,0,7,9]] 

print_board(b3)
solve(b3)
print("_"*27)
print_board(b3)







