class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxi=0
        minIndex=float("inf")
        for i in range(n):
            minIndex=min(minIndex,prices[i])
            maxi=max(maxi,prices[i]-minIndex)
        return maxi