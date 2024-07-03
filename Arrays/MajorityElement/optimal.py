class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=nums[0]
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]==candidate:
                count+=1
            else:
                count-=1
            if count==0:
                candidate=nums[i]
                count=1
        return candidate