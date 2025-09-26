class Solution(object):

    def findMaxAverage(self, nums, k):

        if k > len(nums):
            return

        curr = float(sum(nums[:k]))
        max_sum = curr
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr)
        max_sum = max_sum / k

        return max_sum


solution = Solution()
result = solution.findMaxAverage([1,12,-5,-6,50,3], 4)
print(result)