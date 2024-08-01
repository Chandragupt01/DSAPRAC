class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        if N < 1:
            return
        self.printNos(N-1)
        print(N,end=" ")