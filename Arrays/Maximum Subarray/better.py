class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float("-inf")
        for i in range(n):
            sumNum=0
            for j in range(i,n):
                sumNum+=nums[j]
                maxi=max(maxi,sumNum)
        return maxi