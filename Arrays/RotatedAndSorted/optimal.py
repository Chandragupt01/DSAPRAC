class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        rotations=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                rotations+=1
        if rotations>1:
            return False
        return True