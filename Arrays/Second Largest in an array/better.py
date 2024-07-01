class Solution:
	def print2largest(self,arr, n):
		# code here
		largest=-1
		secondLargest=-1
		for i in range(n):
		    largest=max(largest,arr[i])
		    
		for i in range(n):
		    if arr[i]>secondLargest and arr[i]!=largest:
		        secondLargest=arr[i]
        return secondLargest