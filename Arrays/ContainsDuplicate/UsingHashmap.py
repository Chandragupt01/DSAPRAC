class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap=dict()
        for num in nums:
            if num in hashMap and hashMap[num]>=1:
                return True
            hashMap[num]=hashMap.get(num,0)+1
        return False