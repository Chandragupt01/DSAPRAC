class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        freqMap={i:0 for i in range(1,n+1)}
        for i in nums:
            freqMap[i]+=1
        for k,v in freqMap.items():
            if v==0:
                res.append(k)
        return res