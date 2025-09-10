from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        freq = Counter(arr)
        
        
        frequencies = sorted(freq.values(), reverse=True)
        
        
        half = len(arr) // 2
        removed = 0
        set_size = 0
        
        for f in frequencies:
            removed += f
            set_size += 1
            if removed >= half:
                return set_size
        
        
        return set_size

solution = Solution()
result = solution.minSetSize([3,3,3,3,5,5,5,2,2,7])
print(result)