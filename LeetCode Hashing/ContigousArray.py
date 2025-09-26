class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        sum_to_index = {0: -1}  
        max_length = 0
        running_sum = 0
    
        for i, num in enumerate(nums):
        
            running_sum += 1 if num == 1 else -1
        
        
            if running_sum in sum_to_index:
                max_length = max(max_length, i - sum_to_index[running_sum])
            else:
            
                sum_to_index[running_sum] = i
    
        return max_length

solution = Solution()
print(solution.findMaxLength([0,1,0]))