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
        freq=set()
        for i in arr1:
            freq.add(i)
        for j in arr2:
            freq.add(j)
        return sorted(list(freq))