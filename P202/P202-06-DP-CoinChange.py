##############################################################################
##  Coin Change Problem with DP
##############################################################################

class CoinChange:
    
    def coinRecur(self,T,v,index):
        if T==0:
            return 1
        if T<0:
            return 0
        
        if index == len(v):
            return 0
        
        return self.coinRecur(T-v[index],v,index) + self.coinRecur(T,v,index+1)
    
    
    def coinDP(self,T,v):
        
        table = [[0]*(T+1) for x in range(len(v)+1)]
        
        for i in range(len(v)+1):
            table[i][0] = 1
            
        for i in range(1,len(v)+1):
            for j in range(1,T+1):
                if v[i-1]<=j:
                    table[i][j]=table[i-1][j]+table[i][j-v[i-1]]
                else:
                    table[i][j]=table[i-1][j]
                    
        print("Solution is: {}".format(table[len(v)][T]))
        
        
T = 1000
coins = [1,5,10,25]
cc = CoinChange()
cc.coinDP(T,coins)
#print(cc.coinRecur(T,coins,0))


















        
        