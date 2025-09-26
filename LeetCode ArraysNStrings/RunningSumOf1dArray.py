class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        runSum = []

        for i in range(len(nums)):
            nums[i] += runSum[i-1] if i > 0 else 0
            runSum.append(nums[i])

        return runSum

solution = Solution()
result = solution.runningSum([3,1,2,10,1])
print(result)