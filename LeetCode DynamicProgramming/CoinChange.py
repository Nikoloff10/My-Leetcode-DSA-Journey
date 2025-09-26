class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount == 0:
            return 0
          
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  

        for i in range(1, amount + 1): 
            for coin in coins:   
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1


solution = Solution()
result = solution.coinChange([1, 2, 5], 11)
print(result)



