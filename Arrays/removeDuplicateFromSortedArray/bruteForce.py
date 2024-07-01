class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        freq=dict()
        for i in range(0,n):
            freq[nums[i]]=0
        j=0
        for key in freq:
            nums[j]=key
            j+=1
        return len(freq)
