class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[]
        for i in nums:
            if i!=0:
                res.append(i)
        for i in range(len(res)):
            nums[i]=res[i]
        for i in range(len(res),len(nums)):
            nums[i]=0
            
