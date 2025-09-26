class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
        
        n = len(prices)

        held = -prices[0]  
        sold = 0          
        rest = 0          
        
        for i in range(1, n):
            prev_held = held
            prev_sold = sold
            prev_rest = rest
            
            held = max(prev_held, prev_rest - prices[i])
            sold = prev_held + prices[i]
            rest = max(prev_rest, prev_sold)
        
        return max(sold, rest)


solution = Solution()
result = solution.maxProfit([1])
print(result)