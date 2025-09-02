import heapq
from math import floor # that's a no no


class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        

        for i in range(k):
            x = -heapq.heappop(piles)
            heapq.heappush(piles, -(x - x//2))
        return -sum(piles)



solution = Solution()
result = solution.minStoneSum([5,4,9], 2)
print(result)