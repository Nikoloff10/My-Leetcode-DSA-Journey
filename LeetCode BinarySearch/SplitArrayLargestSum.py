class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        
        def can_split(mid):
            count = 1
            current = 0
            for num in nums:
                current += num
                if current > mid:
                    count += 1
                    current = num
                    if count > k:
                        return False
            return True
        
        while low < high:
            mid = (low + high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
        
solution = Solution()
result = solution.splitArray([7,2,5,10,8], 2)
print(result)