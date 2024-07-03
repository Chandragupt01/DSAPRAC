class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        result=[]
        maxi=float("-inf")
        for i in range(n-1,-1,-1):
            e=max(maxi,arr[i])
            if e>maxi:
                result.append(e)
                maxi=e
        return result