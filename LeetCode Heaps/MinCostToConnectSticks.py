import heapq


class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """

        if len(sticks) <= 1:
            return 0

        heap = [stick for stick in sticks]
        heapq.heapify(heap)
        ans = 0
        while len(heap) != 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            z = x + y
            ans += z
            heapq.heappush(heap, z)
        return ans

solution = Solution()
result = solution.connectSticks([1,8,3,5])
print(result)