class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)

        prev2 = cost[0]  
        prev1 = cost[1]  

        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
        
        return min(prev1, prev2)


solution = Solution()
result = solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
print(result)


