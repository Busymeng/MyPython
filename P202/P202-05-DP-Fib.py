##  Fibonacci Number Calculation

class Fibonacci:
    
    def __init__(self):
        self.table = {}
        self.table[0] = 0
        self.table[1] = 1
        
    def fib_Recursion(self,n):
        
        if n == 0: return 0
        if n == 1: return 1
        
        return self.fib_Recursion(n-1)+self.fib_Recursion(n-2)
    
    ## Memoization  (Top-Down Approach)
    def fib_Memoize(self,n):
        
        if n in self.table:
            return self.table[n]
        
        self.table[n-1] = self.fib_Memoize(n-1)
        self.table[n-2] = self.fib_Memoize(n-2)
        
        f = self.table[n-1] + self.table[n-2]
        self.table[n] = f
        
        return f
    
    
    ## Bottom-Up Approach (No recursion)
    def fib_Tabulate(self,n):
        
        for k in range(2,n+1):
            if k<=2:
                f = 1
            else:
                f = self.table[k-1] + self.table[k-2]
            self.table[k] = f
            
        return self.table[n]
    
    
    def fib_Super(self,n):
        
        b2, b1 = 0, 1
        
        if n == 0: return 0
        if n == 1: return 1
        
        for i in range(2,n):
            temp = b1+b2
            b2 = b1
            b1 = temp
            
        return b1+b2
            
        
    
    
fib = Fibonacci()
print(fib.fib_Recursion(10))

print(fib.fib_Memoize(100))

print(fib.fib_Tabulate(100))

print(fib.fib_Super(100))






















