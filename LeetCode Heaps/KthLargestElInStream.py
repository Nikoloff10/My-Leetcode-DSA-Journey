import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

kth_largest = KthLargest(3, [4, 5, 8, 2])
print(kth_largest.add(3)) 
print(kth_largest.add(5)) 
print(kth_largest.add(10))
print(kth_largest.add(9)) 
print(kth_largest.add(4)) 
