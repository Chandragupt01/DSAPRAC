class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[]
        for i in range(1,n+1):
            if i not in nums:
                arr.append(i)
        return arr