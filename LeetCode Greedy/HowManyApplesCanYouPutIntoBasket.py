class Solution(object):
    def maxNumberOfApples(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
       
        weight.sort()
        
        total_weight = 0
        count = 0
        for w in weight:
            if total_weight + w <= 5000:
                total_weight += w
                count += 1
            else:
                break
        
        return count
    

solution = Solution()
result = solution.maxNumberOfApples([100,200,150,1000])
print(result)
