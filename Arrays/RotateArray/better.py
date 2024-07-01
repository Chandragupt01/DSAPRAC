class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        rotations=k%n
        nums[:]=nums[n-rotations:]+nums[:n-rotations]