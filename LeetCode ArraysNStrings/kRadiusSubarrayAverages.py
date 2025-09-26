class Solution(object):
    def getAverages(self, nums, k):
        
        if k == 0:
            return nums
        
        n = len(nums)
        radius = [-1] * n
        
        if 2 * k + 1 > n:
            return radius
        
        window_sum = 0
        for i in range(min(2 * k + 1, n)):
            window_sum += nums[i]
        
        for i in range(k, n - k):
            radius[i] = window_sum // (2 * k + 1)
            if i + k + 1 < n:
                window_sum += nums[i + k + 1]
            if i - k >= 0:
                window_sum -= nums[i - k]
                
        return radius

solution = Solution()
result = solution.getAverages([7,4,3,9,1,8,5,2,6], 3)
print(result)