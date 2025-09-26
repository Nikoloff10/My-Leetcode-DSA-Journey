class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        magazine_counts = {}
        for char in magazine:
            if char in magazine_counts:
                magazine_counts[char] += 1
            else:
                magazine_counts[char] = 1
        
        for char in ransomNote:
            if char not in magazine_counts or magazine_counts[char] <= 0:
                return False
        
            magazine_counts[char] -= 1
        
        return True

solution = Solution()
result = solution.canConstruct("aa", "aab")
print(result)