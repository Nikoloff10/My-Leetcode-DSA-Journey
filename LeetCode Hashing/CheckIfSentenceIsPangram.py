class Solution(object):
    def checkIfPangram(self, sentence):
        
        seen = set()

        for letter in sentence:
            if letter not in seen:
                seen.add(letter)
        if len(seen) == 26:
            return True
        else:
            return False


        
solution = Solution()
print(solution.checkIfPangram("leetcode"))