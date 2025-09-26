from collections import defaultdict


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        word = "balloon"

        occurs = defaultdict(int)
        occurs_word = defaultdict(int)

        for letter in word:
            occurs_word[letter] += 1

        for letter in text:
            if letter in word and letter in text:
                occurs[letter] += 1

        result = float('inf')
        for letter in occurs_word:
            if letter not in occurs:
                return 0
            else:
                result = min(result, occurs[letter] // occurs_word[letter])
        return result
    
solution = Solution()
print(solution.maxNumberOfBalloons("balon"))