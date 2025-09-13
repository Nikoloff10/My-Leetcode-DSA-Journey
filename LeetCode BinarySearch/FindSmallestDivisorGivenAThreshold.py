class Solution(object):
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)
        
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for num in nums:
                total += (num + mid - 1) // mid
            if total <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        

solution = Solution()
result = solution.smallestDivisor([1,2,5,9], 6)
print(result)