class Solution(object):
    def answerQueries(self, nums, queries):
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for num in nums:
            for j in range(n, 0, -1):
                if dp[j-1] != float('inf'):
                    dp[j] = min(dp[j], dp[j-1] + num)
        
        answer = []
        for q in queries:
            max_size = 0
            for k in range(n + 1):
                if dp[k] <= q:
                    max_size = k
            answer.append(max_size)
        
        return answer
        
solution = Solution()
result = solution.answerQueries([4,5,2,1], [3,10,21])
print(result)