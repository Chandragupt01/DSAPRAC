class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float("-inf")
        for i in range(n):
            for j in range(i,n):
                sumNum=0
                for k in range(i,j+1):
                    sumNum+=nums[k]
                maxi=max(maxi,sumNum)
        return maxi
                