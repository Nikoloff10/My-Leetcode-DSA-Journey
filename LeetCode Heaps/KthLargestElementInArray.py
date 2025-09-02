import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        for _ in range(k):
            x = heapq.heappop(heap)

        return -x

solution = Solution()
result = solution.findKthLargest([3,2,1,5,6,4], 2) 
print(result)