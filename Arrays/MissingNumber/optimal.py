class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        SumNum=(n*(n+1))//2
        sumArr=sum(nums)
        return SumNum - sumArr