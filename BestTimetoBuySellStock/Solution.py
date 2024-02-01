class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while(r < len(prices)):
            if(prices[l] > prices[r]):
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            r+=1
        return maxProfit
        