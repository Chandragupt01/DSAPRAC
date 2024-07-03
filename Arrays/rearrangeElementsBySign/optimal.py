class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        posIdx=0
        negIdx=1
        for i in range(n):
            if nums[i]>0:
                res[posIdx]=nums[i]
                posIdx+=2
            else:
                res[negIdx]=nums[i]
                negIdx+=2
        return res