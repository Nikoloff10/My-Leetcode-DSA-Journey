class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        max_len = 0
        zeros_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1

            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


solution = Solution()
result = solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
print(result)