class Solution(object):
    def sortedSquares(self, nums):
        
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        nums.sort()

        return nums

solution = Solution()
result = solution.sortedSquares([-7,-3,2,3,11])
print(result)