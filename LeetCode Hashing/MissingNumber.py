class Solution(object):
    def missingNumber(self, nums):
        
        nums.sort()
        n = len(nums)

        for i in range(n + 1):
            if i not in nums:
                return i
        
        return n  
        
solution = Solution()
print(solution.missingNumber([1]))