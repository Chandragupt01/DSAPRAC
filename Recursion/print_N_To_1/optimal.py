
class Solution:
    def printNos(self, n):
        # Code here
        if n < 1:
            return
        print(n,end=" ")
        self.printNos(n-1)

