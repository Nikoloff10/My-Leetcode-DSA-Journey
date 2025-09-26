class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, n):
            for j in range(n):
                
                dp[i][j] = matrix[i][j]  
                candidates = []
                candidates.append(dp[i-1][j])

                if j > 0:
                    candidates.append(dp[i-1][j-1])
                if j < n-1:
                    candidates.append(dp[i-1][j+1])

                dp[i][j] += min(candidates)
        
        return min(dp[n-1])


solution = Solution()
result = solution.minFallingPathSum([[-19,57],[-40,-5]])
print(result)
