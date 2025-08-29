class Solution(object):

    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        stack = []
        index = 0

        for x in pushed:
            stack.append(x)

            while stack and index < len(popped) and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return not stack


solution = Solution()

result = solution.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
print(result)
