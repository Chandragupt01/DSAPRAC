class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxi=0
        for i in range(n):
            for j in range(i+1,n):
                if prices[i]<prices[j]:
                    maxi=max(maxi,prices[j]-prices[i])
        return maxi