class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=i+1
        while j<n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1
