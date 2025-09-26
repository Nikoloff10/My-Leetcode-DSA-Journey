from collections import defaultdict


class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurs = defaultdict(int)
        unique_set = set()

        for num in nums:
            unique_set.add(num)
            occurs[num] += 1

        unique = sorted([num for num, occur in occurs.items() if occur == 1])

        if unique:
            return unique[-1]
        else:
            return -1

solution = Solution()
print(solution.largestUniqueNumber([5,7,3,9,4,9,8,3,1]))