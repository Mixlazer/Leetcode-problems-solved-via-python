class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxwin = 0
        minprice = 0
        
        for right in range(1, len(prices)):
            if prices[right] < prices[minprice]:
                minprice = right 
            else:
                maxwin = max(maxwin, prices[right] - prices[minprice])
        
        return maxwin

