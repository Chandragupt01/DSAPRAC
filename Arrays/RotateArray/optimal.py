class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        rotations=k%n
        def reverse(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1
        reverse(0,n-1)
        reverse(0,rotations-1)
        reverse(rotations,n-1)
