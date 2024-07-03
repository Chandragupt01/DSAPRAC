class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=dict()
        n=len(nums)
        for i in range(n):
            hashmap[nums[i]]=hashmap.get(nums[i],0)+1
        for k,v in hashmap.items():
            if v>(n//2):
                return k