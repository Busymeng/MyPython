##  0-1 Knapsack problem

class Knapsack:
    
    def __init__(self,items,cap,weights,values):
        self.items = items
        self.cap = cap
        self.weights = weights
        self.values = values
        self.table = [[0 for i in range(cap+1)] for i in range(items+1)]
        
        
    def DP(self):
        
        for i in range(1,self.items+1):
            for w in range(1,self.cap+1):
                notTakeItem = self.table[i-1][w]
                takeItem = 0
                
                if self.weights[i] <= w:
                    takeItem = self.values[i] + self.table[i-1][w-self.weights[i]]
                    
                self.table[i][w] = max(notTakeItem, takeItem)
                
    def showResult(self):
        print("Total values: {}".format(self.table[self.items][self.cap]))
        
        w = self.cap
        
        for n in range(self.items,0,-1):
            if self.table[n][w]!=0 and self.table[n][w]!= self.table[n-1][w]:
                print("We take item: {}".format(n))
                w = w - self.weights[n]
                

n = 3
cap = 5
w = [0,4,2,3]
v = [0,10,4,7]

knap = Knapsack(n,cap,w,v)
knap.DP()
knap.showResult() 


n = 4
cap = 7
w = [0,1,3,4,5]
v = [0,1,4,5,7]

knap = Knapsack(n,cap,w,v)
knap.DP()
knap.showResult() 










       