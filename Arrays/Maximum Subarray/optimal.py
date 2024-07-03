class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=float("-inf")
        maxi=float("-inf")
        n=len(nums)
        for i in range(n):
            if currSum<0:
                currSum=0
            currSum+=nums[i]
            maxi=max(maxi,currSum)
        return maxi