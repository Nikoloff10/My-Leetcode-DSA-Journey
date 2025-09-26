class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        char_index = {}
        
        max_length = 0
        window_start = 0
        
        for window_end, char in enumerate(s):
            
            if char in char_index and char_index[char] >= window_start:
                
                window_start = char_index[char] + 1
            
            
            char_index[char] = window_end
            
           
            current_length = window_end - window_start + 1
            max_length = max(max_length, current_length)
        
        return max_length
        
solution = Solution()
result = solution.lengthOfLongestSubstring("pwwkew")
print(result)