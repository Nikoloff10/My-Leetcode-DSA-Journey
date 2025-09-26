class Solution(object):
    def countElements(self, arr):
        
        count = 0
        for x in arr:
            if x + 1 in arr:
                count += 1
        return count
    
solution = Solution()
print(solution.countElements([1,1,3,3,5,5,7,7]))