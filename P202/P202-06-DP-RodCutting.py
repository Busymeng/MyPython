##############################################################################
##  Rod Cutting Problem with DP
##############################################################################

class RodCutting:
    
    def __init__(self,rodL,p):
        self.rodL = rodL
        self.p = p
        self.tb = [[0]*(rodL+1) for i in range(len(p))]
        
    def rodDP(self):
        
        for i in range(1,len(self.p)):
            for j in range(1,self.rodL+1):
                if i<=j:
                    b = max(self.tb[i-1][j],p[i]+self.tb[i][j-i])
                    self.tb[i][j] = b
                else:
                    self.tb[i][j]=self.tb[i-1][j]
                    
                    
    def showAns(self):
        
        print("Maximum profit is: ${}".format(self.tb[len(self.p)-1][self.rodL]))
        
        col = self.rodL
        row = len(self.p)-1
        
        while col>0 and row>0:
            if self.tb[row][col]==self.tb[row-1][col]:
                row = row-1
            else:
                print("We make cut: ",row,"m")
                col = col - row
                
rodL = 5
p = [0,2,5,7,3]

rc = RodCutting(rodL,p)
rc.rodDP()
rc.showAns()












                