class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        
        n = len(prices)

        hold = -prices[0]  
        sold = 0           
        
        for i in range(1, n):    
            prev_hold = hold
            hold = max(hold, sold - prices[i])
            sold = max(sold, prev_hold + prices[i] - fee)

        return sold


solution = Solution()
result = solution.maxProfit([1, 3, 7, 5, 10, 3], 3)
print(result)


