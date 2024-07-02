#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i=0
        j=0
        res=[]
        while i<n and j<m:
            if arr1[i]<arr2[j]:
                if len(res)==0 or res[-1]!=arr1[i]:
                    res.append(arr1[i])
                i+=1
            else:    
                if len(res)==0 or res[-1]!=arr2[j]:
                    res.append(arr2[j])
                j+=1
        while i<n:
            if len(res)==0 or res[-1]!=arr1[i]:
                res.append(arr1[i])
            i+=1
        while j<m:
            if len(res)==0 or res[-1]!=arr2[j]:
                res.append(arr2[j])
            j+=1
        return res