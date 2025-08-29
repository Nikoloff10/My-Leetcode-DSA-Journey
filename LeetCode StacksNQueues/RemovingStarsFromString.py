class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        result = []

        for i in range(len(s)):
            stack.append(s[i])

        for i in range(len(stack)):
            if stack[i] != "*":
                result.append(stack[i])
            else:
                result.pop()
        return "".join(result)
        

solution = Solution()

answer = solution.removeStars("leet**cod*e")
print(answer)