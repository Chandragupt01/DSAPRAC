class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        count=0
        n=len(nums)
        i=0
        while i < n:
            if nums[i]==0:
                count=0
            if nums[i]==1:
                count+=1
                maxi=max(maxi,count)
            i+=1
        return maxi
    
    
    # alternateSolution
    """class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                maxi = max(maxi, cnt)
                cnt = 0
        return max(maxi, cnt)"""