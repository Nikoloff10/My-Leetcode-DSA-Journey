class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, current_combination, remaining_sum, remaining_count):
            
            if remaining_count == 0 and remaining_sum == 0:
                res.append(current_combination[:])  
                return
                        
            if remaining_count == 0 or remaining_sum <= 0:
                return
        
            for num in range(start, 10):
                
                if num > remaining_sum:
                    break
                current_combination.append(num)
                backtrack(num + 1, current_combination, remaining_sum - num, remaining_count - 1)
                current_combination.pop()
        
        backtrack(1, [], n, k)
        return res


solution = Solution()


result = solution.combinationSum3(3, 7)
print(result)