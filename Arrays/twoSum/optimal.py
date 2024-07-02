class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=dict()
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in res:
                return [i,res[rem]]
            res[nums[i]]=i