class Solution(object):
    def maximizeSweetness(self, sweetness, k):
        total = sum(sweetness)
        left, right = 1, total
        
        def can_divide(mid):
            count = 0
            current_sum = 0
            for s in sweetness:
                current_sum += s
                if current_sum >= mid:
                    count += 1
                    current_sum = 0
            return count >= k + 1
        
        while left < right:
            mid = (left + right + 1) // 2
            if can_divide(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
        

solution = Solution()
result = solution.maximizeSweetness([1,2,3,4,5,6,7,8,9], 5)
print(result)