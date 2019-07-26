def total( start, end ):

   tot = 0

   for n in range(start,end):
       tot += n

   return tot

A = total( 0, 10 )
print(A)
B = total( 8, 12 )
print(B)
C = total( 15, 15 )
print(C)
D = 3 * total( 4, 7 ) + 10
print(D)
X = 5
E = total( 2*X, 12 )
print(E)
