class Solution(object):
    def minStartValue(self, nums):
        
        startVal = 1

        while True:
            sum = startVal
            valid = True

            for num in nums:
                sum += num

                if sum < 1:
                    valid = False
                    break

            if valid:
                return startVal
            else:
                startVal += 1

solution = Solution()
result = solution.minStartValue([1,-2,-3])
print(result)