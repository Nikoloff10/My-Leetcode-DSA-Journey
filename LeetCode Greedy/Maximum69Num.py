class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        num_str = str(num)
        
        
        for i in range(len(num_str)):
            if num_str[i] == '6':
                
                new_num_str = num_str[:i] + '9' + num_str[i+1:]
                return int(new_num_str)
        
        
        return num

solution = Solution()
result = solution.maximum69Number(9996)
print(result)