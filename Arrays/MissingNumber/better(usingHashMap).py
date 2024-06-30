class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        freq={i:0 for i in range(n+1)}
        for i in range(n):
            freq[nums[i]]+=1
        for k,v in freq.items():
            if v == 0:
                return k